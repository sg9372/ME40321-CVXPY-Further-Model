import unittest
from src.format_weights import format_weights

class test_extract_values(unittest.TestCase):
    # Test number of companies
    def test_Functionality(self):
        # Test if the function returns the correct number of companies
        all_companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
        companies = ['Company A', 'Company E', 'Company C']
        optimized_weights = [0.1, 0.2, 0.3]
        end_date = "01/01/2020"
        result = format_weights(all_companies, companies, optimized_weights, end_date)
        self.assertEqual(result, [end_date, 0.1, 0, 0.3, 0, 0.2])

    def test_DataType(self):
        # Test if the function returns the correct data type
        all_companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
        companies = ['Company A', 'Company E', 'Company C']
        optimized_weights = [0.1, 0.2, 0.3]
        end_date = "01/01/2020"
        result = format_weights(all_companies, companies, optimized_weights, end_date)
        self.assertIsInstance(result, list)

    def test_DateDataType(self):
        # Test if the function returns the correct data type
        all_companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
        companies = ['Company A', 'Company E', 'Company C']
        optimized_weights = [0.1, 0.2, 0.3]
        end_date = "01/01/2020"
        result = format_weights(all_companies, companies, optimized_weights, end_date)
        self.assertIsInstance(result[0], str)
    
    def test_NumberDataType(self):
        # Test if the function returns the correct data type
        all_companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Company E']
        companies = ['Company A', 'Company E', 'Company C']
        optimized_weights = [0.1, 0.2, 0.3]
        end_date = "01/01/2020"
        result = format_weights(all_companies, companies, optimized_weights, end_date)
        self.assertIsInstance(result[1], float)