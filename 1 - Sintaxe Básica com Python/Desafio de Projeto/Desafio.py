menu = """
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR
=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato.append(f"Depósito: R${valor:.2f}")

def sacar(valor):
    global saldo, extrato, numero_saques
    saldo -= valor
    extrato.append(f"Saque: R${valor:.2f}")
    numero_saques += 1

def mostrar_extrato():
    print("\n===============EXTRATO===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R${saldo:.2f}")
    print("======================================")

while True:
    opcao = input(menu)
    
    if opcao == '1':
        valor = float(input("Digite o valor do depósito: R$"))
        if valor > 0:
            depositar(valor)
        else:
            print("Valor inválido! Tente novamente.")
    
    elif opcao == '2':
        valor = float(input("Digite o valor do saque: R$"))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print("Valor do saque excede o limite!")
        elif numero_saques >= limite_saques:
            print("Limite de saques excedido!")
        elif valor > 0:
            sacar(valor)
        else:
            print("Valor inválido! Tente novamente.")
    
    elif opcao == '3':
        mostrar_extrato()
    
    elif opcao == '0':
        print("Fim do programa.")
        break
    
    else:
        print("Opção inválida! Tente novamente.")