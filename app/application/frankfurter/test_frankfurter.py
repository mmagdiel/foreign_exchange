import unittest
import datetime
from .config import *
from . import make_list_url, calculate_numbers_of_days

class TestFrankfurter(unittest.TestCase):
    def test_array_correlation_size(self):
        arr = make_list_url(year_from, month_from, day_from, base_url, periods)
        date_today = datetime.date.today()
        date_from = datetime.date(year_from, month_from, day_from)
        iterations, total_days, adicional_days = calculate_numbers_of_days(date_today, date_from, periods)

        if total_days % periods == 0: 
            self.assertEquals(iterations, len(arr))
        else:
            self.assertEquals(iterations+1, len(arr))


if __name__ == '__main__':
    unittest.main()
