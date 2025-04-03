from datetime import datetime

data_hora_atual = datetime.now()
data_hora_string = "2025-02-26 09:10"
mascara_pt_br = "%d/%m/%Y %a"
mascara_en_us = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_pt_br))

print(datetime.strptime(data_hora_string, mascara_en_us))