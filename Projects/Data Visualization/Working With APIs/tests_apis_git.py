import unittest
import requests
from working_with_apis_git import get_conf_code
from working_with_apis_git import get_repo_dicts


class NamesTestCase(unittest.TestCase):
    """Tests for working_with_apis_git.py."""

    def test_get_conf_code(self):
        """Do URLs return valid confirmation codes?"""
        confirmation_code = get_conf_code('https://api.github.com/search/repositories?q=language:javascript&sort=stars')
        self.assertEqual(confirmation_code, 'Status code: 200')

    def test_get_repo_dicts(self):
        """Do URLs return a valid number of repositories?"""
        repo_conf = get_repo_dicts('https://api.github.com/search/repositories?q=language:javascript&sort=stars')
        self.assertGreater(repo_conf, f"Total repositories: {11}")
