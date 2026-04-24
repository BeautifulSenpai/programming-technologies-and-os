#Список студентов
students = [
 ["Анна", 5, 4, 5],
 ["Иван", 3, 4, 3],
 ["Мария", 5, 5, 5],
 ["Петр", 4, 4, 3]
]
# 1. Вычисляем средний балл и фильтруем (списковое включение)
candidates = []
for s in students:
    avg = sum(s[1:]) / 3
    if avg >= 4.0:
        candidates.append([s[0], round(avg, 2)])
# 2. Сортируем по баллу (второй элемент вложенного списка)
candidates.sort(key=lambda x: x[1], reverse=True)
# 3. Вывод результатов
print("=== СПИСОК НА СТИПЕНДИЮ ===")
for i, (name, avg) in enumerate(candidates, 1):
    print(f"{i}. {name:<10} | Средний балл: {avg}")