#TASK 1

import math
seconds = int(input('Введите промежуток времени в секундах: '))

minutes = seconds/60
hours = seconds/3600
days = seconds/86400

if seconds in range(0, 60):
    print(f'{seconds} сек')
elif seconds in range(60, 3600):
    print(f'{math.floor(minutes)} мин {seconds%60} сек')
elif seconds in range(3600, 86400):
    print(f'{math.floor(hours)} час {math.floor((hours-math.floor(hours))*60)} мин {seconds%60} сек')
elif seconds in range(86400, 604800):
    print(f'{math.floor(days)} дн {math.floor((days-math.floor(days))*24)} час {math.floor((hours-math.floor(hours))*60)} мин {seconds%60} сек')
else:
    print('стоп')