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
