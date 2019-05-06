import unittest

import python_repos_for_testing as pr

class PythonReposTestCase(unittest.TestCase):
    """Test for python_repos.py"""

    def setUp(self):
        """Call all the functions here, and test each element separately"""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)


    def test_get_response(self):
        """Test that we got a valid response"""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """Test that we are getting the data we think we are"""
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositories should have required keys
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

    def test_get_names_plot_dicts(self):
        """Test that we plotted the chart for the project"""
        self.assertEqual(len(self.names), 30)
        self.assertEqual(len(self.plot_dicts), 30)

        self.assertLess(len(self.names), 50)

unittest.main()
