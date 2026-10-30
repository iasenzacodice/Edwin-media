"""Orecchio di Edwin: trascrive l'audio con Whisper small (ONNX) per controllare la pronuncia."""
import base64, wave, sys, re, unicodedata
import numpy as np
import onnxruntime as ort

D = '/tmp/asr/sherpa-onnx-whisper-small'
enc = ort.InferenceSession(f'{D}/small-encoder.int8.onnx', providers=['CPUExecutionProvider'])
dec = ort.InferenceSession(f'{D}/small-decoder.int8.onnx', providers=['CPUExecutionProvider'])
TOK = {}
for line in open(f'{D}/small-tokens.txt', encoding='utf-8'):
    t, i = line.rstrip('\n').rsplit(' ', 1)
    TOK[int(i)] = base64.b64decode(t)
SR = 16000


def mel_filters(n_mels=80, n_fft=400, sr=16000):
    def hz2mel(f):
        f = np.asarray(f, float)
        m = f / (200.0 / 3)
        log = f >= 1000
        m = np.where(log, 15 + np.log(np.maximum(f, 1e-9) / 1000) / (np.log(6.4) / 27), m)
        return m

    def mel2hz(m):
        m = np.asarray(m, float)
        f = m * (200.0 / 3)
        log = m >= 15
        return np.where(log, 1000 * np.exp((np.log(6.4) / 27) * (m - 15)), f)
    fft = np.linspace(0, sr / 2, n_fft // 2 + 1)
    mpts = mel2hz(np.linspace(hz2mel(0), hz2mel(sr / 2), n_mels + 2))
    fd = np.diff(mpts)
    ramps = mpts[:, None] - fft[None, :]
    w = np.zeros((n_mels, len(fft)))
    for i in range(n_mels):
        lo = -ramps[i] / fd[i]
        hi = ramps[i + 2] / fd[i + 1]
        w[i] = np.maximum(0, np.minimum(lo, hi))
    w *= (2.0 / (mpts[2:n_mels + 2] - mpts[:n_mels]))[:, None]
    return w


MEL = mel_filters()


def logmel(y):
    y = np.pad(y, (200, 200), mode='reflect')
    win = np.hanning(401)[:-1]
    n = 1 + (len(y) - 400) // 160
    frames = np.stack([y[i * 160:i * 160 + 400] * win for i in range(n)])
    spec = np.abs(np.fft.rfft(frames, axis=1)) ** 2
    m = MEL @ spec.T
    lm = np.log10(np.maximum(m, 1e-10))
    lm = np.maximum(lm, lm.max() - 8.0)
    return ((lm + 4.0) / 4.0)[:, :-1] if lm.shape[1] > 1 else (lm + 4.0) / 4.0


def load(path):
    with wave.open(path) as w:
        sr = w.getframerate(); ch = w.getnchannels()
        a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    if ch > 1:
        a = a.reshape(-1, ch).mean(1)
    if sr != SR:
        t = np.arange(0, len(a) / sr, 1 / SR)
        a = np.interp(t, np.arange(len(a)) / sr, a).astype(np.float32)
    return a


def transcribe(path):
    y = load(path)[:30 * SR]
    m = logmel(y)
    m = np.pad(m, ((0, 0), (0, 3000 - m.shape[1])), constant_values=m.min()) if m.shape[1] < 3000 else m[:, :3000]
    ck, cv = enc.run(None, {'mel': m[None].astype(np.float32)})
    sk = np.zeros((12, 1, 448, 768), np.float32); sv = np.zeros_like(sk)
    toks = [50258, 50274, 50359, 50363]   # sot, it, transcribe, no_timestamps
    out = []
    logits, sk, sv = dec.run(None, {'tokens': np.array([toks], np.int64), 'in_n_layer_self_k_cache': sk, 'in_n_layer_self_v_cache': sv,
                                    'n_layer_cross_k': ck, 'n_layer_cross_v': cv, 'offset': np.array([0], np.int64)})
    off = len(toks)
    for _ in range(200):
        t = int(np.argmax(logits[0, -1]))
        if t == 50257:
            break
        out.append(t)
        logits, sk, sv = dec.run(None, {'tokens': np.array([[t]], np.int64), 'in_n_layer_self_k_cache': sk, 'in_n_layer_self_v_cache': sv,
                                        'n_layer_cross_k': ck, 'n_layer_cross_v': cv, 'offset': np.array([off], np.int64)})
        off += 1
    return b''.join(TOK[t] for t in out if t < 50257).decode('utf-8', 'replace').strip()


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r"[a-z0-9]+", s.replace("'", ' '))


def diff(ref, hyp):
    import difflib
    a, b = norm(ref), norm(hyp)
    sm = difflib.SequenceMatcher(None, a, b)
    bad = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            bad.append((' '.join(a[i1:i2]), ' '.join(b[j1:j2])))
    return bad


if __name__ == '__main__':
    print(transcribe(sys.argv[1]))
