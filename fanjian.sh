#/bin/sh
cd `dirname $0`
export PYTHONUNBUFFERED=1
./jianfan_preprocess.pl --reverse | ./decoder.py ./jianti.bin | ./jianfan_postprocess.pl
