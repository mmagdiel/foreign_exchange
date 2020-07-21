import unittest
import datetime
from app.application.frankfurter import Frankfurter

class TestFrankfurter(unittest.TestCase):
    def test_array_correlation_size(self):
        frank = Frankfurter()
        arr = frank.make_list_url()
        date_today = datetime.date.today()
        date_from = datetime.date(frank.year_from, frank.month_from, frank.day_from)
        iterations, total_days, adicional_days = frank.calculate_numbers_of_days(date_today, date_from)

        if total_days % frank.periods == 0: 
            self.assertEquals(iterations, len(arr))
        else:
            self.assertEquals(iterations+1, len(arr))


if __name__ == '__main__':
    unittest.main()
