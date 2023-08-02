# ProjetoAnaliseDadosExportacaoImportacaoNacional
Este projeto foi requisitado para um processo seletivo. Nele, o meu objetivo consistia em ler dois arquivos csv e realizar alguns tratamentos. De forma geral, era necessário ler os arquivos, separar os dados por estados e meses e, então, criar um novo arquivo para cada estado. Além disso, foi necessário utilizar VBA para a criação de Macros.

Instruções:
Para que o código funcione, é necessário realizar o download de dois arquivos, ambos que estão disponíveis de forma pública. Ambos estão disponíveis no site: https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
Após acessar o site, é necessário realizar o download do arquivo de importação e de exportação do ano exatamente anterior (a razão disso se deve pelo fato que o arquivo do ano atual ainda está sendo atualizado). Ou seja, na data atual (02/08/2023), eu precisaria realizar o download de ambos os arquivos importação e exportação do ano de 2022. Os links, caso prefira, estão aqui:
https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_2022.csv
https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2022.csv

Assim, ao realizar o download, o único tratamento necessário é adicionar ambos os arquivos no mesmo diretório do arquivo script e criar uma pasta chamada resultado. Entretanto, caso prefira, você pode atualizar o path nas três primeiras variáveis do programa. Os únicos pacotes que são utilizados são o csv e o os, que, normalmente, já vêm instalados por padrão.

Explicação do script:
Olá, bem, para começar, eu escrevi o arquivo em python, pela facilidade da linguagem em trabalhar com listas, alocações de posições, laços for etc.
No desafio, eu utilizei diversas lists comprehensions, com alguns filters e condicionais em lambda.
De começo, para definir como o programa deve começar a procura, eu defini a lista dos estados, onde, através de um laço for, o iterável CSV terá uma seleção à partir da coluna específica para procurar por todos os dados que estejam correspondendo ao estado atual.
Assim, com esta seleção em mãos, eu crio um set, para que ele pegue todos os IDS únicos e facilite, posteriormente, o tratamento dos dados, pois eu poderia obter, com estes ids, uma lista de listas, nas quais estas últimas conteriam todas as transações que foram realizadas sob tal id.
Com isso em mente, bastaria que eu separasse os dados por mês e, assim, escrever uma nova linha. 
Ou seja, para cada dado no set de ID's, haverá uma nova linha, onde o programa irá procurar nas variáveis delimitadas para o estado atual os dados que sejam correspondente à cada interação.

IMPORTANTE
Para alterar o caminho de cada programa, estão declaradas variáveis, em cada arquivo (macro e script) para que se consiga alterar o caminho, bastando apenas colar o diretório desejado.
