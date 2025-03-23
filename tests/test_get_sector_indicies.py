import unittest

from src.get_sector_indicies import get_sector_indicies

class test_get_index_indicies(unittest.TestCase):
    # Tests
    def test_basic_case(self):
        all_sectors = ["Tech", "Finance", "Healthcare"]
        sectors = ["Tech", "Finance", "Tech", "Healthcare", "Finance"]
        expected = [[0, 2], [1, 4], [3]]
        self.assertEqual(get_sector_indicies(all_sectors, sectors), expected)
    
    def test_empty_sectors(self):
        all_sectors = ["Tech", "Finance"]
        sectors = []
        expected = [[], []]
        self.assertEqual(get_sector_indicies(all_sectors, sectors), expected)
    
    def test_no_matching_sectors(self):
        all_sectors = ["Tech", "Finance"]
        sectors = ["Healthcare", "Energy"]
        expected = [[], []]
        self.assertEqual(get_sector_indicies(all_sectors, sectors), expected)
    
    def test_all_companies_same_sector(self):
        all_sectors = ["Tech"]
        sectors = ["Tech", "Tech", "Tech"]
        expected = [[0, 1, 2]]
        self.assertEqual(get_sector_indicies(all_sectors, sectors), expected)
    
    def test_duplicate_sectors(self):
        all_sectors = ["Tech", "Tech", "Finance"]
        sectors = ["Tech", "Finance", "Tech", "Healthcare", "Finance"]
        expected = [[0, 2], [0, 2], [1, 4]]
        self.assertEqual(get_sector_indicies(all_sectors, sectors), expected)