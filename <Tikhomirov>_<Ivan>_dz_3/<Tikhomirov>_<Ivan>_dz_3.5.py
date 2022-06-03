
# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number):
    """
    Generating random jokes

    :param number: Number of jokes you wish to get :return: str
    """
    iterations = 0
    while iterations < number:
        rand_noun = choice(nouns)
        nouns.remove(rand_noun)
        rand_adverb = choice(adverbs)
        adverbs.remove(rand_adverb)
        rand_adjective = choice(adjectives)
        adjectives.remove(rand_adjective)
        print(f'{rand_noun} {rand_adverb} {rand_adjective}')
        iterations += 1

get_jokes(5)


