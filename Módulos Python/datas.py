# Criando datas com módulos datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# datetime.fromtimestamp(Unix Timestamp)
# Para timezones
# https://en.wikipedia.org/wiki/List_of_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data_lugares = datetime.now(timezone('Asia/Tokyo'))
# print(data_lugares)

data_str_data1 = '2025-09-15 14:40:25'
data_str_fmt1 = '%Y-%m-%d %H:%M:%S'
data_str_data2 = '15-09-2025'
data_str_fmt2 = '%d-%m-%Y'

data = datetime(2025, 9, 15, 14, 33)

data1 = datetime.strptime(data_str_data1, data_str_fmt1)
data2 = datetime.strptime(data_str_data2, data_str_fmt2)
# print(data1)
# print(data2)

data_agora = datetime.now()
# print(data_agora)

criar_data = datetime.now()
# print(criar_data.timestamp())