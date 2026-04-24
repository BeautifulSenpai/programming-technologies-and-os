"""
Задача 6. Слияние отсортированных списков
Даны два списка целых чисел lst1 и lst2, каждый из которых уже
отсортирован по возрастанию. Создайте новый отсортированный
список merged, содержащий все элементы из обоих списков. Используйте
алгоритм слияния, не применяя встроенную сортировку sorted().
lst1 = [1, 3, 5]
lst2 = [2, 4, 6, 7]
print(merged) # [1, 2, 3, 4, 5, 6, 7]
"""

lst1 = [1, 3, 5]
lst2 = [2, 4, 6, 7]

merged = []
i = j = 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

while i < len(lst1):
    merged.append(lst1[i])
    i += 1

while j < len(lst2):
    merged.append(lst2[j])
    j += 1

print(merged)