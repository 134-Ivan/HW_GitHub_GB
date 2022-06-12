

def show_sales(start=None, stop=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        total_sales = [0]
        for line in f:
            total_sales.append(line.strip())
        if start is None and stop is None:
            for sale in total_sales[1:]:
                print(sale)
        elif start is not None and stop is None:
            for sale in total_sales[start:]:
                print(sale)
        elif start is not None and stop is not None:
            for sale in total_sales[start:stop+1]:
                print(sale)

if __name__ == '__main__':
    show_sales()
    print("*"*50)
    show_sales(3)
    print("*"*50)
    show_sales(3, 5)
