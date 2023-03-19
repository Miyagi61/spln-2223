### TPC3

## Ficheiros importantes
- lex.py
- parser.py
- saida.html
- exemplo.txt

## Resumo

Após alterar um pouco a gramática a que cheguei no TPC2, cheguei à seguinte:

    dic : es

    es : es LINHA_B e
    es : e

    e : items

    items : items item
    items : item

    item : at_conc
    item : lings

    lings : lings ling
    lings : ling

    ling : ID_LING DOIS_PONTOS ts

    at_conc : ID2 DOIS_PONTOS VAL

    ts : ts t
    ts : t 

    t : PONTO VAL at_ts

    at_ts : at_ts at_t
    at_ts : 

    at_t : ID DOIS_PONTOS VAL
    
Um exemplo não relacionado com medicina de uma entrada válida está no ficheiro exemplo.txt. Após retirar os dados cria uma nova vista html para os dados guardados em memória. 