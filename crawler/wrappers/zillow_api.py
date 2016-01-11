import os
import xml.etree.cElementTree as xml
import requests
import json
from settings import ROOT_DIR
from .zillow_exceptions import ZillowWrapperException


class ZillowAPI:
    """
    Mothership class for wrapping Zillow API
    """
    root_dir = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))

    def __init__(self, api_key=None):
        """
        dev stage api key is here only for development purposes
        if we'll be sure no one else beside our team will use this class
        then it could stay this way, otherwise we should provide the key
        when instantiating the class and get rid of defaulting non-existent
        key to the one present in zillowkey.txt
        """
        with open(os.path.join(ROOT_DIR, 'crawler/wrappers/zillowkey.txt')) as f:
            dev_stage_api_key = f.read()

        self.api_key = dev_stage_api_key if api_key is None else api_key

    def base_api_call(self, *args):
        pass

