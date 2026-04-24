"""
Задача 2. Удаление дубликатов с сохранением порядка
Дан список lst. Создайте новый список unique_lst, в котором все
элементы уникальны, а порядок их первого появления сохранён.
lst = [1, 2, 2, 3, 2, 4, 1]
print(unique_lst) # [1, 2, 3, 4]
"""

lst = [1, 2, 2, 3, 2, 4, 1]

unique_lst = []

for item in lst:
    if item not in unique_lst:
        unique_lst.append(item)

print(unique_lst)