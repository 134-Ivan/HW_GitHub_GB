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

for item in catalog:
    if isinstance(item, str):
        catalog[catalog.index(item)] = item
    elif isinstance(item, list) == True:
        j = catalog.index(item)
        for i in item:
            catalog.insert(j, i)
        catalog.pop(j+3)

print(' '.join(catalog))
