class MyOwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    in_data = input("Введите числа через пробел: ").split()
    if 'stop' in in_data:
        exit()
    our_list = []
    try:
        for el in in_data:
            if el.isdigit():
                our_list.append(el)

            else:
                print(f" Вы ввели - {type(el)}")
                raise MyOwnError("Допустимы только числа")
        print(f"Ваш список - {our_list}")
    except(ValueError, MyOwnError) as err:
        print(err)
