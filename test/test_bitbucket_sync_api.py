# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import phrase-api
from phrase-api.api.bitbucket_sync_api import BitbucketSyncApi  # noqa: E501
from phrase-api.rest import ApiException


class TestBitbucketSyncApi(unittest.TestCase):
    """BitbucketSyncApi unit test stubs"""

    def setUp(self):
        self.api = phrase-api.api.bitbucket_sync_api.BitbucketSyncApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bitbucket_sync_export(self):
        """Test case for bitbucket_sync_export

        Export from Phrase to Bitbucket  # noqa: E501
        """
        pass

    def test_bitbucket_sync_import(self):
        """Test case for bitbucket_sync_import

        Import to Phrase from Bitbucket  # noqa: E501
        """
        pass

    def test_bitbucket_syncs_list(self):
        """Test case for bitbucket_syncs_list

        List Bitbucket syncs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()