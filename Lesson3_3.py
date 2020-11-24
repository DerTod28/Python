def my_func():
    our_input = input("Введите три числа разделенных пробелами: ").split()

    print(our_input)

    for i in our_input:
        max_first = max(our_input)
        print(f"Первый наибольший аргумент - это {max_first}")
        our_input.remove(max_first)
        max_second = max(our_input)
        print(f"Второй наибольший аргумент - это {max_second}")
        our_input.remove(max_second)
        sum_of_max = int(max_first) + int(max_second)
        print(f"Сумма наибольших двух аргументов равняется - {sum_of_max}")
        break
        
my_func()