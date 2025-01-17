# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import phrase_api
from phrase_api.models.search_in_account_parameters import SearchInAccountParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestSearchInAccountParameters(unittest.TestCase):
    """SearchInAccountParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SearchInAccountParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.search_in_account_parameters.SearchInAccountParameters()  # noqa: E501
        if include_optional :
            return SearchInAccountParameters(
                query = 'keyword', 
                locale_code = 'de_DE', 
                page = 1, 
                per_page = 25
            )
        else :
            return SearchInAccountParameters(
        )

    def testSearchInAccountParameters(self):
        """Test SearchInAccountParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
