import unittest
from src.extract_sheet_data import extract_sheet_data
from src.extract_values import extract_values

class test_extract_values(unittest.TestCase):
    # Test number of companies
    def test_CompaniesCount(self):
        # Test if the function returns the correct number of companies
        file = 'Monthly FTSE Data - New.xlsx'
        companies,_,_ = extract_sheet_data(file, '01_2020')
        start_Date = '01/01/2020'
        end_Date = '02/01/2020'
        
        values = extract_values(file, companies, start_Date, end_Date)
        self.assertEqual(len(values), len(companies))
