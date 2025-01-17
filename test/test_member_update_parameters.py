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
from phrase_api.models.member_update_parameters import MemberUpdateParameters  # noqa: E501
from phrase_api.rest import ApiException

class TestMemberUpdateParameters(unittest.TestCase):
    """MemberUpdateParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MemberUpdateParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.member_update_parameters.MemberUpdateParameters()  # noqa: E501
        if include_optional :
            return MemberUpdateParameters(
                strategy = 'set', 
                role = 'Developer', 
                project_ids = 'abcd1234abcd1234abcd1234,abcd1234abcd1234abcd1235', 
                locale_ids = 'abcd1234abcd1234abcd1234,abcd1234abcd1234abcd1235', 
                default_locale_codes = ["en","fi"], 
                space_ids = ["abcd1234abcd1234abcd1234","abcd1234abcd1234abcd1235"], 
                permissions = {"create_upload":true,"review_translations":true}
            )
        else :
            return MemberUpdateParameters(
        )

    def testMemberUpdateParameters(self):
        """Test MemberUpdateParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
