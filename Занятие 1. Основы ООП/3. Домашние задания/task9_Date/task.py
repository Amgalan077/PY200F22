class Date:
    def __init__(self, day, month, year):
        all_int = all(isinstance(i, int) for i in (day, month, year))
        if not all_int:
            raise TypeError
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"Date({self.day, self.month, self.year})"

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"


data = Date(2, 3, 2001)
print(data)
