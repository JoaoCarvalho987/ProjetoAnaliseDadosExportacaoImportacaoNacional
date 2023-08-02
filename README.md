# ProjetoAnaliseDadosExportacaoImportacaoNacional
Este projeto foi requisitado para um processo seletivo. Nele, o meu objetivo consistia em ler dois arquivos csv e realizar alguns tratamentos. De forma geral, era necessário ler os arquivos, separar os dados por estados e meses e, então, criar um novo arquivo para cada estado. Além disso, foi necessário utilizar VBA para a criação de Macros.

Explicação do script:
Olá, bem, para começar, eu escrevi o arquivo em python, pela facilidade da linguagem em trabalhar com listas, alocações de posições, laços for etc.
No desafio, eu utilizei diversas lists comprehensions, com alguns filters e condicionais em lambda.
De começo, para definir como o programa deve começar a procura, eu defini a lista dos estados, onde, através de um laço for, o iterável CSV terá uma seleção à partir da coluna específica para procurar por todos os dados que estejam correspondendo ao estado atual.
Assim, com esta seleção em mãos, eu crio um set, para que ele pegue todos os IDS únicos e facilite, posteriormente, o tratamento dos dados, pois eu poderia obter, com estes ids, uma lista de listas, nas quais estas últimas conteriam todas as transações que foram realizadas sob tal id.
Com isso em mente, bastaria que eu separasse os dados por mês e, assim, escrever uma nova linha. 
Ou seja, para cada dado no set de ID's, haverá uma nova linha, onde o programa irá procurar nas variáveis delimitadas para o estado atual os dados que sejam correspondente à cada interação.

IMPORTANTE
Para alterar o caminho de cada programa, estão declaradas variáveis, em cada arquivo (macro e script) para que se consiga alterar o caminho, bastando apenas colar o diretório desejado.
