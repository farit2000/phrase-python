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
from phrase_api.models.job_template import JobTemplate  # noqa: E501
from phrase_api.rest import ApiException

class TestJobTemplate(unittest.TestCase):
    """JobTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = phrase_api.models.job_template.JobTemplate()  # noqa: E501
        if include_optional :
            return JobTemplate(
                id = '0', 
                name = '0', 
                briefing = '0', 
                project = {"id":"abcd1234cdef1234abcd1234cdef1234","name":"My Android Project","main_format":"xml","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z"}, 
                branch = {"name":"new-branch","created_at":"2015-01-28T09:52:53Z","updated_at":"2015-01-28T09:52:53Z","merged_at":"2015-01-28T09:52:53Z","merged_by":{"id":"abcd1234cdef1234abcd1234cdef1234","username":"joe.doe","name":"Joe Doe"},"created_by":{"id":"abcd1234cdef1234abcd1234cdef1234","username":"joe.doe","name":"Joe Doe"},"state":"success"}, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return JobTemplate(
        )

    def testJobTemplate(self):
        """Test JobTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
