import unittest
from json_mapping_data_sets import get_country_code

class NamesTestCase(unittest.TestCase):
    """Tests for json_mapping_data_sets.py."""

    def test_get_country_code(self):
        """Do codes return two-letter codes?"""
        country_code = get_country_code("United States")
        self.assertEqual(country_code, "us")


print(get_country_code("United States"))