# TASK 2

catalog = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

for item in catalog:
    if is_digit(item):
        if len(item) == 1:
            catalog[catalog.index(item)] = ['"', f'0{item[-1]}', '"']
        elif "+" in item:
            catalog[catalog.index(item)] = ['"', f'+0{item[-1]}', '"']
        else:
            catalog[catalog.index(item)] = ['"', item, '"']

new_list = []

for item in catalog:
    if isinstance(item, str):
        new_list.append(item)
    elif isinstance(item, list) == True:
        for i in item:
            new_list.append(i)

print(' '.join(new_list))
