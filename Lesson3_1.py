exeption = 0


first_argument = int(input("Введите первый аргумент: "))
second_argument = int(input("Введите второй аргумент: "))


def dividing_function():
    try:
        dividing = first_argument / second_argument
        return dividing
    except ZeroDivisionError:
        if second_argument == exeption:
            print("Деление на ночь невозомжно")
            exit()


dividing_result = dividing_function()
print(f"Результат деления - {dividing_result:.3f}",)
