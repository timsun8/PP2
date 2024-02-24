# 1
import datetime

current = datetime.date.today()

new = current - datetime.timedelta(days=5)

print(current)
print(new)
# 2
import datetime

today_date = datetime.date.today()

yesterday_date = today_date - datetime.timedelta(days=1)

tomorrow_date = today_date + datetime.timedelta(days=1)

print("yesterday: ", yesterday_date)
print("today: ", today_date)
print("tomorrow: ", tomorrow_date)
# 3
import datetime

date = datetime.datetime.now()

date = date.replace(microsecond=0)

print(date)
# 4
from datetime import datetime

def difference_in_sec(date1, date2):
    d = date2 - date1
    return d.total_seconds()

date1_str = input("Введите первую дату в формате (гггг-мм-дд чч:мм:сс): ")
date2_str = input("Введите вторую дату в формате (гггг-мм-дд чч:мм:сс): ")

date1 = datetime.strptime(date1_str, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

difference = difference_in_sec(date1, date2)

print(difference)