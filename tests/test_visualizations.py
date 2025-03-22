import unittest
import os
from scripts.visualization import red_sox_data, plot_age_distribution, plot_age_spread

class TestVisualizations(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.output_dir = os.path.join(self.base_dir, 'output')
        os.makedirs(self.output_dir, exist_ok=True)

    def test_visualization_age_distribution(self):
        plot_age_distribution(red_sox_data, self.output_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.output_dir, 'age_distribution.png')), "Age distribution plot not created")

    def test_visualization_age_spread(self):
        plot_age_spread(red_sox_data, self.output_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.output_dir, 'age_spread.png')), "Age spread plot not created")

if __name__ == '__main__':
    unittest.main()