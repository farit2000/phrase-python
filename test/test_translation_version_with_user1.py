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
from phrase_api.models.translation_version_with_user1 import TranslationVersionWithUser1  # noqa: E501
from phrase_api.rest import ApiException

class TestTranslationVersionWithUser1(unittest.TestCase):
    """TranslationVersionWithUser1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationVersionWithUser1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.translation_version_with_user1.TranslationVersionWithUser1()  # noqa: E501
        if include_optional :
            return TranslationVersionWithUser1(
                user = phrase_api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', 
                    gravatar_uid = '0', )
            )
        else :
            return TranslationVersionWithUser1(
        )

    def testTranslationVersionWithUser1(self):
        """Test TranslationVersionWithUser1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
