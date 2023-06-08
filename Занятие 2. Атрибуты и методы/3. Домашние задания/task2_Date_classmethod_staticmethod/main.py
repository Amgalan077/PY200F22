class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @classmethod
    def is_leap_year(cls, year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return True
        return False
        # TODO реализовать метод

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[1][month - 1]
        return cls.DAY_OF_MONTH[0][month - 1]
        ...  # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if 1 < year and (1 <= month <= 12) and 1 <= day <= Date.get_max_day(month, year):
            return 'Дата корректная'
        return "Дата некорректная"
        ...  # TODO проверить валидность даты


print(Date.is_valid_date(22, 12, 2022))
