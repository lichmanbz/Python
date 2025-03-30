# Функция для проверки и подсчета цифр в числе
def count_digits():
    while True:
        user_input = input("Введите число (или 'exit' для выхода): ")
        
        if user_input.lower() == 'exit':
            print("Выход из программы...")
            break
        
        # Проверка, является ли введенное значение числом
        if user_input.lstrip('-').isdigit():
            # Подсчет количества цифр
            digit_count = len(user_input.lstrip('-'))  # Убираем знак минус, если он есть
            print(f"В этом числе {digit_count} цифры.")
        else:
            print("Ошибка: данные не являются числом.")

# Запуск функции
count_digits()
