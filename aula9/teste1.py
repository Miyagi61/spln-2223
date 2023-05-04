#! /usr/bin/env python3

from gensim.models import Word2Vec
import gensim
import argparse

parser = argparse.ArgumentParser(
    prog='Teste0',
    epilog='Made for SPLN 2022/2023'
)

parser.add_argument('-m',"--model", help='Directory with txt files')
parser.add_argument('-s','--similaridades', default='sim.txt', help='File with analogies')

args = parser.parse_args()

modelArg = args.model
input = args.similaridades

model = Word2Vec.load(modelArg)

fd = open(input, 'r')

for line in fd:
    words = line.split(" ")
    if len(words) == 3:
        w1, w2, w3 = words
        print(model.wv.similarity(w1,w2))
        print(model.wv.similarity(w1,w3))



