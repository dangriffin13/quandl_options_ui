import urllib, urllib.request
import json
import requests
import numpy as np
import pandas as pd


quandl_api_key = '&api_key=pWjXmxamqHYAMueDfPUE'

murl = f'https://www.quandl.com/api/v3/datasets/CME/CLH2018.json?start_date=2018-01-04&api_key=pWjXmxamqHYAMueDfPUE'

r = requests.get(murl)

dat = r.json()['dataset']


def quandl_api_wrapper(database_code, dataset_code): #CME, CLH2018
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}.json?'

    response = requests.get(quote_url + quandl_api_key)
    return response.json()


def quandl_api_start_date(database_code, dataset_code, start_date): #CME, CLH2018
    #start date must be yyyy-mm-dd
    quote_url = f'https://www.quandl.com/api/v3/datasets/' \
        '{database_code}/{dataset_code}.json?start_date={start_date}'

    response = requests.get(quote_url + quandl_api_key)
    return response.json()

