### TPC2

## Ficheiros importantes
- medicina.py
- medicina.json
- medicina2.json
- lex.py
- parser.py

## Resumo

No ficheiro medicina.py o dicionario galego é transformado num "dicionario médico abstrato", nos quais as entradas são: area e traducoes. Tendo este ultimo campo todas as informações sobre cada língua.

A gramática escolhida para o dicionario foi a seguinte: 
    dic : es
    es : es LINHA_B e
    es : e
    e : items
    items : items item
    items : item
    item : '@' ling
    item : at_conc
    ling : ID_LING ':' ts
    at_conc : ID ':' VAL
    ts : ts t
    ts : t 
    t : '-' VAL at_ts
    at_ts : at_ts at_t
    at_ts : 
    at_t : '+' ID ':' VAL

Por alguma razão ainda não está funcional e não reconhece corretamente o dicionario.