import urllib, urllib.request
import json
import requests
import numpy as np
import pandas as pd
import data_access_object as dao

api_url = 'https://www.quandl.com/api/v3/'

quandl_api_key = '&api_key=pWjXmxamqHYAMueDfPUE'

api_key_only = 'pWjXmxamqHYAMueDfPUE'



def concatenate_api_key(url):
    return url + api_key_only
    #return url + '&api_key=' + quandl_api_key  #untested refactor


def quandl_database_code_metadata_call(database_code, return_format='json'):
    quote_url = api_url + f'databases/{database_code}.{return_format}?api_key='
    call_url = concatenate_api_key(quote_url)

    response = requests.get(call_url)
    return response.json()


def quandl_dataset_code_metadata_call(database_code, dataset_code, return_format='json'):
    quote_url = api_url + f'datasets/{database_code}/{dataset_code}/metadata.{return_format}?api_key='
    call_url = concatenate_api_key(quote_url)

    response = requests.get(call_url)
    http_status_check(response)
    return response.json()



def quandl_api_wrapper(database_code, dataset_code): #CME, CLH2018; CHRIS, ICE_T1
    quote_url = api_url + f'datasets/{database_code}/{dataset_code}.json?'
 
    response = requests.get(quote_url + quandl_api_key)
    return response.json()


def quandl_api_start_date(database_code, dataset_code, start_date): #CME, CLH2018
    #start date must be yyyy-mm-dd
    quote_url = api_url + f'datasets/{database_code}/{dataset_code}' \
        f'.json?start_date={start_date}'

    response = requests.get(quote_url + quandl_api_key)
    http_status_check(response)
    return response.json()


def url_test(database_code, dataset_code, start_date):
    quote_url = api_url + f'datasets/{database_code}/{dataset_code}' \
        f'.json?start_date={start_date}'

    return quote_url

def quandl_to_df(dat):
    dat = dat['dataset']
    df = pd.DataFrame(dat['data'])
    df.columns = dat['column_names']
    return df


def check_dataset_headings(data):
    #get database
    cols = dao.get_column_names(data['database_code'])
    #check if database has headings to match dataset
    #include heading in database


def prep_df_for_db(df):
    #this may have to be a factory method for different quandl databases
    pass


def prep_df_for_chris(df):
    df['dataset_master_id'] = dao.get_dataset_master_id(dataset_code)
    df.rename(str.lower, axis='columns', inplace=True)
    df.rename(columns={'prev. day open interest':'open_interest'}, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df

def refresh_db(database):
    #select a certain database and pull the most recent data from quandl
    pass

def refresh_all_db():
    #refresh data from quandl for ALL databases
    #this could be risky.  a change on quandl to one DB could break this whole thing
    #untangling the cause could be futile
    pass


def sort_df_by_date(df):
    return df.sort_values(by='Date')    

def http_status_check(response):
    if response.status_code == 200:
        print('Call successful')
    else:
        print(response.status_code)


class Dataset:
    def __init__(self, meta, dat):
        self.meta = meta
        self.dat = dat


if __name__ == '__main__':
    print('Functions:')
    print('quandl_api_start_date', 'quandl_to_df')
    dat = quandl_api_start_date('CHRIS','ICE_T1','2019-01-02')
    df = quandl_to_df(dat)
    icet1_meta = quandl_dataset_code_metadata_call('CHRIS','ICE_T1')
    icet1_id = icet1_meta['dataset']['id']
