"""Voce di Edwin con Kokoro (modello neurale open source, Apache 2.0), tutto in locale.

Uso: python3 voce_neurale.py "testo" uscita.wav [voce] [velocità]
voce: im_nicola (default) | if_sara
"""
import ctypes, json, re, sys, wave
import numpy as np
import onnxruntime as ort

DL = '/tmp/tts_dl'
LIB = f'{DL}/piper/libespeak-ng.so.1'
DATA = f'{DL}/piper'          # cartella che contiene espeak-ng-data
VOCAB = json.load(open('/home/claude/thewh1teagle/kokoro-onnx/src/kokoro_onnx/config.json'))['vocab']
SR = 24000

es = ctypes.CDLL(LIB)
es.espeak_Initialize.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_int]
es.espeak_SetVoiceByName.argtypes = [ctypes.c_char_p]
es.espeak_TextToPhonemes.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_int, ctypes.c_int]
es.espeak_TextToPhonemes.restype = ctypes.c_char_p
es.espeak_Initialize(0x02, 0, DATA.encode(), 0)
es.espeak_SetVoiceByName(b'it')

def ipa(chunk):
    out = []
    buf = ctypes.c_char_p(chunk.encode('utf-8'))
    ptr = ctypes.pointer(buf)
    while buf.value:
        r = es.espeak_TextToPhonemes(ptr, 1, 0x02)
        if r:
            out.append(r.decode('utf-8'))
    return ' '.join(out)

# parole da pronunciare in modo speciale (nomi stranieri, sigle)
LESSICO = {'Claude': 'Clòd', 'chat': 'ciàt', 'file': 'fàil', 'email': 'imèil', 'e-mail': 'imèil', 'password': 'pàssuord', 'online': 'onlàin', 'Instagram': 'Ìnstagram', 'instagram': 'ìnstagram', 'Edwin Arc': 'Èduin Ark', 'Edwin': 'Èduin', 'Arc': 'Ark', 'IA': 'i a', "l'IA": "l'i a", '1889': 'milleottocentottantanòve'}

# correzioni dirette sui fonemi (dopo espeak)
FONEMI = {'sˈeɡwimi': 'sˈeɡuimi'}

# s sorda tra vocali (pronuncia standard), parola -> fonemi corretti
# pronunce scelte da Davide a orecchio (30/10/2026): «cosa» con o aperta e s come in «rosa»
S_SORDA = {'cosa': 'kˈɔza', 'cose': 'kˈɔze',
           'controllali': 'kontrˈɔllali', 'controllalo': 'kontrˈɔllalo', 'controllala': 'kontrˈɔllala', 'controllale': 'kontrˈɔllale',
           'automi': 'autˈɔmi', 'autòmi': 'autˈɔmi', 'automa': 'autˈɔma'}
ACCENTATE = 'àèéìòóù'
ATONE = set('il lo la i gli le l un uno una un di a da in con su per tra fra e ed o ma che non mi ti ci vi si ne se '
            'del dello della dei degli delle al allo alla ai agli alle dal dallo dalla dai dagli dalle nel nello nella nei negli nelle '
            'sul sullo sulla sui sugli sulle col coi me te ce ve'.split())
PREP = set('a da di in con su per tra fra'.split())


def word_ipa(w):
    lw = w.lower()
    if lw in ATONE:
        return ipa(w).strip().replace('ˈ', '').replace('ˌ', '').replace('ː', '').replace('ɛ', 'e').replace('ɔ', 'o')
    if lw in S_SORDA:
        return S_SORDA[lw]
    ph = ipa(w).strip()
    # parole tronche (con l'accento sull'ultima vocale): accento principale, così non si attaccano alla parola dopo
    if lw and lw[-1] in ACCENTATE:
        ph = ph.replace('ˌ', '')
        if 'ˈ' not in ph:
            vow = [i for i, c in enumerate(ph) if c in 'aeiouɛɔ']
            if vow:
                i = vow[-1]
                ph = ph[:i] + 'ˈ' + ph[i:]
        if lw in ('è',):
            ph = 'ˈɛ'
    return ph

