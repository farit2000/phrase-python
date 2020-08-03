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
from phrase_api.api.teams_api import TeamsApi  # noqa: E501
from phrase_api.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = phrase_api.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_team_create(self):
        """Test case for team_create

        Create a Team  # noqa: E501
        """
        pass

    def test_team_delete(self):
        """Test case for team_delete

        Delete Team  # noqa: E501
        """
        pass

    def test_team_show(self):
        """Test case for team_show

        Get Team  # noqa: E501
        """
        pass

    def test_team_update(self):
        """Test case for team_update

        Update Team  # noqa: E501
        """
        pass

    def test_teams_list(self):
        """Test case for teams_list

        List Teams  # noqa: E501
        """
        pass

    def test_teams_projects_create(self):
        """Test case for teams_projects_create

        Add Project  # noqa: E501
        """
        pass

    def test_teams_projects_delete(self):
        """Test case for teams_projects_delete

        Remove Project  # noqa: E501
        """
        pass

    def test_teams_spaces_create(self):
        """Test case for teams_spaces_create

        Add Space  # noqa: E501
        """
        pass

    def test_teams_spaces_delete(self):
        """Test case for teams_spaces_delete

        Remove Space  # noqa: E501
        """
        pass

    def test_teams_users_create(self):
        """Test case for teams_users_create

        Add User  # noqa: E501
        """
        pass

    def test_teams_users_delete(self):
        """Test case for teams_users_delete

        Remove User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
