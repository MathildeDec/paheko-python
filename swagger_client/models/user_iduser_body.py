# coding: utf-8

"""
    Paheko API

    Documentation Swagger pour l'API de Paheko  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserIDUSERBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'email': 'str',
        'id_category': 'int'
    }

    attribute_map = {
        'email': 'email',
        'id_category': 'id_category'
    }

    def __init__(self, email=None, id_category=None):  # noqa: E501
        """UserIDUSERBody - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._id_category = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if id_category is not None:
            self.id_category = id_category

    @property
    def email(self):
        """Gets the email of this UserIDUSERBody.  # noqa: E501


        :return: The email of this UserIDUSERBody.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserIDUSERBody.


        :param email: The email of this UserIDUSERBody.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id_category(self):
        """Gets the id_category of this UserIDUSERBody.  # noqa: E501


        :return: The id_category of this UserIDUSERBody.  # noqa: E501
        :rtype: int
        """
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        """Sets the id_category of this UserIDUSERBody.


        :param id_category: The id_category of this UserIDUSERBody.  # noqa: E501
        :type: int
        """

        self._id_category = id_category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserIDUSERBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserIDUSERBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
