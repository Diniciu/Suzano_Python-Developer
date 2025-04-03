# [].sort() - Ordena a lista

"""
linguagens = ['Python', 'Java', 'C#', 'C++']
linguagens.sort()

linguagens = ['Python', 'Java', 'C#', 'C++']
linguagens.sort(reverse=True)

linguagens = ['Python', 'Java', 'C#', 'C++']
linguagens.sort(key = lambda x: len(x))

linguagens = ['Python', 'Java', 'C#', 'C++']
linguagens.sort(key = lambda x: len(x), reverse = True)
"""

# [].reverse() - Inverte a ordem dos elementos da lista

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

linguagens.reverse()

print(linguagens)
"""

# [].remove() - Remove o primeiro item com o valor especificado

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

linguagens.remove('C++')

print(linguagens)
"""

# [].pop() - Remove o elemento no índice especificado

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)
"""

# [].index() - Retorna o índice do primeiro elemento com o valor especificado

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

linguagens.index('Python')
linguagens.index('Java')
"""

# [].extend() - Adiciona os elementos de uma lista (ou qualquer iterável) ao final da lista

"""
linguagens = ['Python', 'Java', 'C#', 'C++']

print(linguagens)

linguagens.extend(['JavaScript', 'PHP', 'Ruby'])

print(linguagens)
"""

# [].count() - Retorna o número de vezes que um valor específico aparece na lista

"""
cores = ['verde', 'amarelo', 'azul', 'vermelho', 'verde', 'verde']

cores.count("vermelho")
cores.count("azul")
cores.count("verde")
"""

# [].copy() - Retorna uma cópia da lista

"""
lista = [1, 'Python', [40, 30, 20]]

lista.copy()

print(lista)
"""

# [].clear() - Remove todos os itens da lista

"""
lista = [1, 'Python', [40, 30, 20]]

print(lista)

lista.clear()

print(lista)
"""

# [].append() - Adiciona um item ao final da lista

"""
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
"""