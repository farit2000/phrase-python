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


class Branch(object):
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
        'base_project_id': 'str',
        'branch_project_id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'merged_at': 'datetime',
        'merged_by': 'UserPreview',
        'created_by': 'UserPreview',
        'state': 'str'
    }

    attribute_map = {
        'base_project_id': 'base_project_id',
        'branch_project_id': 'branch_project_id',
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'merged_at': 'merged_at',
        'merged_by': 'merged_by',
        'created_by': 'created_by',
        'state': 'state'
    }

    def __init__(self, base_project_id=None, branch_project_id=None, name=None, created_at=None, updated_at=None, merged_at=None, merged_by=None, created_by=None, state=None, local_vars_configuration=None):  # noqa: E501
        """Branch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_project_id = None
        self._branch_project_id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._merged_at = None
        self._merged_by = None
        self._created_by = None
        self._state = None
        self.discriminator = None

        if base_project_id is not None:
            self.base_project_id = base_project_id
        if branch_project_id is not None:
            self.branch_project_id = branch_project_id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if merged_at is not None:
            self.merged_at = merged_at
        if merged_by is not None:
            self.merged_by = merged_by
        if created_by is not None:
            self.created_by = created_by
        if state is not None:
            self.state = state

    @property
    def base_project_id(self):
        """Gets the base_project_id of this Branch.  # noqa: E501


        :return: The base_project_id of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._base_project_id

    @base_project_id.setter
    def base_project_id(self, base_project_id):
        """Sets the base_project_id of this Branch.


        :param base_project_id: The base_project_id of this Branch.  # noqa: E501
        :type: str
        """

        self._base_project_id = base_project_id

    @property
    def branch_project_id(self):
        """Gets the branch_project_id of this Branch.  # noqa: E501


        :return: The branch_project_id of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._branch_project_id

    @branch_project_id.setter
    def branch_project_id(self, branch_project_id):
        """Sets the branch_project_id of this Branch.


        :param branch_project_id: The branch_project_id of this Branch.  # noqa: E501
        :type: str
        """

        self._branch_project_id = branch_project_id

    @property
    def name(self):
        """Gets the name of this Branch.  # noqa: E501


        :return: The name of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Branch.


        :param name: The name of this Branch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Branch.  # noqa: E501


        :return: The created_at of this Branch.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Branch.


        :param created_at: The created_at of this Branch.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Branch.  # noqa: E501


        :return: The updated_at of this Branch.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Branch.


        :param updated_at: The updated_at of this Branch.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def merged_at(self):
        """Gets the merged_at of this Branch.  # noqa: E501


        :return: The merged_at of this Branch.  # noqa: E501
        :rtype: datetime
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        """Sets the merged_at of this Branch.


        :param merged_at: The merged_at of this Branch.  # noqa: E501
        :type: datetime
        """

        self._merged_at = merged_at

    @property
    def merged_by(self):
        """Gets the merged_by of this Branch.  # noqa: E501


        :return: The merged_by of this Branch.  # noqa: E501
        :rtype: UserPreview
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        """Sets the merged_by of this Branch.


        :param merged_by: The merged_by of this Branch.  # noqa: E501
        :type: UserPreview
        """

        self._merged_by = merged_by

    @property
    def created_by(self):
        """Gets the created_by of this Branch.  # noqa: E501


        :return: The created_by of this Branch.  # noqa: E501
        :rtype: UserPreview
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Branch.


        :param created_by: The created_by of this Branch.  # noqa: E501
        :type: UserPreview
        """

        self._created_by = created_by

    @property
    def state(self):
        """Gets the state of this Branch.  # noqa: E501


        :return: The state of this Branch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Branch.


        :param state: The state of this Branch.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if not isinstance(other, Branch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Branch):
            return True

        return self.to_dict() != other.to_dict()
