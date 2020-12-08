class Cells:
    def __init__(self, cells):
        self.cells = cells

    def make_order(self, rows):
        return '\n'.join(['x' * rows for _ in range(self.cells // rows)]) + '\n' + 'x' * (self.cells % rows)

    def __str__(self):
        return self.cells

    def __add__(self, other):
        return f"Сумма клеток: {self.cells + other.cells}"

    def __sub__(self, other):
        return self.cells - other.cells if self.cells - other.cells > 0 else "Вычитание невозможно"

    def __mul__(self, other):
        return f"Умнижение клеток: {self.cells * other.cells}"

cell_1 = Cells(10)
cell_2 = Cells(5)

print(cell_1 + cell_2)
print(cell_2.make_order(2))