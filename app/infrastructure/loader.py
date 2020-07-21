import requests
from typing import List

HTTP_ERROR_MSG = "An HTTP error occurred"
CONNECTION_ERROR_MSG = "A Connection error occurred"
URL_REQUIRED_MSG = "A valid URL is required to make a request"
TOO_MANY_REDIRECTS_MSG = "Too many redirects"
READ_TIMEOUT_MSG = "The server did not send any data in the allotted amount of time"
REQUEST_EXCEPTION_MSG = "Other error occurred"

def query(url: str) -> List:
    """exec request"""
    try:
        response = requests.get(url, headers={})
        if response.status_code >= 200 or response.status_code <= 399:
            return response.json(), 200
    except requests.exceptions.HTTPError as httpError_err:
        print(f'{HTTP_ERROR_MSG}: {httpError_err}')
        res = { msg: HTTP_ERROR_MSG, obj: httpError_err}, 400
    except requests.exceptions.ConnectionError as connectionError_err:
        print(f'{CONNECTION_ERROR_MSG}: {connectionError_err}')
        res = { msg: CONNECTION_ERROR_MSG, obj: connectionError_err}, 444
    except requests.exceptions.URLRequired as urlRequired_err:
        print(f'{URL_REQUIRED_MSG}: {urlRequired_err}')
        res = { msg: URL_REQUIRED_MSG, obj: urlRequired_err}, 414
    except requests.exceptions.TooManyRedirects as tooManyRedirects_err:
        print(f'{TOO_MANY_REDIRECTS_MSG}: {tooManyRedirects_err}')
        res = { msg: TOO_MANY_REDIRECTS_MSG, obj: tooManyRedirects_err}, 429
    except requests.exceptions.ReadTimeout as readTimeout_err:
        print(f'{READ_TIMEOUT_MSG}: {readTimeout_err}')
        res = { msg: READ_TIMEOUT_MSG, obj: readTimeout_err}, 504
    except requests.exceptions.RequestException as requestException_err:
        print(f'{REQUEST_EXCEPTION_MSG}: {requestException_err}')
        res = { msg: REQUEST_EXCEPTION_MSG, obj: requestException_err}, 500
    return res
