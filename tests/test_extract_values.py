import unittest
import numpy as np
import pandas as pd
from src.extract_sheet_data import extract_sheet_data
from src.extract_values import extract_values

class test_extract_values(unittest.TestCase):
    # Test number of companies
    def test_CompaniesCount(self):
        # Test if the function returns the correct number of companies
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
        end_Date = '02/01/2020'
        rows = 2
        
        values,_ = extract_values(file, companies, end_Date, rows)
        self.assertEqual(values.shape, (2, 101))

    # Ensure no NaN
    def test_RemoveNaN(self):
        # Test if the function returns no NaN values
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
        end_Date = '01/02/2020'
        rows = 20
        
        values,_ = extract_values(file, companies, end_Date, rows)
        self.assertFalse(np.isnan(values).any())

    # Test data type is np.array
    def test_ValuesDataType(self):
        # Test if the function returns values as a numpy array
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
        end_Date = '02/01/2020'
        rows = 2
        
        values,_ = extract_values(file, companies, end_Date, rows)
        self.assertIsInstance(values, np.ndarray)

    # Test date collecting works
    def test_DateCollection(self):
        # Test if the function returns the correct number of dates
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
<<<<<<< HEAD
        end_Date = '05/01/2020'
        rows = 3
        
        _,dates = extract_values(file, companies, end_Date, rows)
        self.assertEqual(len(dates), 3)
=======
        start_Date = '01/01/2020'
        end_Date = '06/01/2020'
        

        _,dates = extract_values(file, companies, start_Date, end_Date)
        self.assertEqual(len(dates), 4)

    # Test data type is np.array
    def test_DateDataType(self):
        # Test if the function returns dates as a numpy array
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
        start_Date = '01/01/2020'
        end_Date = '06/01/2020'
        
        _,dates = extract_values(file, companies, start_Date, end_Date)
        self.assertIsInstance(dates, pd.Series)
        
>>>>>>> b697049128bba8e3694ebff41e7326c57f1be117
