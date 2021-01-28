#This example uses Python 2.7 and the python-request library.
import os

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import yaml

def retrcrypto():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    key = None
    # !/usr/bin/env python


    with open("../config.yaml", 'r') as stream:
        try:
            key = yaml.safe_load(stream)['coinmarketcap']['api_key']
        except yaml.YAMLError as exc:
            print(exc)

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

    crypto_df = None

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        crypto_df = pd.DataFrame.from_dict(data['data'])[['name', 'symbol']]
        crypto_df.rename(columns={'name': 'Name', 'symbol': 'Symbol'})

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    path = os.path.join('../', 'files', 'cryptolist')
    if not os.path.isdir(path):
        os.makedirs(path)
    with open('../files/cryptolist/coinmarketbaselisted.csv', 'wb') as fp:
        crypto_df.to_csv('./files/cryptolist/coinmarketbaselisted.csv')


def retrdataframe():
    retrcrypto()
    return pd.read_csv('../files/cryptolist/coinmarketbaselisted.csv')