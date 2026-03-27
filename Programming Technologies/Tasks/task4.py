"""
Задача 4: Поиск простых чисел
Напишите программу, которая выводит все простые числа в диапазоне
от 1 до N, где N вводит пользователь. Простое число — это натуральное
число больше 1, которое делится только на 1 и на само себя.
"""

while True:
    try:
        n = int(input("Введите верхнюю границу N: "))
        break
    except ValueError:
        print("Введите целое число")

print(f"Простые числа от 1 до {n}:")

for number in range(2, n + 1):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")