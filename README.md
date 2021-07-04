jfconv-scripts: Simplified/Traditional Chinese Converter
==========

How To Use
----------


First, you need to download language models for simplified and traditional Chinese.

[fanti.bin](https://drive.google.com/file/d/18lF4lrxtWFACRJdEiZDkBIokoKmJQQfM/view)

[jianti.bin](https://drive.google.com/file/d/1Mj-7-8ib1AIt8pPPLCayLJPhqKxJ9XXH/view)


Alternately, you can build your own language models.

Install KenLM on your system and prepare Chinese corpora in simplified and traditional Chinese. (ex. jianti.txt, fanti.txt)

Then build the language models (names must be jianti.bin and fanti.bin):

    $ perl -Mutf8 -CSD -F/\\t/ -nale 'tr/ /\x{e000}/; print join(" ", split(//, $_))' jianti.txt > jianti_space.txt
    $ lmplz -o4 --prune 0 5 10 15 < jianti_space.txt > jianti.arpa
    $ build_binary jianti.arpa jianti.bin


Now you can perform conversion:

    $ echo "干燥 干部 干涉" | ./jianfan.sh
    乾燥 幹部 干涉

    $ echo "乾燥 乾坤" | ./fanjian.sh
    干燥 乾坤

The results may vary depending on the corpora.
