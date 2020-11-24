def sum_of_separated_numbers():
    result = 0
    run_this_code = True
    try:
        while run_this_code:
            user_input = input("Введите числа, разделенные пробелом: ")  # Ввод
            separated_list = user_input.split()  # Создаем список
            x = list(map(int, separated_list))
            print(f"Вы ввели следующие цифры - {x}")

            for i in x:
                result += i
            print(f"Сумма всех чисел = {result}")
    except ValueError:
        print(f"Итоговая сумма = {result}")


sum_of_separated_numbers()
