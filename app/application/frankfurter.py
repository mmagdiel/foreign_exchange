# 'https://api.frankfurter.app/1900-01-01..2020-06-15'
import datetime

class Frankfurter:
    def __init__(self, periods=7, day_from=4, month_from=1, year_from=1999, base_url='https://api.frankfurter.app/'):
        self.periods = periods 
        self.base_url = base_url
        self.day_from = day_from 
        self.year_from = year_from
        self.month_from = month_from 


    def make_list_url(self):
        arr = []
        date_today = datetime.date.today()
        date_from = datetime.date(self.year_from, self.month_from, self.day_from)
        iterations, total_days, adicional_days = self.calculate_numbers_of_days(date_today, date_from)

        for _ in range(iterations):
            date_to = date_from + datetime.timedelta(days=self.periods)
            arr.append( self.base_url + date_from.isoformat() + '..' + date_to.isoformat() )
            date_from = date_to

        date_to = date_from + datetime.timedelta(adicional_days)
        arr.append( self.base_url + date_from.isoformat() + '..' + date_to.isoformat() )
        
        return  arr


    def calculate_numbers_of_days(self, date_today, date_from):
        delta_days =  date_today - date_from
        total_days = int(delta_days.days)
        iterations = int(delta_days.days/self.periods)
        adicional_days = (delta_days.days - int(delta_days.days/self.periods)*self.periods)
        
        return iterations, total_days, adicional_days