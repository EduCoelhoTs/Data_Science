# spread dict
teste = {
    "nome": "teste",
    "idade": 10,
}

teste = {**teste, "teste": 10}

print(teste)

# spread array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array = [*array, 11, 12]
print(array)

# Tuplas => listas imutaveis:

tupla = ("user", "password", "host", "port", "database")
print(tupla)

tupla.count(4)
