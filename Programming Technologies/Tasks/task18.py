"""
Задача 3. Группировка по чётности
Дан список целых чисел nums. Создайте два списка: even_nums (чётные
числа) и odd_nums (нечётные числа). Порядок чисел в каждом списке должен
соответствовать исходному.
nums = [1, 4, 7, 2, 9, 8]
print(even_nums) # [4, 2, 8]
print(odd_nums) # [1, 7, 9]
"""

nums = [1, 4, 7, 2, 9, 8]

even_nums = []
odd_nums = []

for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(even_nums)
print(odd_nums)