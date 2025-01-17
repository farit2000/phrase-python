# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase_api
from phrase_api.api.search_api import SearchApi  # noqa: E501
from phrase_api.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_in_account(self):
        """Test case for search_in_account

        Search across projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
