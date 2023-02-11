import pandas as pd
import numpy as np

data = {"col1": [1, 2, 3, 4], "col2": [5, 6, 7, 8], "col3": ["A", "B", "C", "D"]}

df = pd.DataFrame(data)

# adicionar novas colunas:

df["col4"] = [10, 20, 30, 40]
print(df)

# excluir colunas:
df = df.drop(["col4"], axis=1)
print(df)

# renomear colunas
df = df.rename(columns={"col1": "coluna1", "col2": "coluna2", "col3": "coluna3"})
print(df)
