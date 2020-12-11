class Data:
    def __init__(self, string):
        """принимает дату в виде строки "день - месяц - год" """
        self.string = string
        self.get_our_data()

    def get_our_data(self):
        self.day, self.month,self.year = map(int, self.string.split("-"))

    @staticmethod
    def our_date(day, month, year):
        if day in range(1,32) and month in range(1, 12) and year > 0:
            return True
        else:
            return False

    def __str__(self):
        return " ".join(map(str, (self.day, self.month, self.year)))

our_date = Data("20-06-2011")
print(our_date)