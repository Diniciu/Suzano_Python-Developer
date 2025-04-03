from datetime import date, datetime, time, timedelta

# Criando data e hora

data = datetime.datetime(2025, 2, 25, 15, 29, 26)
print(data)

# Adicionando uma semana 

data = data + datetime.timedelta(weeks = 1)
print(data)

"""
data = date(2025, 2, 25)
print(data)

print(date.today())

data_hora = datetime(2025, 2, 25)
print(data_hora.today())

hora = (10, 20, 0)
print(hora)
"""