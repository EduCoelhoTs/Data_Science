# imports
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib as mpl
import seaborn as sns

# lendo arquivo csv:
df = pd.read_csv("ds_salaries.csv")

print(df)

# listando linhas do dataFrame => head(): 5 primeiras -- tail(): 5 ultimas
# info() => retorna informações especificas sobre o datafram (numero de linhas e colunas, tipos de dados, quantidades de valores nulos e ecs)
# describe() => retorna informações estatisticas sobre o dataframe (media, mediana, desvio padrao, minimo, maximo, quartis e etc)
# value_counts() => retorna a quantidade de valores unicos de uma coluna
# sort_values() => ordena o dataframe por uma coluna especifica
# isnull() => retorna um dataframe booleano com True para valores nulos e False para valores nao nulos
# notnull() => retorna um dataframe booleano com True para valores nao nulos e False para valores nulos
# dropna() => remove linhas com valores nulos
# fillna() => preenche valores nulos com um valor especifico
# unique() => retorna uma lista com os valores unicos de uma coluna
# nunique() => retorna a quantidade de valores unicos de uma coluna
# corr() => retorna uma matriz de correlação entre as colunas numericas do dataframe
# pivot_table() => cria uma tabela dinamica a partir de um dataframe
# groupby() => agrupa linhas de um dataframe com base em uma coluna especifica
# merge() => combina dataframes
# join() => combina dataframes
# concat() => combina dataframes
# apply() => aplica uma funcao a cada linha ou coluna de um dataframe
# sample() => retorna uma amostra aleatoria de um dataframe
# to_csv() => salva um dataframe em um arquivo csv
# to_excel() => salva um dataframe em um arquivo excel
# to_sql() => salva um dataframe em um banco de dados sql
# to_json() => salva um dataframe em um arquivo json
# to_html() => salva um dataframe em um arquivo html
# to_clipboard() => copia um dataframe para a area de transferencia
# to_string() => retorna uma string representando o dataframe
# to_latex() => retorna uma string representando o dataframe em formato latex
# to_dict() => retorna um dicionario representando o dataframe
# to_numpy() => retorna um array numpy representando o dataframe
# to_records() => retorna um array numpy representando o dataframe
print("Head")
head = df.head(10)
print(head)

print("")

print("tail")
tail = df.tail(10)
print(tail)

print("")

print("Tail")
print(df.info())

print("")

print("describe")
print(df.describe())

print("")
print("pegando valores por nome da coluna")
print(df["job_title"].value_counts())

print("")
print("calculando a mediana das colunas numericas")
print(df.median())

print("")
print("calculando o valor minimo das colunas")
print(df.min())

print("")
print("calculando o valor maximo das colunas")
print(df.max())

print("")
print("calculando a soma das colunas")
print(df.sum())
