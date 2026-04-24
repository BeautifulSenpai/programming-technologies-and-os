"""
Задача 7. Транспонирование матрицы
Матрица представлена списком списков (строки) matrix. Создайте новую
матрицу transposed, в которой строки и столбцы поменяны местами.
Предполагается, что матрица прямоугольная (все строки одинаковой длины).
matrix = [[1, 2, 3], [4, 5, 6]]
print(transposed)
"""

matrix = [[1, 2, 3], [4, 5, 6]]

rows = len(matrix)
cols = len(matrix[0])

transposed = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print(transposed)