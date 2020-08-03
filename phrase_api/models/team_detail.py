# coding: utf-8

"""
    Phrase API Reference

    The version of the OpenAPI document: 2.0.0
    Contact: support@phrase.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from phrase_api.configuration import Configuration


class TeamDetail(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'projects': 'list[Project]',
        'spaces': 'list[Space]',
        'users': 'list[User]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'projects': 'projects',
        'spaces': 'spaces',
        'users': 'users'
    }

    def __init__(self, id=None, name=None, created_at=None, updated_at=None, projects=None, spaces=None, users=None, local_vars_configuration=None):  # noqa: E501
        """TeamDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._projects = None
        self._spaces = None
        self._users = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if projects is not None:
            self.projects = projects
        if spaces is not None:
            self.spaces = spaces
        if users is not None:
            self.users = users

    @property
    def id(self):
        """Gets the id of this TeamDetail.  # noqa: E501


        :return: The id of this TeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TeamDetail.


        :param id: The id of this TeamDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TeamDetail.  # noqa: E501


        :return: The name of this TeamDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamDetail.


        :param name: The name of this TeamDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this TeamDetail.  # noqa: E501


        :return: The created_at of this TeamDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TeamDetail.


        :param created_at: The created_at of this TeamDetail.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TeamDetail.  # noqa: E501


        :return: The updated_at of this TeamDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TeamDetail.


        :param updated_at: The updated_at of this TeamDetail.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def projects(self):
        """Gets the projects of this TeamDetail.  # noqa: E501


        :return: The projects of this TeamDetail.  # noqa: E501
        :rtype: list[Project]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this TeamDetail.


        :param projects: The projects of this TeamDetail.  # noqa: E501
        :type: list[Project]
        """

        self._projects = projects

    @property
    def spaces(self):
        """Gets the spaces of this TeamDetail.  # noqa: E501


        :return: The spaces of this TeamDetail.  # noqa: E501
        :rtype: list[Space]
        """
        return self._spaces

    @spaces.setter
    def spaces(self, spaces):
        """Sets the spaces of this TeamDetail.


        :param spaces: The spaces of this TeamDetail.  # noqa: E501
        :type: list[Space]
        """

        self._spaces = spaces

    @property
    def users(self):
        """Gets the users of this TeamDetail.  # noqa: E501


        :return: The users of this TeamDetail.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this TeamDetail.


        :param users: The users of this TeamDetail.  # noqa: E501
        :type: list[User]
        """

        self._users = users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TeamDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamDetail):
            return True

        return self.to_dict() != other.to_dict()
