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


class Distribution(object):
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
        'project': 'ProjectShort',
        'platforms': 'list[str]',
        'locales': 'list[LocalePreview]',
        'releases': 'list[ReleasePreview]',
        'created_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project': 'project',
        'platforms': 'platforms',
        'locales': 'locales',
        'releases': 'releases',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at'
    }

    def __init__(self, id=None, name=None, project=None, platforms=None, locales=None, releases=None, created_at=None, deleted_at=None, local_vars_configuration=None):  # noqa: E501
        """Distribution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._project = None
        self._platforms = None
        self._locales = None
        self._releases = None
        self._created_at = None
        self._deleted_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if platforms is not None:
            self.platforms = platforms
        if locales is not None:
            self.locales = locales
        if releases is not None:
            self.releases = releases
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def id(self):
        """Gets the id of this Distribution.  # noqa: E501


        :return: The id of this Distribution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Distribution.


        :param id: The id of this Distribution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Distribution.  # noqa: E501


        :return: The name of this Distribution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Distribution.


        :param name: The name of this Distribution.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this Distribution.  # noqa: E501


        :return: The project of this Distribution.  # noqa: E501
        :rtype: ProjectShort
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Distribution.


        :param project: The project of this Distribution.  # noqa: E501
        :type: ProjectShort
        """

        self._project = project

    @property
    def platforms(self):
        """Gets the platforms of this Distribution.  # noqa: E501


        :return: The platforms of this Distribution.  # noqa: E501
        :rtype: list[str]
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this Distribution.


        :param platforms: The platforms of this Distribution.  # noqa: E501
        :type: list[str]
        """

        self._platforms = platforms

    @property
    def locales(self):
        """Gets the locales of this Distribution.  # noqa: E501


        :return: The locales of this Distribution.  # noqa: E501
        :rtype: list[LocalePreview]
        """
        return self._locales

    @locales.setter
    def locales(self, locales):
        """Sets the locales of this Distribution.


        :param locales: The locales of this Distribution.  # noqa: E501
        :type: list[LocalePreview]
        """

        self._locales = locales

    @property
    def releases(self):
        """Gets the releases of this Distribution.  # noqa: E501


        :return: The releases of this Distribution.  # noqa: E501
        :rtype: list[ReleasePreview]
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this Distribution.


        :param releases: The releases of this Distribution.  # noqa: E501
        :type: list[ReleasePreview]
        """

        self._releases = releases

    @property
    def created_at(self):
        """Gets the created_at of this Distribution.  # noqa: E501


        :return: The created_at of this Distribution.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Distribution.


        :param created_at: The created_at of this Distribution.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Distribution.  # noqa: E501


        :return: The deleted_at of this Distribution.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Distribution.


        :param deleted_at: The deleted_at of this Distribution.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if not isinstance(other, Distribution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Distribution):
            return True

        return self.to_dict() != other.to_dict()
