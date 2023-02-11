# iniciando com o pandas

import pandas as pd
import numpy as np

# Criando uma lista de dados:

data = [
    ["John", 32, "Male"],
    ["Jane", 22, "Female"],
    ["Jim", 25, "Male"],
]

# criando dataframe a partir da lista
df = pd.DataFrame(data, columns=["Name", "Age", "Gender"])

# exibindo dataframe

print(df)

# Criando dataFrame de outra forma:

new_data = {
    "Name": ["John", "Jane", "Jim"],
    "Age": [32, 22, 25],
    "Gender": ["Male", "Female", "Male"],
}

new_df = pd.DataFrame(new_data)

print(new_df)

# Criando dataframe a partir de um dicionario:

new_data = pd.DataFrame(
    {"col1": [1, 2, 3, 4], "col2": [5, 6, 7, 8], "col3": ["A", "B", "C", "D"]}
)

row2_loc = new_data.loc[1]
print("Acessando a segunda linha com loc:")
print(row2_loc)
# vai printar coluna 2:
# saida:
# col1  2
# col2  6
# col3  B
# Nome: 1, dtype: object
print("")
row2_iloc = new_data.iloc[1]
print("Acessando a segunda linha com iloc:")
print(row2_iloc)
# saida
# col1    2
# col2    6
# col3    B
# Name: 1, dtype: object

print("")
# exibindo so algumas colunas;
cols = new_data[["col1", "col3"]]
print("colunas 1 e 3")
print(cols)
# exibindo so algumas linhas;
print("")
print("linhas 0")
rows = new_data.loc[0]
print(rows)
