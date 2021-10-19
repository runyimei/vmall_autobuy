from datetime import datetime, timedelta

now = datetime.now()
buy_time_Str = '2021-10-19 10:08:00'
buy_time = datetime.strptime(buy_time_Str, "%Y-%m-%d %H:%M:%S")
begin_time = buy_time - timedelta(minutes=2)
print('ok')
dl = begin_time - now
sen = dl.seconds
print('ok')