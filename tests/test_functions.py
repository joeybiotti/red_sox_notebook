import unittest
import os
import pandas as pd
from scripts.visualization import red_sox_data

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.output_dir = os.path.join(self.base_dir, 'output')
        os.makedirs(self.output_dir, exist_ok=True)

    def test_data_loading(self):
        csv_path = os.path.join(self.base_dir, 'data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')
        data = pd.read_csv(csv_path)
        self.assertFalse(data.empty, "Dataframe is empty after loading")

    def test_data_transformation(self):
        csv_path = os.path.join(self.base_dir, 'data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')
        red_sox_data = pd.read_csv(csv_path)
        red_sox_data['Birth Year'] = pd.to_datetime(red_sox_data['DoB'], errors='coerce').dt.year
        self.assertTrue('Birth Year' in red_sox_data.columns, "Birth Year column not created")
        self.assertFalse(red_sox_data['Birth Year'].isnull().all(), "Birth Year column is all null")

if __name__ == '__main__':
    unittest.main()