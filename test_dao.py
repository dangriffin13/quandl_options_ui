import unittest
import pandas as pd
import psycopg2
import data_access_object as dao
import api_to_dataframe as api

conn = psycopg2.connect(user='danielgriffin', password='', 
                        database='quandl_ui', host='localhost')




class QuandlDAOTest(unittest.Testcase):

    def setUp(self):
        self.connection = conn