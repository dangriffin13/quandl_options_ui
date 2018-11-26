import unittest
import pandas as pd
import requests
from api_to_dataframe import quandl_api_wrapper

call_url = 'https://www.quandl.com/api/v3/datasets/CME/CLH2018.json?start_date=2018-01-04&api_key=pWjXmxamqHYAMueDfPUE'

class QuandlAPITest(unittest.Testcase):

    def setUp(self):
        self.response = requests.get(call_url)
    

    def test_api_connection:
        self.assertTrue(self.response)


    def test_df_columns:
        self.assertEqual(quandl_to_df(self.data).columns.tolist(), ['Date', 'Open', 'High', 'Low', 'Last', 'Change', 'Settle', 'Volume', 'Previous Day Open Interest'])


    def test_date_sorting:
        df = quandl_to_df(self.response)
        self.assertEqual(df.iloc[31]['Date'], '2018-01-04')