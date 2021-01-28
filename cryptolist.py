#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
key = None
#!/usr/bin/env python

import yaml

with open("config.yaml", 'r') as stream:
    try:
        key = yaml.safe_load(stream)['coinmarketcap']['api_key']
    except yaml.YAMLError as exc:
        print(exc)



def retrcrypto():

    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)