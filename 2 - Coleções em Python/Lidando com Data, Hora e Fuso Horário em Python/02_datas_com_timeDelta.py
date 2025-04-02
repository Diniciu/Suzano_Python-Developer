from datetime import datetime, timedelta

tipo_carro = str(input("Qual o tipo do carro? ")) # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno) 
    print(f"Pronto às {data_estimada}.")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_medio) 
    print(f"Pronto às {data_estimada}.")
else: 
    data_estimada = data_atual + timedelta(minutes = tempo_grande) 
    print(f"Pronto às {data_estimada}.")


resultado = datetime(2025, 2, 25, 16, 1, 48) - timedelta(hours = 1)
print(resultado.time())