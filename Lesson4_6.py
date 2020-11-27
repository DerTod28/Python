from itertools import count
from itertools import cycle

print('Генератор целых чисел. Укажите число, с которого программа'
      'начнет генерацию целых числе. Для выведения следующего чилса нажмите Enter.'
      'Для выхода нажмите - "Q"')

for i in count(int(input("Введите первое число: "))):
    print(i)
    quit = input()
    if quit == 'q' or quit == 'Q':
        break
    #if i > 10:   возможно второе условие
        #break


print('Программа повторяет элементы списка. Введите через пробел элементы списка.')

our_list = input('Введите через пробел элементы списка: ').split()
iterrator = cycle(our_list)
quit = None
while quit != 'q':
    print(iterrator.__next__())
    quit = input()