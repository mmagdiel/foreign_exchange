# 'https://api.frankfurter.app/1900-01-01..2020-06-15'
# import simplejson as json
from messages import *
import requests
import datetime


def main():
    now = datetime.datetime.now()
    params = '1900-01-01..' + datetime.date.today().isoformat()
    url = 'https://api.frankfurter.app/' + params
    listest = query(url)
    print(listest)
    return listest


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
