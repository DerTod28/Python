x = int(input("Введите целое положительное число: "))
maximum = x%10
print(maximum)
x = x//10
while x > 0:
    if x%10 > maximum:
        maximum = x % 10
    x = x//10
print(maximum)

