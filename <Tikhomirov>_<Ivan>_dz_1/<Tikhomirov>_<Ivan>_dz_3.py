#TASK 3

numbers = [number for number in range(1, 100)]
print(numbers)

for number in numbers:
    if number == 1:
        print(f'{number} процент')
    elif number in range(2, 5):
        print(f'{number} процента')
    elif number in range(5, 21):
        print(f'{number} процентов')
    elif number in range(22, 25):
        print(f'{number} процента')
    elif number in range(32, 35):
        print(f'{number} процента')
    elif number in range(42, 45):
        print(f'{number} процента')
    elif number in range(52, 55):
        print(f'{number} процента')
    elif number in range(62, 65):
        print(f'{number} процента')
    elif number in range(72, 75):
        print(f'{number} процента')
    elif number in range(82, 85):
        print(f'{number} процента')
    elif number in range(92, 95):
        print(f'{number} процента')
    elif (str(number))[-1] == '1':
        print(f'{number} процент')
    else:
        print(f'{number} процентов')
