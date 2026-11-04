import sys, subprocess, re, os
n = sys.argv[1]
cop = open(f'out2/s{n}/copione.txt').read().splitlines()
times = [float(l.split('-')[0]) + 1.4 for l in cop]
# un fotogramma per frase, a metà risoluzione
os.makedirs('test/ctl', exist_ok=True)
fs = []
for i, t in enumerate(times):
    f = f'test/ctl/{n}_{i:02d}.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', f'out2/s{n}/reel.mp4', '-frames:v', '1', '-vf', 'scale=432:-1', f], check=True)
    fs.append(f)
cols = 6
rows = (len(fs) + cols - 1) // cols
args = []
for f in fs: args += ['-i', f]
pad = cols * rows - len(fs)
flt = ''.join(f'[{i}]' for i in range(len(fs)))
subprocess.run(['ffmpeg', '-v', 'error', '-y', *args, '-filter_complex', f'{flt}xstack=inputs={len(fs)}:layout=' + '|'.join(f'{(i % cols) * 432}_{(i // cols) * 768}' for i in range(len(fs))) + ':fill=black', f'test/ctl/foglio_{n}.png'], check=True)
print(f'test/ctl/foglio_{n}.png', len(fs))
