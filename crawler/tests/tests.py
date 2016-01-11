import unittest
from crawler.wrappers.zillow_api import ZillowAPI  # this works only if i explicitly import sys
                                                   #  and append my PycharmProjects dir to pythonpath


class ZillowApiTests(unittest.TestCase):

    def setUp(self):
        self.api_key = 'totally_not_valid_api_key'

    def tearDown(self):
        pass

    def test_api_connection(self):
        conn = ZillowAPI(key=self.api_key)  # surely it wont do anything, it's all a mock now

        self.fail('mock test')

if __name__ == '__main__':
    unittest.main()
