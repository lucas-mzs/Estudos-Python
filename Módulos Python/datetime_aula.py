from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inico = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 09:20:20', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(data_fim, data_inico)
print(delta.days, delta.years)