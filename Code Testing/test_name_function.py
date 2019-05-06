import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'function_test_name.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_middle_name(self):
        """Test run when middle name is included."""

        formatted_name = get_formatted_name('janis','mary','joplin')
        self.assertEqual(formatted_name,'Janis Mary Joplin')


unittest.main()
