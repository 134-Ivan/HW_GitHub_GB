# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import json
import requests
import datetime

def currency_rates(currency):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    dict_json = json.loads(response.text)
    currency = currency.upper() if currency.lower() else currency
    currency_date = datetime.datetime.utcnow()
    currency_rate = dict_json['Valute'][currency]['Value']
    return f'Курс {currency} на {currency_date.date()} равено {currency_rate}'

if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('USD'))
    print(currency_rates('eur'))
    print(type(currency_rates('eur')))
