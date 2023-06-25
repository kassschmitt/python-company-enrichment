import unittest
import os, sys

from python_company_enrichment import AbstractCompanyEnrichment
from dotenv import load_dotenv

load_dotenv()

COMPANY_ENRICHMENT_API_KEY = os.getenv('COMPANY_ENRICHMENT_API_KEY')

class TestAbstractCompanyEnrichment(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestAbstractCompanyEnrichment, self).__init__(*args, **kwargs)

    def test_no_config(self):

        with self.assertRaises(Exception):
            # tests aren't always run in order, so make sure to
            # clear api_key
            AbstractCompanyEnrichment.api_key = None
            AbstractCompanyEnrichment.look_up("airbnb.com")

    def test_config(self):

        AbstractCompanyEnrichment.configure(COMPANY_ENRICHMENT_API_KEY)
        AbstractCompanyEnrichment.look_up("airbnb.com")


if __name__ == '__main__':
    unittest.main()
