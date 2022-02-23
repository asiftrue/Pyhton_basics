employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for item in employees:
    div = item.split()
    print(f'Привет, {str(div[-1].title())}!')
