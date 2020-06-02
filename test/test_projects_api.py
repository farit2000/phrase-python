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
from phrase-api.api.projects_api import ProjectsApi  # noqa: E501
from phrase-api.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = phrase-api.api.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_project_create(self):
        """Test case for project_create

        Create a project  # noqa: E501
        """
        pass

    def test_project_delete(self):
        """Test case for project_delete

        Delete a project  # noqa: E501
        """
        pass

    def test_project_show(self):
        """Test case for project_show

        Get a single project  # noqa: E501
        """
        pass

    def test_project_update(self):
        """Test case for project_update

        Update a project  # noqa: E501
        """
        pass

    def test_projects_list(self):
        """Test case for projects_list

        List projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()