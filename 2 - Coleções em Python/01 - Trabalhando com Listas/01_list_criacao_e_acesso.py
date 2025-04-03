# Comprensão de listas em Python

"""
# filtro v1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# filtro v2

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
"""

# Função enumerate em Python para iterar sobre listas

"""
carros = ["mercedes", "BMW", "chevrolet"]

for indice, carro in enumerate(carros):
    print(f"Índice: {indice} - Carro: {carro}")
"""

# Iterar sobre listas em Python usando o laço FOR

"""
carros = ["gol", "palio", "celta", "uno"]

for carro in carros:
    print(carro)
"""

# Fatiamento de listas em Python

"""
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]
"""

# Listas aninhadas em Python

"""
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5 , "c"]
]

matriz[0]
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]
"""

# Exemplo de criação de listas em Python

"""
frutas = ["maçã", "banana", "laranja", "melancia", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, "São Paulo", True]
"""