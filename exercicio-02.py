import pandas as pd
import numpy as np

df = pd.read_csv("./ds_salaries.csv")

print("Exercicio 11 - Ler os 10,20,50 primeiros registros")

print(df.head(10))
print(df.head(20))
print(df.head(50))

print("Exercico 12 - Ler os 10,20,50 ultimos registros")

print(df.tail(10))
print(df.tail(20))
print(df.tail(50))

print("Exercico 13")

group = df.groupby(["company_location", "company_size"])["salary_in_usd"].mean()
print(group)

print("Exercico 14")

pivot = df.pivot_table(
    index="job_title", columns="work_year", values="salary_in_usd", aggfunc="mean"
)
print(pivot)
