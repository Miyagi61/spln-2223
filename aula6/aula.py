#!/usr/bin/env python3

import spacy
from collections import Counter

nlp = spacy.load('pt_core_news_lg')

text = open('Harry.txt').read()

doc = nlp(text)

#for w in doc:
#    print(w,w.pos_,w.lemma, w.ent_iob_, w.ent_type_)
#
#print("--------------")
#
#for w in doc.ents:
#    print(w.text, w.start_char, w.end_char, w.label_)
#
#print("--------------")

dic = Counter()
for s in doc.sents:
    for w in s:
        if w.pos_ == "VERB":
            dict[w.lemma_] += 1

dict_norm = Counter()

for key,value in dic.items():
    if value > 5:
        dict_norm[key] = value

lemas = open('lemas.txt').readlines()

dict_lema = Counter()
for line in lemas:
    campos = line.split()
    if len(line) >= 2:
        dict_lema[campos[1]] = int(campos[0])

print(dic.most_common(10))
print(dict_norm.most_common(10))
print(dict_lema.most_common(10)) 


f = open("resultados.txt","w")
for verb in dict_norm.items():
    f.write(value/dict_lema.get(verb,100),verb)

f.close()






