#! /usr/bin/python3
import bs4
from bs4 import BeautifulSoup as bs
import requests

import sys

url = sys.argv[1]

if sys.argv[2]:
    goal = int(sys.argv[2])

conteudo = requests.get(url).text

doc_tree = bs(conteudo, 'lxml')

tabelas = doc_tree.find_all('table')

idx = 0
for tabela in tabelas:
    idx += 1
    if goal and idx != goal:
        continue

    print("-----------------","Tabela",idx,"-----------------")
    linhas = tabela.find_all('tr')
    for linha in linhas:
        celulas = [cel.text for cel in linha.find_all('td')]
        linha_txt = "::".join(celulas)
        print(linha_txt)
            


# fazer um get links (a href)
# | grep categoria
# for a in $(get_links <url>| grep category ): do get_tables $a; done