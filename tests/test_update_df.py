import unittest
import pandas as pd
from src.update_df import update_df

class test_add_first_line(unittest.TestCase):
    # Test number of companies
    def test_first_pass_shape(self):
        # Test if the function correctly appends first line to df.
        new_weights_df = pd.DataFrame(columns=['Date'] + ['Company1', 'Company2', 'Company3', 'Company4', 'Company5'])
        result = update_df(new_weights_df, new_weights=['2021-01-01', 0.1, 0.2, 0.3, 0.4, 0.5])
        self.assertEqual(result.shape, (1, 6))

    def test_append_shape(self):
        # Test if the function correctly appends to df.
        new_weights_df = pd.DataFrame(columns=['Date'] + ['Company1', 'Company2', 'Company3', 'Company4', 'Company5'])
        new_weights_df = update_df(new_weights_df, end_date='2021-01-01', new_weights=[0.1, 0.2, 0.3, 0.4, 0.5])
        result = update_df(new_weights_df, new_weights=['2021-02-01', 0.1, 0.2, 0.3, 0.4, 0.5])
        self.assertEqual(result.shape, (2, 6))