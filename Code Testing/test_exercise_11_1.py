import unittest

from exercise_11_1 import get_formatted_location


class LocationTestCase(unittest.TestCase):
    """Test run for exercise_11_1.py."""

    def test_city_country_location(self):
        """Check if formatting for Chile location would work"""
        formatted_location = get_formatted_location('santiago', 'chile')
        self.assertEqual(formatted_location,'Santiago, Chile')

    def test_city_population(self):
        """Test run if city population included"""

        formatted_location = get_formatted_location('santiago','chile',population=5000000)
        self.assertEqual(formatted_location,'Santiago, Chile - population 5000000')


unittest.main()