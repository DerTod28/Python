class DivisionZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def division(num_1, num_2):
        try:
            if num_2 == 0:
                raise DivisionZeroError("Деление на ноль невозможно!")
        except (ValueError, DivisionZeroError) as err:
            print(err)
        else:
            print(num_1 / num_2)

DivisionZeroError.division(3, 1)
DivisionZeroError.division(3, 0)
