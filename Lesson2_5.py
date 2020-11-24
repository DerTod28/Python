my_list = [7,5,3,3,2]
while True:
    x = int(input('Введите новый элемент списка: '))
    if x in my_list:
        position = my_list.index(x)
        amount = my_list.count(x)
        my_list.insert(position + amount, x)
        print(my_list)
    else:
        my_list.append(x)
        my_list.sort()
        my_list.reverse()
        print(my_list)
        continue
