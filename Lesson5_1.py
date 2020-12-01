with open("new_file.txt", "w", encoding="utf-8") as f:
    while True:
        m = input("Введите слово для записи в файл: ")
        f.write(f"{m}\n")
        if not m:
            break
