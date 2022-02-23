prices = [57.8, 62, 8, 26.5, 634.32, 5, 101, 83.1, 0.36, 1.88, 412.4]  # 11 элементов
prices_00 = []
for item in prices:
    item = ('%.2f' % item)
    prices_00.append(item)

str_prices = [str(x) for x in prices_00]
split_prices = []
for item in str_prices:
    r_kk = item.split('.')
    split_prices.append(r_kk)

prices_format = []
for item in split_prices:
    item[0] = int(item[0])
    item[1] = int(item[1])
    price = f"{item[0]:02d} руб {item[1]:02d} коп, "
    print(price, end=' ')
print('\n', 'ID списка: ', id(split_prices), '\n')

split_prices.sort()
for item in split_prices:
    price = f"{item[0]:02d} руб {item[1]:02d} коп, "
    print(price, end=' ')
print('\n', 'ID списка после сортировки по возрастанию: ', id(split_prices), '\n')

print('Сортировка по возрастанию: ')
split_prices_s = sorted(split_prices, reverse=True)
for item in split_prices_s:
    price = f"{item[0]:02d} руб {item[1]:02d} коп, "
    print(price, end=' ')

print('\n', '\n', 'Пять самых дорогих товаров по возрастанию: ')
split_prices_s.sort()
top_5 = split_prices_s[5:]
for item in top_5:
    price1 = f"{item[0]:02d} руб {item[1]:02d} коп, "
    print(price1, end=' ')
