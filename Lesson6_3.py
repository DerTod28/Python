class Worker:
    bonus = 5000
    wage = 10000
    full_income = {"оклад": wage, "премия": bonus}
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        print({name}, {surname}, {position}, {income})


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        print(Worker.full_income)
        finall_income = self._income
        print(f"Доход составляет: {self._income}")
        print(f"Итоговая сумма дохода: {sum(Worker.full_income.values()) + finall_income}")


worker_1 = Position("Алексей", "Иванов", "водитель", 20000)
worker_1.get_full_name()
worker_1.get_total_income()
