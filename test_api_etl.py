import unittest
import pandas as pd
import requests
from api_to_dataframe import quandl_api_wrapper

data_call_url = 'https://www.quandl.com/api/v3/datasets/CME/CLH2018.json?start_date=2018-01-04&api_key=pWjXmxamqHYAMueDfPUE'

db_call_url = 'https://www.quandl.com/api/v3/databases/CHRIS.json?api_key=pWjXmxamqHYAMueDfPUE'

class QuandlAPITest(unittest.Testcase):

    def setUp(self):
        self.data = requests.get(data_call_url)
        self.db_metadata = requests.get(db_call_url)
    

    def test_api_connection:
        self.assertTrue(self.data)


    def test_metadata_call:
        self.assetTrue(self.db_metadata)


    def test_df_column_headings:
        self.assertEqual(quandl_to_df(self.data).columns.tolist(), ['Date', 'Open', 'High', 'Low', 'Last', 'Change', 'Settle', 'Volume', 'Previous Day Open Interest'])


    def test_date_sorting:
        df = sort_df_by_date(quandl_to_df(self.data))
        self.assertEqual(df.iloc[-1]['Date'], '2018-01-04')

