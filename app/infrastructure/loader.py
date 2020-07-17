from .messages import *
import requests

from app.models.operations import open_session, close_session
from app.models.source import Source
from app.models.destiny import Destiny

from app.application.frank_config import *
from app.application.frankfurter import make_list_url



def main():
    arr = make_list_url(year_from, month_from, day_from, base_url, periods)
    session = open_session()

    data = query(arr[0])
    session = save(data['base'], session) 

    close_session()
    return "status", "ok"

def save(iso_new, session):
    list_instances = []

    for instance in session.query(Source.iso):
        print(instance.iso, iso_new)
        if instance.iso != iso_new:
            source = Source(name='', iso=iso_new)
            list_instances.append(source)

    session.add_all(list_instances)
    return session

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
