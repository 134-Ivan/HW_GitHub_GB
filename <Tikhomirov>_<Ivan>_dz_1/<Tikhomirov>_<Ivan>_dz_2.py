import math

numbers = [number**3 for number in range(1, 1000)]

def get_sum_list7(numbers_list):
    new_list = []
    for number in numbers_list:
        if sum(list(map(int, str(number))))%7 == 0:
            new_list.append(number)
    print(sum(new_list))

def get_sum_list17(numbers_list):
    new_list = []
    for number in numbers_list:
        if sum(list(map(int, str(number+17))))% 7 == 0:
            new_list.append(number)
    print(sum(new_list))

get_sum_list7(numbers)
get_sum_list17(numbers)

