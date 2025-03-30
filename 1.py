1.	Форматирование строк

# Запрашиваем у пользователя имя, фамилию и возраст
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")

# Вывод с использованием метода format()
output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
print(output_format)

# Вывод с использованием f-string
output_f_string = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print(output_f_string)
