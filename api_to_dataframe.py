import urllib, urllib.request
import json
import requests
import numpy as np
import pandas as pd


quandl_api_key = '&api_key=pWjXmxamqHYAMueDfPUE'

api_key_only = 'pWjXmxamqHYAMueDfPUE'



def concatenate_api_key(url):
    return url + quandl_api_key
    #return url + '&api_key=' + quandl_api_key  #untested refactor


def quandl_database_code_metadata_call(database_code, return_format='json'):
    quote_url = f'https://www.quandl.com/api/v3/databases/{database_code}.{return_format}?api_key='
    call_url = concatenate_api_key(quote_url + api_key_only)

    response = requests.get(call_url)
    return response.json()


def quandl_dataset_code_metadata_call(database_code, dataset_code, return_format='json'):
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/metadata.{return_format}?api_key='
    call_url = concatenate_api_key(quote_url + api_key_only)

    response = requests.get(call_url)
    return response.json()



def quandl_api_wrapper(database_code, dataset_code): #CME, CLH2018  #CHRIS, ICE_T1
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}.json?'
 
    response = requests.get(quote_url + quandl_api_key)
    return response.json()


def quandl_api_start_date(database_code, dataset_code, start_date): #CME, CLH2018
    #start date must be yyyy-mm-dd
    quote_url = f'https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}.json?start_date={start_date}'

    response = requests.get(quote_url + quandl_api_key)
    print(response)
    return response.json()


def url_test(database_code, dataset_code, start_date):
    quote_url = f'https://www.quandl.com/api/v3/datasets/' \
            f'{database_code}/{dataset_code}.json?start_date={start_date}'
    return quote_url

def quandl_to_df(dat):
    dat = dat['dataset']
    df = pd.DataFrame(dat['data'])
    df.columns = dat['column_names']
    return df

def sort_df_by_date(df):
    return df.sort_values(by='Date')    


if __name__ == '__main__':
    print('Functions:')
    print('quandl_api_start_date', 'quandl_to_df')
    dat = quandl_api_start_date('CHRIS','ICE_T1','2019-01-02')
    df = quandl_to_df(dat)
    icet1_meta = quandl_dataset_code_metadata_call('CHRIS','ICE_T1')
