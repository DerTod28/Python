def user_information():

    user_name = input("Введите Ваши имя и фамилию: ")
    try:
        user_name = input("Введите Ваши имя и фамилию: ")
        if user_name.isdigit():
             raise TypeError("Введите имя и фамилию с большой буквы")
    except ValueError:
        if user_name.isdigit():
            print("Вы ввели число.")


    user_date_of_birth = input("Год рождения (**.**.****): ")

    user_living_city = input("Город проживания: ")
    try:
        user_living_city = input("Город проживания: ")
    except ValueError:
        if not user_living_city.capitalize():
            print("Введите город с большой буквы")

    user_email = input("Введите вашу почту: ")
    try:
        user_email = input("Введите вашу почту: ")
    except ValueError:
        if '@' not in user_email:
            print("Попробуйте еще раз")

    user_phone_number = input("Номер телефона: ")

    if not user_phone_number.isdigit():
        print("Неверно указан номер телефона. ")
    print(f" Имя и Фамилия:{user_name}, "
          f"Год рождения:{user_date_of_birth},"
          f"Город проживания:{user_living_city}, "
          f"Почта:{user_email}, "
          f"Номер телефона:{user_phone_number}")


user_information()
