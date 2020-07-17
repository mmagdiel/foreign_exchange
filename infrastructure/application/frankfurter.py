# 'https://api.frankfurter.app/1900-01-01..2020-06-15'
import datetime
from infrastructure.application.frank_config import *

def make_list_url(year_from, month_from, day_from, base_url, periods):
    arr = []
    date_today = datetime.date.today()
    date_from = datetime.date(year_from, month_from, day_from)
    iterations, total_days, adicional_days = calculate_numbers_of_days(date_today, date_from, periods)

    for _ in range(iterations):
        date_to = date_from + datetime.timedelta(days=periods)
        arr.append( base_url + date_from.isoformat() + '..' + date_to.isoformat() )
        date_from = date_to

    date_to = date_from + datetime.timedelta(adicional_days)
    arr.append( base_url + date_from.isoformat() + '..' + date_to.isoformat() )
    
    return  arr


def calculate_numbers_of_days(date_today, date_from, periods):
    delta_days =  date_today - date_from
    total_days = int(delta_days.days)
    iterations = int(delta_days.days/periods)
    adicional_days = (delta_days.days - int(delta_days.days/periods)*periods)
    
    return iterations, total_days, adicional_days