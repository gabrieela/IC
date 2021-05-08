# Testes - IntuitiveCare

- Da proposta apresentada, foram escolhidos o teste 01 e o teste 03, e ambos foram implementados usando a linguagem Python, e portanto a instalação do Python é um pré-requisito para execução deste projeto.

## Teste 01

```bash

# Clone o repositório
$ git clone https://github.com/gabrieela/IC.git

# Acesse a pasta do projeto no terminal/cmd
$ cd IC

# Instale as seguintes biblitecas da linguagem Python
$ pip3 install bs4
$ pip3 install pandas
$ pip3 install urllib

# Execute o arquivo, rodando o comando abaixo
$ python3 teste01.py

O comportamento esperado é o download do pdf em questão, e a exibição de uma mensagem informando sucesso no donwload.

```

## Teste 03

```bash


# Instale as seguintes biblitecas da linguagem Python
$ pip3 install sqlite3
$ pip3 install sqlalchemy

# Execute o arquivo, rodando o comando abaixo
$ python3 teste03.py

O comportamento esperado é a criação de um banco de dados no diretório local, inserção dos dados contidos nos arquivos csv, a execução de uma query de consulta relativa ao último trimestre cadastrado e outra relativa ao último ano cadastrado, por último devem ser exibidos os resultados correspondentes a essas seleções.

```