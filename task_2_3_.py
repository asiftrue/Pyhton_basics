weather = ['В', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('Список = ', weather)
print('ID списка: ', id(weather), '\n')

for idx, weather[idx] in enumerate(weather):
    if weather[idx].isdigit():
        item_n = int(weather[idx])
        item_n_f = str(f'"{item_n:02d}"')
        weather[idx] = item_n_f
    elif weather[idx][0] == '+' and weather[idx][1].isdigit():
        item_m = int(weather[idx])
        item_m_f = str(f'"+{item_m:02d}"')
        weather[idx] = item_m_f
    elif weather[idx][0] == '-' and weather[idx][1].isdigit():
        item_a = int(weather[idx][1])
        item_a_f = str(f'"-{item_a:02d}"')
        weather[idx] = item_a_f
print('Список = ', weather)
print('ID списка: ', id(weather), '\n')
print(" ".join(weather))
