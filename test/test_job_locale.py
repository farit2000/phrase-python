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
from phrase-api.models.job_locale import JobLocale  # noqa: E501
from phrase-api.rest import ApiException

class TestJobLocale(unittest.TestCase):
    """JobLocale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobLocale
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase-api.models.job_locale.JobLocale()  # noqa: E501
        if include_optional :
            return JobLocale(
                id = '0', 
                job = phrase-api.models.job_preview.job_preview(
                    id = '0', 
                    name = '0', 
                    state = '0', ), 
                locale = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"English","code":"en-GB"}, 
                users = [
                    phrase-api.models.user_preview.user_preview(
                        id = '0', 
                        username = '0', 
                        name = '0', )
                    ]
            )
        else :
            return JobLocale(
        )

    def testJobLocale(self):
        """Test JobLocale"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()