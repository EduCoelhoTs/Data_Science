print(
    "Exercicio 1 - imprima na tela os números de 1 a 10; Use uma lista para armazernar os números;"
)


def printNumber(list):
    for number in list:
        print(number)


printNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("")
print("Exercicio 2 - Crie uma lista de 5 objetos e imprima na tela;")


def printList(list):
    for item in list:
        print(item)


printList([10, "Item2", 15.5, "Item4", 20])

print("")
print("Exercicio 3 - Crie duas strings e concatene as duas em uma terceira string;")


def concatString(string1, string2):
    print(string1 + string2)


concatString("String1 ", "String 2")

print("")
print("Exercicio 4")


def createTuple(values, valueToCount):
    print(values.count(valueToCount))


createTuple((1, 2, 3, 4, 4, 4, 5), 4)

print("")
print("Exercicio 5")


def createDictionary():
    print({})


createDictionary()

print("")
print("Exercicio 6")


def createNewDictionary():
    print(
        {
            "name": "Eduardo",
            "age": 25,
            "city": "Fortaleza",
        }
    )


createNewDictionary()

print("")
print("Exercicio 7")


def createElementsList():
    list = [
        "firstElement",
        ("test", 10),
        {
            "name": "Eduardo",
            "age": 25,
        },
        10,
    ]
    print(list)


createElementsList()

print("")
print("Exercicio 8")


def createFruitList(fruitList, fruitToGet):
    for fruit in fruitList:
        if fruit == fruitToGet:
            print(fruitToGet + " existe na lista")


createFruitList(["banana", "maça", "uva", "pera"], "pera")


print("")
print("Exercicio 9")


def multElements(element_list):
    resp = list(map(lambda x: x * 2, element_list))
    print(resp)


multElements((1, 2, 3, 4))

print("")
print("Exercicio 10")


def printTemperature(temperature):
    const_temperature = 40
    while const_temperature > temperature:
        print("Temperatura: " + str(const_temperature))
        const_temperature -= 1


printTemperature(35)


# Exercicios - Eduardo Coelho Silva - 11/02/2023
