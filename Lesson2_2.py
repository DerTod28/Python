empty_list = list()
while True:
    our_list = input("Введите элемент списка: ")
    empty_list.append(our_list)
    print(empty_list)
    if our_list == '999':
        i = 0
        for i in range(0, (len(empty_list))-1, 2):
            old_index = empty_list[i]
            empty_list[i] = empty_list[i+1]
            empty_list[i+1] = old_index
        print(empty_list)
        break
