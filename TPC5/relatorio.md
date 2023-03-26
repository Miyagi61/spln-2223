### TPC4

## Ficheiros importantes
- tokenizadorSPLN/*

## Resumo

Em primeiro lugar continuei o tratamento do texto conforme
indicado na aula. Adicionei o ficheiro de abreviaturas *abrev.txt* na diretoria *conf*. 
Na expressão regex que identifica as abreviaturas são adicionadas as abreviaturas na língua escolhida pelo utilizador. O ficheiro de abreviaturas é facilmente alterável e extensível pelo utilizador comum.
Este tokenizador após ser instalado pode ser chamado com o comando *tok*. Neste comando existe a flag -l que permite escolher a língua das abreviaturas usadas. Todo o tratamento de comandos foi realizado com o módulo argparse.