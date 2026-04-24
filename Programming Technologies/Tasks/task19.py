"""
Задача 4. Сжатие списка
Дан список lst. Создайте новый список compressed, в котором
подряд идущие одинаковые элементы заменяются на пары [элемент,
количество]. Если элемент не повторяется (количество = 1), он остаётся как
есть (без счётчика).
lst = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
print(compressed) # [[1, 3], [2, 2], 3, [4, 4], 5]
"""

lst = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5]
compressed = []

i = 0
while i < len(lst):
    current = lst[i]
    count = 1
    
    while i + count < len(lst) and lst[i + count] == current:
        count += 1
    
    if count == 1:
        compressed.append(current)
    else:
        compressed.append([current, count])
    
    i += count

print(compressed)