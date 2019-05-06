import unittest

from exercise_11_3 import Employee


class TestEmployee(unittest.TestCase):

    """Test that Employee module works properly."""

    def setUp(self):
        self.hannah = Employee('hannah', 'brown', 57000)

    def test_give_default_raise(self):
        """Test that default raise works."""
        self.hannah.give_raise()
        self.assertIn(str(self.hannah.annual_salary), '62000')

    def test_give_custom_raise(self):
        """Test that custom raise can be effected also."""
        self.hannah.give_raise(13000)
        self.assertIn(str(self.hannah.annual_salary), '70000')


unittest.main()
