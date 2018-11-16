import unittest
import pandas as pd
from api_to_dataframe import quandl_api_wrapper

class QuandlAPITest(unittest.Testcase):

    def setUp(self):
        self.data = []
        self.api_key = '&api_key=pWjXmxamqHYAMueDfPUE'