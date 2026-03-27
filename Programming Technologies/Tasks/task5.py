"""
Задача 5: Числовая пирамида
Напишите программу, которая запрашивает у пользователя высоту
пирамиды (целое число от 1 до 9) и выводит числовую пирамиду
следующего вида:
    1
   121
  12321
 1234321
123454321
"""

while True:
    try:
        height = int(input("Введите высоту пирамиды (1-9): "))
        if 1 <= height <= 9:
            break
        else:
            print("Введите число от 1 до 9")
    except ValueError:
        print("Введите целое число")

for row in range(1, height + 1):

    line = ""

    for i in range(1, row + 1):
        line += str(i)

    for i in range(row - 1, 0, -1):
        line += str(i)

    spaces = " " * (height - row)

    print(spaces + line)