### TPC1

## Ficheiros importantes
- medicina.py
- medicina.txt
- medicina.json

## Resumo

Em primeiro lugar passei o ficheiro xml para txt.
Ao ficheiro txt, utilizando uma série de substituições e aplicação de marcas, procedi à organização
da informação. As substituições foram realizadas tendo em consideração principalmente a fonte associada
ao texto em xml. Após esta primeira fase, seguiu-se uma parte mais minuciosa para englobar alguns casos 
específicos.

Tendo a organização feita, a informação foi armazenada num ficheiro json, sendo este composto por duas chaves principais 'R' e 'C' para as entradas remissivas e completas. As entradas remissivas são compostas por um nome (que funciona como chave) e o valor respetivo em forma de string. As entradas completas são compostas por uma chave (id) e o valor é um dicionário com os seguintes campos:
  -  nome (string)
  -  info (lista)
  -  genero (lista)
  -  areas (lista)
  -  linguas (dicionario)
  -  nota (string)
O campo info é consituido por elementos SIN e VAR.
O campo linguas é um dicionario em que as chaves são as línguas (p.e.: "en") e o valor é uma lista das traduções naquela língua.


