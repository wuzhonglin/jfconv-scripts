#/bin/sh
cd `dirname $0`
./jianfan_preprocess.pl | ./decoder.py ./fanti.bin | ./jianfan_postprocess.pl
