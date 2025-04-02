#MÉTODOS DA CLASSE SET

# in

"""
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(1 in numeros)
print(10 in numeros)
"""

# len

"""
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(len(numeros))
"""

# {}.remove

"""
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros
numeros.remove(10)
print(numeros)
"""

# {}.pop

"""
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros
numeros.pop()
numeros.pop()
print(numeros)
"""

# {}.discard

"""
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros
numeros.discard(1)
numeros.discard(45)
print(numeros)
"""

# {}.copy

"""
sorteio = {1, 23}

sorteio
sorteio.copy()
sorteio
"""

# {}.clear

"""
sorteio = {1, 23}

sorteio
sorteio.clear()
sorteio
"""

# {}.add

"""
sorteio = {1, 23}

print(sorteio.add(25))
print(sorteio.add(42))
print(sorteio.add(25))
"""

# {}.isdisjoint

"""
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
"""

# {}.issuperset

"""
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
"""

# {}.issubset

"""
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
"""

"""
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))
"""

# {}.difference

"""
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
"""

# {}.intersection

"""
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
"""

# {}.union

"""
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funcão enumerate em um conjunto

"""
carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
"""

# Iterar conjuntos (set) usando loop FOR

"""
carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)
"""

# Acessando dados do set 

"""
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
"""

# Criando sets

"""
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)
"""