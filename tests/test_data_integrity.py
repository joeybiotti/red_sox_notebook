import unittest
import pandas as pd
import os

class TestDataIntegrity(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        csv_path = os.path.join(self.base_dir, 'data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')
        self.red_sox_data = pd.read_csv(csv_path)

    def test_no_missing_values_in_critical_columns(self):
        critical_columns = ['Name', 'Season', 'Age', 'Born']
        for column in critical_columns:
            self.assertFalse(self.red_sox_data[column].isnull().any(), f"Missing values found in column: {column}")

    def test_column_data_types(self):
        expected_dtypes = {
            'Name': 'object',
            'Season': 'int64',
            'Age': 'int64',
            'Born': 'object'
        }
        for column, expected_dtype in expected_dtypes.items():
            self.assertEqual(self.red_sox_data[column].dtype, expected_dtype, f"Column {column} has incorrect dtype: {self.red_sox_data[column].dtype}")

    def test_unique_player_names_per_season(self):
        duplicates = self.red_sox_data[self.red_sox_data.duplicated(subset=['Name', 'Season'], keep=False)]
        self.assertTrue(duplicates.empty, "There are duplicate player names for the same season")

    def test_valid_age_range(self):
        valid_age_range = (self.red_sox_data['Age'] >= 16) & (self.red_sox_data['Age'] <= 60)
        self.assertTrue(valid_age_range.all(), "There are players with ages outside the valid range (16-60)")

    def test_valid_season_range(self):
        valid_season_range = (self.red_sox_data['Season'] >= 1908) & (self.red_sox_data['Season'] <= 2020)
        self.assertTrue(valid_season_range.all(), "There are seasons outside the valid range (1908-2020)")

if __name__ == '__main__':
    unittest.main()