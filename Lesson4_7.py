def factorial(number):
    f_start = 1
    for i in range(1,number+1):
        f_start = f_start * i
        yield f'{i}! = {f_start}'

number = int(input("Факториал числа n. Введите число 'n': "))
if number == 0:
    print(f"{number}! = 1")
# try:
#     number = int(input())
# except ValueError:
#     print("Необходимо ввести число")
#     number = int(input("Введите число еще раз: "))

for el in factorial(number):
    print(el)