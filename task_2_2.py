weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

message = ''
for item in weather:
    if item.isdigit():
        item_n = int(item)
        message += '"'
        message += f'{item_n:02d}'
        message += '" '
    elif item[0] == '+' or item[0] == '-' and item[1].isdigit():
        item_n = int(item)
        message += '"'
        message += item[0]
        message += f'{item_n:02d}'
        message += '" '
    else:
        message += item
        message += ' '
print(message)
