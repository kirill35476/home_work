# Создаем пустой список
numbers = []

# Запрашиваем у пользователя 5 чисел
for i in range(5):
    num = float(input(f"Введите число {i + 1}: "))
    numbers.append(num)  # Добавляем число в список

# Сортируем список
numbers.sort()

# Выводим отсортированный список
print("Отсортированный список чисел:")
print(numbers)
