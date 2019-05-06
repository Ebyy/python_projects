import unittest

from world_countries_codes import get_country_codes


class CountryCodesTestCase(unittest.TestCase):
    """Write test case for world_country_codes.py"""
    def test_get_country_codes(self):
        """Check if the test is valid"""
        country_code = get_country_codes('Afghanistan')
        self.assertEqual(country_code, 'af')

unittest.main()
