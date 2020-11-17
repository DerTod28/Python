#выручка
earnings = int(input("Введите значение выручки: "))
#издержки
firm_cost_value = int(input("Введите значение издержек фирмы: "))
if earnings > firm_cost_value:
    print("Прибыль на "+ str(earnings - firm_cost_value))
else:
    print("Убыток на "+ str(earnings - firm_cost_value))
employees = int(input("Введите количество сотрудников: "))
earnings_for_one_person = earnings / employees
print("Количетсво выручки на одного: ", earnings_for_one_person, "рублей")
