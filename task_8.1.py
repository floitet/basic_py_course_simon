# Task 8.1
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        global day_int, month_int, year_int
        day_int, month_int, year_int = map(int, date_as_string.split('-'))
        return cls(day_int, month_int, year_int)

    @staticmethod
    def is_date_valid():
        return day_int <= 31 and month_int <= 12 and year_int <= 3999

date2 = Date.from_string('11-09-2012')
print(date2.day, date2.month, date2.year)
is_date = Date.is_date_valid()