import os
import unittest
from crawler.wrappers.zillow_api import ZillowAPI
from settings import ROOT_DIR


class ZillowApiTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_key_is_defaulted_to_dev_when_not_provided(self):
        zillow = ZillowAPI()

        with open(os.path.join(ROOT_DIR, 'crawler/wrappers/zillowkey.txt')) as f:
            dev_stage_api_key = f.read()

        assert zillow.api_key == dev_stage_api_key

    def test_key_is_correct_when_provided(self):
        zillow = ZillowAPI(api_key='humptydumptyhadagreatfall')

        assert zillow.api_key == 'humptydumptyhadagreatfall'


if __name__ == '__main__':
    unittest.main()
