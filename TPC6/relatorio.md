## TPC6

O objetivo neste tpc era reunir através da página de um jornal à escolha (neste caso Jornal Expresso) um corpus que vá crescendo conforme os dias vão passando.

Esta implementação cria uma pasta *corpus* dentro da qual são criadas pastas relativas a cada dia com nome no formato "AAAA_MM_DD", dentro de cada uma desta pasta são guardadas informações sobre os artigos, mais concretamente, o título, o *url*, os autores e o texto relativo à notícia. Conforme o programa vai fazendo o *parse* às notícias é armazenado num dicionário dividido por dias. No final da execução em cada pasta é criado um ficheiro *.corpus.txt* no qual o corpus daquele dia é armazenado (no caso de já existir este ficheiro este é aberto em modo *append*)