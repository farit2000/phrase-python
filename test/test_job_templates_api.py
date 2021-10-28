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
from phrase_api.api.job_templates_api import JobTemplatesApi  # noqa: E501
from phrase_api.rest import ApiException


class TestJobTemplatesApi(unittest.TestCase):
    """JobTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.job_templates_api.JobTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_job_template_create(self):
        """Test case for job_template_create

        Create a job template  # noqa: E501
        """
        pass

    def test_job_template_delete(self):
        """Test case for job_template_delete

        Delete a job template  # noqa: E501
        """
        pass

    def test_job_template_show(self):
        """Test case for job_template_show

        Get a single job template  # noqa: E501
        """
        pass

    def test_job_template_update(self):
        """Test case for job_template_update

        Update a job template  # noqa: E501
        """
        pass

    def test_job_templates_list(self):
        """Test case for job_templates_list

        List job templates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()