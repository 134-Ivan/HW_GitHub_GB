# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
#

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    ip_list = []
    for line in f:
        ip = line.split()[0]
        ip_list.append(ip)
    # print(ip_list)
    _ = set(ip_list)
    unique_ip = []
    for item in _:
        unique_ip.append(item)
    # print(unique_ip)
    dict = {}
    for user in unique_ip:
        dict[user] = ip_list.count(user)
    spammer = max(zip(dict.values(), dict.keys()))
    print(f'Спаммером является клиект с IP: {spammer[1]}. Количество попыток входа составляет: {spammer[0]}')
