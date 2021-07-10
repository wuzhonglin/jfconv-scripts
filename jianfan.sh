#/bin/sh
cd `dirname $0`
export PYTHONUNBUFFERED=1
./jianfan_preprocess.pl | ./decoder.py ./fanti.bin | ./jianfan_postprocess.pl
