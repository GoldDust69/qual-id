import unittest
from qual_id.categories.sports import Sports
from test.utils.category_helper import CategoryHelper


class TestSports(unittest.TestCase):
    def setUp(self):
        self.sports = Sports()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.sports)
        self.assertTrue(error_message == "", error_message)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
