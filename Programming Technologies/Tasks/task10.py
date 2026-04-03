"""
Напишите программу-калькулятор, которая запрашивает у пользователя:
1. Перое число
2. Второе число
3. Операция (+,-,*,/)
Программа должна вывести результат выполнения операции над числами
Требования:
При делении на ноль вывести "Ошибка: деление на ноль"
Если введена неизвестная операция, вывести "Неизвестная операция"
"""

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    
    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
            print(f"Результат: {result}")
            break
        elif operation == '-':
            result = num1 - num2
            print(f"Результат: {result}")
            break
        elif operation == '*':
            result = num1 * num2
            print(f"Результат: {result}")
            break
        elif operation == '/':
            result = num1 / num2
            print(f"Результат: {result}")
            break
        else:
            print("Неизвестная операция")

except ValueError:
    print("Ошибка: введены некорректные числа")
except ZeroDivisionError: #или делаем как крутые и пишем проверку if num2 == 0
    print("Ошибка: деление на ноль")