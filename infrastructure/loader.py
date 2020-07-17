from infrastructure.messages import *
import pandas as pd
import requests

from sqlalchemy.orm import sessionmaker
from infrastructure.database.operations import open_session
from infrastructure.application.domain.models import Source, Destiny

from infrastructure.application.frank_config import *
from infrastructure.application.frankfurter import make_list_url, calculate_numbers_of_days

def main():
    arr = make_list_url(year_from, month_from, day_from, base_url, periods)
    session = open_session()
    
    for url in arr:
        data = query(url)
        save(data['base'], data['rates'])

    session.close()
    return "status", "ok"


def save(src, dst):

    source = Source(name='', iso=src)
    session.add(source)
    session.flush()

    fd = pd.DataFrame(dst)
    df = fd.transpose()

    for date in range(df.index.size):
        for currency in range(df.columns.size):
            destiny = Destiny(date=df.index[date], iso=df.columns[currency],
                              value=df.loc[df.index[date],
                                           df.columns[currency]],
                              source_id=source.id)
            session.add(destiny)
            session.commit()
    session.close()


def query(url: str):
    """exec request"""
    try:
        response = requests.get(url, headers={})
        if response.status_code != 200:
            return None, 0
        return response.json()
    except requests.exceptions.HTTPError as httpError_err:
        print(f'{HTTP_ERROR_MSG}: {httpError_err}')
    except requests.exceptions.ConnectionError as connectionError_err:
        print(f'{CONNECTION_ERROR_MSG}: {connectionError_err}')
    except requests.exceptions.URLRequired as urlRequired_err:
        print(f'{URL_REQUIRED_MSG}: {urlRequired_err}')
    except requests.exceptions.TooManyRedirects as tooManyRedirects_err:
        print(f'{TOO_MANY_REDIRECTS_MSG}: {tooManyRedirects_err}')
    except requests.exceptions.ReadTimeout as readTimeout_err:
        print(f'{READ_TIMEOUT_MSG}: {readTimeout_err}')
    except requests.exceptions.RequestException as requestException_err:
        print(f'{REQUEST_EXCEPTION_MSG}: {requestException_err}')
    return None, 0
