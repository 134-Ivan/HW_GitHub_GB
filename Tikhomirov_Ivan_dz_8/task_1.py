# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(email_address):
    RE_DOMAIN = re.compile('[\w.-]+\.[\w]{2,4}', re.IGNORECASE)
    RE_USERNAME = re.compile(r'[а-яёa-zA_Z0-9_.+-]+', re.IGNORECASE)
    email_dict = {'username': None, 'domain': None}
    try:
        if RE_DOMAIN and RE_USERNAME:
            email_dict['domain'] = RE_DOMAIN.findall(email_address)[0]
            email_dict['username'] = RE_USERNAME.findall(email_address)[0]
            print(email_dict)
        else:
            raise ValueError
    except ValueError:
        print('oops')


email_parse('жлmeone@geekbrains.ru')
email_parse('123@com.ru')
email_parse('AnAnsnd324@dialoGG.ru')
email_parse('gogi_3+@2SS3.ru')
#
# email_parse('жлmeone@geekbrainsru')
