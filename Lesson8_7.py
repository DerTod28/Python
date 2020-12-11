class ComplexNumber:
    """Операции с комплексными числами"""
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f"Сумма v1 и v2 равна")
        return f'z = {self.a + other.b} + {self.b + other.a} * i'

    def __mul__(self, other):
        print(f'Произведение 1 и v2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

v_1 = ComplexNumber(1, -2)
v_2 = ComplexNumber(3, 4)
print(v_1)
print(v_2)
print(v_1 + v_2)
print(v_1*v_2)