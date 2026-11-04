#!/bin/sh
# $1 reel.mp4  $2 copertina 1080x1920  $3 uscita
set -e
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
ffmpeg -v error -y -loop 1 -t 0.7 -framerate 30 -i "$2" -i "$1" -filter_complex \
"[0:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1,settb=1/30[c];[1:v]fps=30,format=yuv420p,setsar=1,settb=1/30[v];[c][v]xfade=transition=fade:duration=0.2:offset=0.5,format=yuv420p[o];[1:a]adelay=300|300,apad=pad_dur=0.5[a]" \
-map "[o]" -map "[a]" -t $(echo "$D + 0.5" | bc) -c:v libx264 -preset veryfast -crf 19 -c:a aac -b:a 160k -movflags +faststart "$3"
