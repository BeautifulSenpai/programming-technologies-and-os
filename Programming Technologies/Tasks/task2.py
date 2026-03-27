"""
Задача 2: Таблица умножения для числа
Напишите программу, которая запрашивает у пользователя целое число
и выводит таблицу умножения для этого числа от 1 до 10.
"""

while True:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print("Введите целое число")
    
for i in range(1, 11):

    result = number * i

    print(f"{number} x {i} = {result}")
