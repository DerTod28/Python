months_input = int(input("Введите месяц в виде целого числа от 1 до 12: "))
months = {1: 'Январь',
          2: 'Февраль',
          3: 'Март',
          4: 'Апрель',
          5: 'Май',
          6: 'Июнь',
          7: 'Июль',
          8: 'Август',
          9: 'Сентябрь',
          10: 'Октябрь',
          11: 'Ноябрь',
          12: 'Декабрь'}
Winter = [months[1], months[2], months[3]]
Spring = [months[4], months[5], months[6]]
Summer = [months[7], months[8], months[9]]
Autumn = [months[10], months[11], months[12]]

our_month = months[months_input]
print(our_month)

if our_month in Winter:
    print("Зима")
elif our_month in Spring:
    print("Весна")
elif our_month in Summer:
    print("Лето")
else:
    print('Осень')
