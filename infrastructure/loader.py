# 'https://api.frankfurter.app/1900-01-01..2020-06-15'
# import simplejson as json
from infrastructure.messages import *
import pandas as pd
import requests
import datetime

from sqlalchemy.orm import sessionmaker
from infrastructure.database_setup import engine
from infrastructure.application.domain.models import Source, Destiny


def main():
    date_from = datetime.date(1999, 1, 4)
    date_to = date_from + datetime.timedelta(days=7)
    params = date_from.isoformat() + '..' + date_to.isoformat()
    url = 'https://api.frankfurter.app/' + params
    # print(url)
    data = query(url)
    print(data)
    save(data['base'], data['rates'])

    return "status", "ok"


def save(src, dst):
    Session = sessionmaker(bind=engine)
    session = Session()

    source = Source(name='', iso=src)
    session.add(source)
    session.flush()

    fd = pd.DataFrame(dst)
    df = fd.transpose()

    for date in range(df.index.size):
        for currency in range(df.columns.size):
            destiny = Destiny(date=df.index[date], iso=df.columns[currency],
                              value=df.loc[df.index[date], df.columns[currency]],
                              source_id=source.id )
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
