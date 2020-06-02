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

import phrase-api
from phrase-api.models.bitbucket_sync_export_parameters import BitbucketSyncExportParameters  # noqa: E501
from phrase-api.rest import ApiException

class TestBitbucketSyncExportParameters(unittest.TestCase):
    """BitbucketSyncExportParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BitbucketSyncExportParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.bitbucket_sync_export_parameters.BitbucketSyncExportParameters()  # noqa: E501
        if include_optional :
            return BitbucketSyncExportParameters(
                account_id = 'abcd1234'
            )
        else :
            return BitbucketSyncExportParameters(
        )

    def testBitbucketSyncExportParameters(self):
        """Test BitbucketSyncExportParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()