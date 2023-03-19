#! /usr/bin/env python3

import sys
import fileinput
import re

text = ""

for line in fileinput.input():
    text += line


# 0 - QUEBRAS DE PAGINA ++
# 1 - SEPARAR PONTUACAO DAS PALAVRAS ++
# 2 - MARCAR CAPITULOS ++
# 3 - SEPARAR PARAGRAFOS DE LINHAS PEQUENAS 
# 4 - JUNTAR LINHAS DA MESMA FRASE ++
# 5 - QUEBRAR AS FRASES ++
# #

regex_exp = r'.*(CAP[IÍ]TULO\s+\w+).*'
res = re.sub(regex_exp,r'\n# \1',text)

regex_nl = r'([a-z0-9,;])\n\n([a-z0-9])'
res = re.sub(regex_nl,r'\1=\n\2',res)

regex_poema = r'<poema>(.*?)</poema>'

arr_poemas = []

def guarda_poema(poema):
    arr_poemas.append(poema[1])
    print(poema)
    return f'»{len(arr_poemas)}«'


res = re.sub(regex_poema, guarda_poema, res, flags=re.S)
# re.S faz com que o .* incluia tmb \n

regex_junta = r'([^\.?!\n])\n(\w)'
res = re.sub(regex_junta,r"\1 \2",res)

regex_par = r'(.)\n([^–])'
res = re.sub(regex_par,r"\1\n\n\2",res,flags=re.UNICODE)

regex_erro = r'\n+([a-z])'
res = re.sub(regex_erro,r'\1',res)

regex_sep = r'(\w)([,.;!?])'
res = re.sub(regex_sep,r'\1 \2',res)

regex_sep2 = r'([,.;!?])(\w)'
res = re.sub(regex_sep2,r'\1 \2',res)

regex_frase = r'([^–].*?[\.?!])\s*(.*)' 
while (res != re.sub(regex_frase,r'\1\n\2',res,flags=re.UNICODE)):
    res = re.sub(regex_frase,r'\1\n\2',res,flags=re.UNICODE)

regex_SR = r'(Sra?)\s*(\.)\n+(\w)'
res = re.sub(regex_SR,r'\1\2 \3',res)

print(res)
