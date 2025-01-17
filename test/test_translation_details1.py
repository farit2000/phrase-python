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
from phrase_api.models.translation_details1 import TranslationDetails1  # noqa: E501
from phrase_api.rest import ApiException

class TestTranslationDetails1(unittest.TestCase):
    """TranslationDetails1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TranslationDetails1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.translation_details1.TranslationDetails1()  # noqa: E501
        if include_optional :
            return TranslationDetails1(
                user = phrase_api.models.user_preview.user_preview(
                    id = '0', 
                    username = '0', 
                    name = '0', 
                    gravatar_uid = '0', ), 
                word_count = 56
            )
        else :
            return TranslationDetails1(
        )

    def testTranslationDetails1(self):
        """Test TranslationDetails1"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
