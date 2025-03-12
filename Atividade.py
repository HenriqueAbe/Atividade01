import random

numeros = []

while True:
    try:
        inteiro = int(input("Digite um número de 0 a 20: "))
        if inteiro > 20 or inteiro < 0:
            print("Número inválido.")
        else:
            break
    except ValueError:
        print("Digite um número.")
    

while inteiro > 0:
    numerosAleatorios = random.randint(1, 100)

    if numerosAleatorios not in numeros:
        numeros.append(numerosAleatorios)
        inteiro -= 1

print("----------resultados----------")

for numeros in numeros:
    if numeros % 3 == 0:
        print(numeros, " - número múltiplo de 3.")
    elif numeros % 2 == 0:
        print(numeros, " - número par.")
    else:
        print(numeros," - Número ímpar.")