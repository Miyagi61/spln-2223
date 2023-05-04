## TPC7

O objetivo neste tpc foi continuar o TPC anterior.

O que foi adicionado foi a agregação de todo o corpus num único ficheiro, além da criação de um script com a utilização da ferramente de linha de comandos *crontab*. Esta ferramenta permite escalonar execuções a certas horas. Neste caso fiz com que o script fosse executado todos os dias às 10:00 com a linha "00 10 * * * <path para o script>.

Além disso com o criador de modelos desenvolvida na aula foi integrado no script de forma a tentar criar um modelo cada vez mais aceitável. 

Para testar o modelo utilizei os testes realizados na aula e para já alguns resultados parecem promissores contudo ainda existe um longo caminho a percorrer até serem aceitáveis.

Exemplo de teste de similaridades e respetivos scores:

- portugal : crime -> 0.7678891
- portugal : frança -> 0.8889487
- política : lixo -> 0.77003086
- política : comida -> 0.772603
- campeão : medalha -> 0.9146067
- campeão : doença -> 0.94590604
- dados : informação -> 0.7226403
- dados : creme -> 0.4421657


