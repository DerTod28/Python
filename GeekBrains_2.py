#Задание_2
var_time_in_seconds = int(input('Введите время в секундах: '))
hours = int(var_time_in_seconds // 3600)
minutes = int((var_time_in_seconds - hours * 3600) // 60)
sec = int(var_time_in_seconds - (hours * 3600 + minutes * 60))
print(str(var_time_in_seconds) + " секунд- это: {0}h:{1}m:{2}c".format(hours,minutes,sec))