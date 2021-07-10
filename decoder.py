#!/usr/bin/env python3
# coding: utf8

import fileinput
import argparse
import os
import sys

import kenlm

def main():
    parser = argparse.ArgumentParser(description="N-gram decoder")
    parser.add_argument("lm", help="Path to the language model")
    args = parser.parse_args()

    lm = kenlm.LanguageModel(args.lm)
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
    
    for line in sys.stdin:
        line = line.rstrip("\n")
        words_list = [x[1:-1].split("|") if x.startswith("[") and x.endswith("]") else [x] for x in line.split(" ")]
        words_list.insert(0, ["<s>"])
        words_list.append(["</s>"])
        decoded = decode(lm, words_list)
        print(" ".join(decoded[1:-1]))

def decode(lm, words_list):
    bos_state = kenlm.State()
    lm.BeginSentenceWrite(bos_state)
    dict_list = [{bos_state : (0.0, None, "<s>")}]
    for pos in range(0, len(words_list) - 1):
        dict_list.append({})
        for state in dict_list[pos]:
            score = dict_list[pos][state][0]
            for word in words_list[pos + 1]:
                new_state = kenlm.State()
                s = lm.BaseScore(state, word, new_state)
                new_score = score + s
                if new_state not in dict_list[pos + 1] or new_score > dict_list[pos + 1][new_state][0]:
                    dict_list[pos + 1][new_state] = (new_score, state, word)

    best_score = -999999
    best_state = kenlm.State()
    last_dict = dict_list[len(words_list) - 1]
    for state, (score, prev_state, word) in last_dict.items():
        if score > best_score:
            best_score = score
            best_state = state

    ret = []
    for pos in range(len(words_list) - 1, -1, -1):
        t = dict_list[pos][state]
        ret.insert(0, t[2])
        if pos > 0:
            state = t[1]

    return ret

if __name__ == "__main__":
    main()
    
