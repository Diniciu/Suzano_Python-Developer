# Condincional ternária

"""
saldo = 2500
saque = 2000

status = "Sucesso" if saldo >= saque else "Falha"
print(f"Status: {status}.")
"""

# Condicional aninhada

"""
conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque efetuado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque efetuado com cheque especial.")
    else:
        print("Não foi possível efetuar o saque, saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque efetuado com sucesso.")
    else:
        print("Saldo insuficiente.")
else:
    print("Operação inválida.")
"""

#Condicional unária

"""
maior_idade = 18
idade_especial = 16
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH.")
elif idade == 16:
    print("Pode fazer as aulas teóricas.")
else:
    print("Não pode tirar a CNH.")
"""