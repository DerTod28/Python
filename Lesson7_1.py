A = [[1, 2], [3, 4], [5, 6]]
B = [[7, 8], [9, 10], [11, 12]]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, el)) for el in self.matrix])

    # output:
    # 1 2
    # 3 4
    # 5 6

    def __add__(self, other):
        return Matrix(map(lambda mtrx_1, mtrx_2: map(lambda x, y: x + y, mtrx_1, mtrx_2), self.matrix, other.matrix))


matrix_1 = Matrix(A)
print("Матрица №1")
print(matrix_1)
matrix_2 = Matrix(B)
print("Матрица №2")
print(matrix_2)
print("Результат сложения матриц")
print(matrix_1 + matrix_2)
