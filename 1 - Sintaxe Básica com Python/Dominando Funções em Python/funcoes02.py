#-Parâmetros especiais-#

# Objetos de primeira classe

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado da operação = {resultado}.")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)







































# Keyword and positional only

"""
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") #Válido
criar_carro(modelo = "Palio", ano = 1999, placa = "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") #Inválido
"""

# Keyword only

"""
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo = "Palio", ano = 1999, placa = "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") #Válido    
criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor = "1.0", combustivel = "Gasolina") #Inválido
"""

# Positional only

"""
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca = "Fiat", motor = 1.0, combustivel = "Gasolina") #Válido
criar_carro(modelo ="Palio", ano = 1999, placa = "ABC-1234", marca = "Fiat", motor = 1.0, combustivel = "Gasolina") #Inválido
"""