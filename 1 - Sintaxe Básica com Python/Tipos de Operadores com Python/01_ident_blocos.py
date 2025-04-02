def sacar(valor):
    saldo = 100
    if saldo > valor:
        print("Valor pode ser sacado.")
    elif saldo < valor:
        print("Saldo insuficiente.")
    elif saldo == valor:
        print("Saldo será zerado.")
sacar(100)

def depositar(valor1):
    saldo = 500
    saldo += valor1