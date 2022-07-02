

def add_sale(sale_amount=None):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        if sale_amount:
            f.write(f'{sale_amount}\n')

if __name__ == '__main__':
    add_sale(200)
    add_sale(300)
    add_sale(400)