# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

english_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate(number):
    print(english_dict.get(number))

num_translate('one')
num_translate('six')
num_translate('eight')
num_translate('eleven')
num_translate('thirty')
num_translate('two')

# def num_translate(str):
#     if str in english_dict:
#         print(english_dict[str])
#     else:
#         print('None')