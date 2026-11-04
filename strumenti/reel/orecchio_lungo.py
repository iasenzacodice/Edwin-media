"""Trascrive tutta la voce a pezzi (<28 s) tagliando nei silenzi."""
import sys, wave, numpy as np, subprocess, os, tempfile
import orecchio
p = sys.argv[1]
w = wave.open(p); sr = w.getframerate(); y = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
hop = sr // 100; n = len(y) // hop
r = np.sqrt(np.mean(y[:n * hop].reshape(n, hop) ** 2, axis=1))
cuts = [0]; 
while (n - cuts[-1]) / 100 > 26:
    lo, hi = cuts[-1] + 1500, cuts[-1] + 2600
    i = lo + int(np.argmin(np.convolve(r[lo:hi], np.ones(30) / 30, 'same')))
    cuts.append(i)
cuts.append(n)
out = []
for a, b in zip(cuts, cuts[1:]):
    seg = y[a * hop:b * hop]
    f = tempfile.mktemp(suffix='.wav')
    with wave.open(f, 'wb') as o:
        o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes((seg * 32767).astype(np.int16).tobytes())
    out.append(orecchio.transcribe(f)); os.remove(f)
print(' | '.join(out))
