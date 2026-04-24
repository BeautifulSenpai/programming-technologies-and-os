"""
Задача 8. Плоский список с произвольной вложенностью
Дан список nested_list, который может содержать элементы или другие
списки (любой глубины вложенности). Создайте одномерный список flat_list,
содержащий все элементы в порядке их следования. Решите задачу без
рекурсии, используя явный стек (список).
nested_list = [1, [2, 3], [[4], [5, 6]], 7]
print(flat_list) # [1, 2, 3, 4, 5, 6, 7]
"""

nested_list = [1, [2, 3], [[4], [5, 6]], 7]

flat_list = []
stack = [nested_list]

while stack:
    current = stack.pop(0)
    
    if isinstance(current, list):
        for item in reversed(current):
            stack.insert(0, item)
    else:
        flat_list.append(current)

print(flat_list)