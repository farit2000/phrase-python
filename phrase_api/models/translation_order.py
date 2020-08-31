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


class TranslationOrder(object):
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
        'lsp': 'str',
        'amount_in_cents': 'int',
        'currency': 'str',
        'message': 'str',
        'state': 'str',
        'translation_type': 'str',
        'progress_percent': 'int',
        'source_locale': 'LocalePreview',
        'target_locales': 'list[LocalePreview]',
        'tag': 'str',
        'styleguide': 'StyleguidePreview',
        'unverify_translations_upon_delivery': 'bool',
        'quality': 'bool',
        'priority': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'lsp': 'lsp',
        'amount_in_cents': 'amount_in_cents',
        'currency': 'currency',
        'message': 'message',
        'state': 'state',
        'translation_type': 'translation_type',
        'progress_percent': 'progress_percent',
        'source_locale': 'source_locale',
        'target_locales': 'target_locales',
        'tag': 'tag',
        'styleguide': 'styleguide',
        'unverify_translations_upon_delivery': 'unverify_translations_upon_delivery',
        'quality': 'quality',
        'priority': 'priority',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, lsp=None, amount_in_cents=None, currency=None, message=None, state=None, translation_type=None, progress_percent=None, source_locale=None, target_locales=None, tag=None, styleguide=None, unverify_translations_upon_delivery=None, quality=None, priority=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """TranslationOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._lsp = None
        self._amount_in_cents = None
        self._currency = None
        self._message = None
        self._state = None
        self._translation_type = None
        self._progress_percent = None
        self._source_locale = None
        self._target_locales = None
        self._tag = None
        self._styleguide = None
        self._unverify_translations_upon_delivery = None
        self._quality = None
        self._priority = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if lsp is not None:
            self.lsp = lsp
        if amount_in_cents is not None:
            self.amount_in_cents = amount_in_cents
        if currency is not None:
            self.currency = currency
        if message is not None:
            self.message = message
        if state is not None:
            self.state = state
        if translation_type is not None:
            self.translation_type = translation_type
        if progress_percent is not None:
            self.progress_percent = progress_percent
        if source_locale is not None:
            self.source_locale = source_locale
        if target_locales is not None:
            self.target_locales = target_locales
        if tag is not None:
            self.tag = tag
        if styleguide is not None:
            self.styleguide = styleguide
        if unverify_translations_upon_delivery is not None:
            self.unverify_translations_upon_delivery = unverify_translations_upon_delivery
        if quality is not None:
            self.quality = quality
        if priority is not None:
            self.priority = priority
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TranslationOrder.  # noqa: E501


        :return: The id of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationOrder.


        :param id: The id of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lsp(self):
        """Gets the lsp of this TranslationOrder.  # noqa: E501


        :return: The lsp of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._lsp

    @lsp.setter
    def lsp(self, lsp):
        """Sets the lsp of this TranslationOrder.


        :param lsp: The lsp of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._lsp = lsp

    @property
    def amount_in_cents(self):
        """Gets the amount_in_cents of this TranslationOrder.  # noqa: E501


        :return: The amount_in_cents of this TranslationOrder.  # noqa: E501
        :rtype: int
        """
        return self._amount_in_cents

    @amount_in_cents.setter
    def amount_in_cents(self, amount_in_cents):
        """Sets the amount_in_cents of this TranslationOrder.


        :param amount_in_cents: The amount_in_cents of this TranslationOrder.  # noqa: E501
        :type: int
        """

        self._amount_in_cents = amount_in_cents

    @property
    def currency(self):
        """Gets the currency of this TranslationOrder.  # noqa: E501


        :return: The currency of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TranslationOrder.


        :param currency: The currency of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def message(self):
        """Gets the message of this TranslationOrder.  # noqa: E501


        :return: The message of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TranslationOrder.


        :param message: The message of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def state(self):
        """Gets the state of this TranslationOrder.  # noqa: E501


        :return: The state of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TranslationOrder.


        :param state: The state of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def translation_type(self):
        """Gets the translation_type of this TranslationOrder.  # noqa: E501


        :return: The translation_type of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._translation_type

    @translation_type.setter
    def translation_type(self, translation_type):
        """Sets the translation_type of this TranslationOrder.


        :param translation_type: The translation_type of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._translation_type = translation_type

    @property
    def progress_percent(self):
        """Gets the progress_percent of this TranslationOrder.  # noqa: E501


        :return: The progress_percent of this TranslationOrder.  # noqa: E501
        :rtype: int
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this TranslationOrder.


        :param progress_percent: The progress_percent of this TranslationOrder.  # noqa: E501
        :type: int
        """

        self._progress_percent = progress_percent

    @property
    def source_locale(self):
        """Gets the source_locale of this TranslationOrder.  # noqa: E501


        :return: The source_locale of this TranslationOrder.  # noqa: E501
        :rtype: LocalePreview
        """
        return self._source_locale

    @source_locale.setter
    def source_locale(self, source_locale):
        """Sets the source_locale of this TranslationOrder.


        :param source_locale: The source_locale of this TranslationOrder.  # noqa: E501
        :type: LocalePreview
        """

        self._source_locale = source_locale

    @property
    def target_locales(self):
        """Gets the target_locales of this TranslationOrder.  # noqa: E501


        :return: The target_locales of this TranslationOrder.  # noqa: E501
        :rtype: list[LocalePreview]
        """
        return self._target_locales

    @target_locales.setter
    def target_locales(self, target_locales):
        """Sets the target_locales of this TranslationOrder.


        :param target_locales: The target_locales of this TranslationOrder.  # noqa: E501
        :type: list[LocalePreview]
        """

        self._target_locales = target_locales

    @property
    def tag(self):
        """Gets the tag of this TranslationOrder.  # noqa: E501


        :return: The tag of this TranslationOrder.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this TranslationOrder.


        :param tag: The tag of this TranslationOrder.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def styleguide(self):
        """Gets the styleguide of this TranslationOrder.  # noqa: E501


        :return: The styleguide of this TranslationOrder.  # noqa: E501
        :rtype: StyleguidePreview
        """
        return self._styleguide

    @styleguide.setter
    def styleguide(self, styleguide):
        """Sets the styleguide of this TranslationOrder.


        :param styleguide: The styleguide of this TranslationOrder.  # noqa: E501
        :type: StyleguidePreview
        """

        self._styleguide = styleguide

    @property
    def unverify_translations_upon_delivery(self):
        """Gets the unverify_translations_upon_delivery of this TranslationOrder.  # noqa: E501


        :return: The unverify_translations_upon_delivery of this TranslationOrder.  # noqa: E501
        :rtype: bool
        """
        return self._unverify_translations_upon_delivery

    @unverify_translations_upon_delivery.setter
    def unverify_translations_upon_delivery(self, unverify_translations_upon_delivery):
        """Sets the unverify_translations_upon_delivery of this TranslationOrder.


        :param unverify_translations_upon_delivery: The unverify_translations_upon_delivery of this TranslationOrder.  # noqa: E501
        :type: bool
        """

        self._unverify_translations_upon_delivery = unverify_translations_upon_delivery

    @property
    def quality(self):
        """Gets the quality of this TranslationOrder.  # noqa: E501


        :return: The quality of this TranslationOrder.  # noqa: E501
        :rtype: bool
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this TranslationOrder.


        :param quality: The quality of this TranslationOrder.  # noqa: E501
        :type: bool
        """

        self._quality = quality

    @property
    def priority(self):
        """Gets the priority of this TranslationOrder.  # noqa: E501


        :return: The priority of this TranslationOrder.  # noqa: E501
        :rtype: bool
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TranslationOrder.


        :param priority: The priority of this TranslationOrder.  # noqa: E501
        :type: bool
        """

        self._priority = priority

    @property
    def created_at(self):
        """Gets the created_at of this TranslationOrder.  # noqa: E501


        :return: The created_at of this TranslationOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TranslationOrder.


        :param created_at: The created_at of this TranslationOrder.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TranslationOrder.  # noqa: E501


        :return: The updated_at of this TranslationOrder.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TranslationOrder.


        :param updated_at: The updated_at of this TranslationOrder.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, TranslationOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationOrder):
            return True

        return self.to_dict() != other.to_dict()