def phonemize(text):
    for k, v in sorted(LESSICO.items(), key=lambda kv: -len(kv[0])):
        text = re.sub(r'(?<!\w)' + re.escape(k) + r'(?!\w)', v, text)
    parts = re.split(r'([.,;:!?…])', text)
    ph = ''
    for p in parts:
        if not p.strip():
            continue
        if p in '.,;:!?…':
            ph = ph.rstrip() + p + ' '
        else:
            # parola per parola: ogni parola ha il suo spazio e il suo accento
            toks = re.findall(r"[\w']+|[^\w\s]", p.strip())
            ws = []
            prev = ''
            for t in toks:
                if t.lower() in ('me', 'te', 'sé', 'lui', 'lei', 'noi', 'voi', 'loro') and prev in PREP:
                    ws.append(ipa(t).strip()); prev = t.lower(); continue
                prev = t.lower()
                if "'" in t and not t.endswith("'"):
                    a, b = t.split("'", 1)
                    ws.append(ipa(a + "'" + b).strip())
                else:
                    ws.append(word_ipa(t))
            ph += ' '.join(x for x in ws if x) + ' '
    ph = re.sub(r'\([a-z\-]+\)', '', ph)   # toglie i cambi di lingua di espeak, es. (en)...(it)
    ph = ph.replace('ʊ', 'u').replace('ɪ', 'i')
    # affricate come un solo suono (evita la 't' in più, es. artifi-T-ciale)
    for a, b in (('tʃ', 'ʧ'), ('dʒ', 'ʤ'), ('ts', 'ʦ'), ('dz', 'ʣ')):
        ph = ph.replace(a, b)
    for k, v in FONEMI.items():
        ph = ph.replace(k, v)
    return ''.join(c for c in ph if c in VOCAB).strip()

sess = ort.InferenceSession(f'{DL}/kokoro-v1.0.onnx', providers=['CPUExecutionProvider'])
INPUTS = {i.name: i for i in sess.get_inputs()}
TOK = 'input_ids' if 'input_ids' in INPUTS else 'tokens'
voices = np.load(f'{DL}/voices-v1.0.bin')

def tts(text, voice='im_nicola', speed=1.0, gap=0.12):
    """Genera blocchi il più lunghi possibile (max ~480 fonemi) per un'intonazione continua."""
    sentences = [x for x in re.split(r'(?<=[.!?…])\s+', text) if x.strip()]
    blocks, cur = [], ''
    for x in sentences:
        cand = (cur + ' ' + x).strip()
        if cur and len(phonemize(cand)) > 480:
            blocks.append(cur); cur = x
        else:
            cur = cand
    if cur:
        blocks.append(cur)
    audio = []
    for b in blocks:
        ph = phonemize(b)
        toks = [VOCAB[c] for c in ph if c in VOCAB][:508]
        if '+' in voice:
            style = sum(float(w) * voices[n][len(toks) - 1] for n, w in (q.split(':') for q in voice.split('+')))
        else:
            style = voices[voice][len(toks) - 1]
        sp = np.array([speed], dtype=np.int32 if 'int' in INPUTS['speed'].type else np.float32)
        out = sess.run(None, {TOK: np.array([[0, *toks, 0]], dtype=np.int64), 'style': style.astype(np.float32), 'speed': sp})[0]
        audio.append(np.asarray(out).reshape(-1))
        audio.append(np.zeros(int(gap * SR), dtype=np.float32))
    return np.concatenate(audio), blocks

if __name__ == '__main__':
    text, out = sys.argv[1], sys.argv[2]
    voice = sys.argv[3] if len(sys.argv) > 3 else 'im_nicola'
    speed = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
    y, _ = tts(text, voice, speed)
    y = y / (np.max(np.abs(y)) + 1e-9) * 0.9
    with wave.open(out, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((y * 32767).astype(np.int16).tobytes())
    print(out, round(len(y) / SR, 2), 's |', phonemize(text)[:200])
