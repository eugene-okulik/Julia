import datetime

date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(date, '%b  %d, %Y -  %X')
print(python_date.month)
print(python_date.strftime('%d.%m.%Y, %H:%M '))
