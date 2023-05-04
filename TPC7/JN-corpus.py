#!/usr/bin/env python3

import os
import datetime
import re


path_ = "../TPC6/corpus"

corpus = ""

for pasta in os.listdir(path_):
    if os.path.isdir(path_ + "/" + pasta):
        corpus_path = path_ + "/" + pasta + "/" + ".corpus.txt"
        with open(corpus_path, 'r') as f:
            corpus += f.read()

with open("JN-corpus.txt", 'w') as f:
    f.write(corpus)

# junta todos os corpus num só