import unittest
from stats_function import mean_vict_age, median_vict_age
from validate_functions import valid_datatype

class StatValidateFunctionsTest(unittest.TestCase):
    def test_mean_vict_age(self):
        self.assertIsInstance(mean_vict_age(), float)
    def test_median_vict_age(self):
        self.assertIsInstance(median_vict_age(), float)
    def test_valid_datatype(self):
        self.assertEqual(valid_datatype(), True)

    if __name__ == '__main__': unittest.main()
