#MÉTODOS DA CLASSE TUPLE

# [].len() - Retorna quantos elementos possui a tupla (tamanho dela)

# [].index() - Retorna o índice do primeiro elemento com o valor especificado dentro da tupla

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

linguagens.index('Python')
linguagens.index('Java')
"""

# [].count() - Retorna o número de vezes que um valor específico aparece na tupla

"""
cores = ['verde', 'amarelo', 'azul', 'vermelho', 'verde', 'verde']

cores.count("vermelho")
cores.count("azul")
cores.count("verde")
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Função enumerate em Python para iterar sobre tuplas

"""
carros = ["mercedes", "BMW", "chevrolet"]

for indice, carro in enumerate(carros):
    print(f"Índice: {indice} - Carro: {carro}")
"""

# Iterar sobre tuplas em Python usando o laço FOR

"""
carros = ["gol", "palio", "celta", "uno"]

for carro in carros:
    print(carro)
"""

# Fatiamento de tuplas

"""
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]
"""


# Tuplas aninhadas

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

# Índices negativos

"""
frutas = ["maça", "laranja", "uva", "pera"]

frutas[-1]
frutas[-3]
"""

# Acesso direto as tuplas 

"""
frutas = ["maça", "laranja", "uva", "pera"]

frutas[0]
frutas[1]
"""

# Conhecendo tuplas

"""
frutas = ["laranja", "pera", "uva"]

letras = tuple("Python")

numeros = tuple[1, 2, 3, 4, 5]

pais = ("Brasil",)
"""