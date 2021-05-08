import pandas as pd
import sqlite3
from sqlalchemy import create_engine

database = create_engine('sqlite:///database.db')
chunk_size = 50000
batch_no = 1

file_encoding = 'cp1252'

fileNames = ["1T2019.csv", "2T2019.csv", "3T2019.csv", "4T2019.csv", "1T2020.csv", "2T2020.csv", "3T2020.csv", "4T2020.csv"]

for file in fileNames:
    dataset = pd.read_csv(file, sep = ";", chunksize = chunk_size, iterator = True,  encoding=file_encoding)
    print(f'Inserindo dados, provenientes do arquivo {file}, no banco database na tabela dados')

    for chunck in dataset:
        chunck.to_sql('dados', database, if_exists = 'append')
        batch_no += 1
        print('index: {}'.format(batch_no))

input_fd = open("Relatorio_cadop.csv", encoding=file_encoding, errors = 'backslashreplace')
dataset_cadop = pd.read_csv(input_fd, sep = ";", chunksize = chunk_size, skiprows=[0])
print('Inserindo dados, provenientes do arquivo Relatorio_cadop.csv, no banco database na tabela dados')
for chunck in dataset_cadop:
    chunck.to_sql('relatorio_cadop', database, if_exists = 'append')
    batch_no += 1
    print('index: {}'.format(batch_no))


print("--------------------------------------------------")
print("Seleção das operadoras que atendem a condição (último trimestre)")
resultTrimestre = pd.read_sql_query("SELECT relatorio_cadop.`Razão Social` FROM relatorio_cadop JOIN dados ON ( relatorio_cadop.`Registro ANS` = dados.REG_ANS) WHERE dados.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' AND dados.DATA >= '01/10/2020' ORDER BY dados.VL_SALDO_FINAL LIMIT 10", database)
print(resultTrimestre)

print("--------------------------------------------------")
print("Seleção das operadoras que atendem a condição (último ano)")
ResultAno = pd.read_sql_query("SELECT relatorio_cadop.`Razão Social` FROM relatorio_cadop JOIN dados ON ( relatorio_cadop.`Registro ANS` = dados.REG_ANS) WHERE dados.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' AND dados.DATA BETWEEN '01/01/2020' AND '01/10/2020' ORDER BY dados.VL_SALDO_FINAL LIMIT 10", database)
print(ResultAno)