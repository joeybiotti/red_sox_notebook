import unittest
import os

class TestDirectoryStructure(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def test_data_directory_exists(self):
        self.assertTrue(os.path.isdir(os.path.join(self.base_dir, 'data')), "Data directory does not exist")

    def test_cleaned_data_directory_exists(self):
        self.assertTrue(os.path.isdir(os.path.join(self.base_dir, 'data/cleaned')), "Cleaned data directory does not exist")

    def test_cleaned_data_file_exists(self):
        self.assertTrue(os.path.isfile(os.path.join(self.base_dir, 'data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')), "Cleaned data file does not exist")

    def test_notebooks_directory_exists(self):
        self.assertTrue(os.path.isdir(os.path.join(self.base_dir, 'notebooks')), "Notebooks directory does not exist")

    def test_scripts_directory_exists(self):
        self.assertTrue(os.path.isdir(os.path.join(self.base_dir, 'scripts')), "Scripts directory does not exist")

    def test_tests_directory_exists(self):
        self.assertTrue(os.path.isdir(os.path.join(self.base_dir, 'tests')), "Tests directory does not exist")

if __name__ == '__main__':
    unittest.main()