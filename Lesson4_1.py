from sys import argv

name, amount_of_hours, pay_rate, award = argv
final_pay_rate = (float(amount_of_hours) * float(pay_rate)) + float(award)


print("Количество отрабобтанных часов: ", amount_of_hours)
print("Ставка в час: ", pay_rate)
print("Премия: ", award)
print("""Расчет заработной платы происходит по 
        следующей формуле:
        
        (выработка в часах * ставка в час) + премия    
      """)

print(f"Ваша заработная плата составляет: {final_pay_rate}")
