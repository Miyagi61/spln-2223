#!/usr/bin/env python3

import sys
import fileinput
import re

text = ""

for line in fileinput.input():
    text += line


# 0 - QUEBRAS DE PAGINA ++
# 1 - SEPARAR PONTUACAO DAS PALAVRAS
# 2 - MARCAR CAPITULOS ++
# 3 - SEPARAR PARAGRAFOS DE LINHAS PEQUENAS
# 4 - JUNTAR LINHAS DA MESMA FRASE
# 5 - QUEBRAR AS FRASES
# #

regex_exp = r'.*(CAP[IÍ]TULO\s+\w+).*'
res = re.sub(regex_exp,r'\n# \1',text)

regex_nl = r'([a-z0-9,;])\n\n([a-z0-9])'
res = re.sub(regex_nl,r'\1=\n\2',text)

regex_poema = r'<poema>(.*?)</poema>'

arr_poemas = []

def guarda_poema(poema):
    arr_poemas.append(poema[1])
    print(poema)
    return f'»{len(arr_poemas)}«'


text = re.sub(regex_poema, guarda_poema, text, flags=re.S)
# re.S faz com que o .* incluia tmb \n


print(res)
