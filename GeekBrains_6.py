a = int(input('Введите результат в километрах: '))
b = int(input("Желаемый результат: "))
result_days = 1
result_km = a
print(result_days, "-ый день: ", a)
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = a
        print(result_days, "-ый день: ", a)
print(f"на %.d день спортсмен достиг результата" % result_days )
