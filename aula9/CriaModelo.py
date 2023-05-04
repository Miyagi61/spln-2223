#! /usr/bin/env python3
import argparse
import os
from glob import glob
from gensim.utils import tokenize
from gensim.models import Word2Vec

parser = argparse.ArgumentParser(
    prog='CriaModelo',
    epilog='Made for SPLN 2022/2023'
)

parser.add_argument('-d',"--dir", help='Directory with txt files')
parser.add_argument('-o',"--out", default='output.wv', help='Output file')
parser.add_argument('-e',"--ephochs", default=5, help='Number of ephochs')
parser.add_argument('-s',"--dim", default=300, help='Dimension of the vector')

args = parser.parse_args()

ephochs = args.ephochs
dim = args.dim
out = args.out

if not args.dir:
    dir = '/home/miyagi/Desktop/spln-2223/TPC6/corpus/'
    files = []
    # access folder inside dir and get all txt files
    for subdir in os.listdir(dir):
        aux = dir + subdir
        if os.path.isdir(aux):
            files += glob(aux + '/.corpus.txt')   
else:
    files = glob(args.dir + '/*.txt')



cont = []

for file in files:
    fd = open(file, 'r')
    for line in fd:
        cont.append(list(tokenize(line,lower=True)))


model = Word2Vec(cont, epochs=ephochs, vector_size=dim)

model.save(out)

