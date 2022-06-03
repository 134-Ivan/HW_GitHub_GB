# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
# предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def tesaurus_adv(*args):
    employers_dictionary = {}
    for element in args:
        first_name = element.split()[0]
        second_name = element.split()[1]
        employers_dictionary.setdefault(second_name[0], {}).setdefault(first_name[0], []).append(element)
        # employers_dictionary_adv[second_name[0]] = {first_name[0]: [first_name]}
    print(employers_dictionary)

tesaurus_adv('Ivan Tikhomirov', 'Alex Pikul', 'Danila Afanasev', 'Dmitriy Lugovtsov', 'Irina Torotko')


# reserve
# def tesaurus_adv(*names):
#     employers_dictionary_adv = {}
#     for name in names:
#         employers_dictionary_adv[name.split()[1][0]] = {name[0]: name}
#     print(employers_dictionary_adv)