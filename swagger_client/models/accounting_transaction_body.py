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

class AccountingTransactionBody(object):
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
        'id_year': 'int',
        'label': 'str',
        '_date': 'date',
        'type': 'str',
        'amount': 'float',
        'credit': 'str',
        'debit': 'str',
        'lines': 'list[AccountingtransactionLines]',
        'reference': 'str',
        'linked_users': 'list[int]',
        'linked_transactions': 'list[int]'
    }

    attribute_map = {
        'id_year': 'id_year',
        'label': 'label',
        '_date': 'date',
        'type': 'type',
        'amount': 'amount',
        'credit': 'credit',
        'debit': 'debit',
        'lines': 'lines',
        'reference': 'reference',
        'linked_users': 'linked_users',
        'linked_transactions': 'linked_transactions'
    }

    def __init__(self, id_year=None, label=None, _date=None, type=None, amount=None, credit=None, debit=None, lines=None, reference=None, linked_users=None, linked_transactions=None):  # noqa: E501
        """AccountingTransactionBody - a model defined in Swagger"""  # noqa: E501
        self._id_year = None
        self._label = None
        self.__date = None
        self._type = None
        self._amount = None
        self._credit = None
        self._debit = None
        self._lines = None
        self._reference = None
        self._linked_users = None
        self._linked_transactions = None
        self.discriminator = None
        self.id_year = id_year
        self.label = label
        self._date = _date
        if type is not None:
            self.type = type
        if amount is not None:
            self.amount = amount
        if credit is not None:
            self.credit = credit
        if debit is not None:
            self.debit = debit
        if lines is not None:
            self.lines = lines
        if reference is not None:
            self.reference = reference
        if linked_users is not None:
            self.linked_users = linked_users
        if linked_transactions is not None:
            self.linked_transactions = linked_transactions

    @property
    def id_year(self):
        """Gets the id_year of this AccountingTransactionBody.  # noqa: E501

        ID de l'exercice comptable  # noqa: E501

        :return: The id_year of this AccountingTransactionBody.  # noqa: E501
        :rtype: int
        """
        return self._id_year

    @id_year.setter
    def id_year(self, id_year):
        """Sets the id_year of this AccountingTransactionBody.

        ID de l'exercice comptable  # noqa: E501

        :param id_year: The id_year of this AccountingTransactionBody.  # noqa: E501
        :type: int
        """
        if id_year is None:
            raise ValueError("Invalid value for `id_year`, must not be `None`")  # noqa: E501

        self._id_year = id_year

    @property
    def label(self):
        """Gets the label of this AccountingTransactionBody.  # noqa: E501

        Libellé de la transaction  # noqa: E501

        :return: The label of this AccountingTransactionBody.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AccountingTransactionBody.

        Libellé de la transaction  # noqa: E501

        :param label: The label of this AccountingTransactionBody.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def _date(self):
        """Gets the _date of this AccountingTransactionBody.  # noqa: E501

        Date au format YYYY-MM-DD  # noqa: E501

        :return: The _date of this AccountingTransactionBody.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AccountingTransactionBody.

        Date au format YYYY-MM-DD  # noqa: E501

        :param _date: The _date of this AccountingTransactionBody.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def type(self):
        """Gets the type of this AccountingTransactionBody.  # noqa: E501

        Type de transaction  # noqa: E501

        :return: The type of this AccountingTransactionBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountingTransactionBody.

        Type de transaction  # noqa: E501

        :param type: The type of this AccountingTransactionBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["EXPENSE", "REVENUE", "TRANSFER", "DEBT", "CREDIT", "ADVANCED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this AccountingTransactionBody.  # noqa: E501

        Montant (pour transactions simplifiées)  # noqa: E501

        :return: The amount of this AccountingTransactionBody.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountingTransactionBody.

        Montant (pour transactions simplifiées)  # noqa: E501

        :param amount: The amount of this AccountingTransactionBody.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def credit(self):
        """Gets the credit of this AccountingTransactionBody.  # noqa: E501

        Compte crédité (numéro)  # noqa: E501

        :return: The credit of this AccountingTransactionBody.  # noqa: E501
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this AccountingTransactionBody.

        Compte crédité (numéro)  # noqa: E501

        :param credit: The credit of this AccountingTransactionBody.  # noqa: E501
        :type: str
        """

        self._credit = credit

    @property
    def debit(self):
        """Gets the debit of this AccountingTransactionBody.  # noqa: E501

        Compte débité (numéro)  # noqa: E501

        :return: The debit of this AccountingTransactionBody.  # noqa: E501
        :rtype: str
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this AccountingTransactionBody.

        Compte débité (numéro)  # noqa: E501

        :param debit: The debit of this AccountingTransactionBody.  # noqa: E501
        :type: str
        """

        self._debit = debit

    @property
    def lines(self):
        """Gets the lines of this AccountingTransactionBody.  # noqa: E501

        Lignes comptables (pour ADVANCED)  # noqa: E501

        :return: The lines of this AccountingTransactionBody.  # noqa: E501
        :rtype: list[AccountingtransactionLines]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this AccountingTransactionBody.

        Lignes comptables (pour ADVANCED)  # noqa: E501

        :param lines: The lines of this AccountingTransactionBody.  # noqa: E501
        :type: list[AccountingtransactionLines]
        """

        self._lines = lines

    @property
    def reference(self):
        """Gets the reference of this AccountingTransactionBody.  # noqa: E501

        Numéro de pièce comptable  # noqa: E501

        :return: The reference of this AccountingTransactionBody.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this AccountingTransactionBody.

        Numéro de pièce comptable  # noqa: E501

        :param reference: The reference of this AccountingTransactionBody.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def linked_users(self):
        """Gets the linked_users of this AccountingTransactionBody.  # noqa: E501

        IDs des membres liés (depuis 1.3.3)  # noqa: E501

        :return: The linked_users of this AccountingTransactionBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_users

    @linked_users.setter
    def linked_users(self, linked_users):
        """Sets the linked_users of this AccountingTransactionBody.

        IDs des membres liés (depuis 1.3.3)  # noqa: E501

        :param linked_users: The linked_users of this AccountingTransactionBody.  # noqa: E501
        :type: list[int]
        """

        self._linked_users = linked_users

    @property
    def linked_transactions(self):
        """Gets the linked_transactions of this AccountingTransactionBody.  # noqa: E501

        IDs des transactions liées (depuis 1.3.5)  # noqa: E501

        :return: The linked_transactions of this AccountingTransactionBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_transactions

    @linked_transactions.setter
    def linked_transactions(self, linked_transactions):
        """Sets the linked_transactions of this AccountingTransactionBody.

        IDs des transactions liées (depuis 1.3.5)  # noqa: E501

        :param linked_transactions: The linked_transactions of this AccountingTransactionBody.  # noqa: E501
        :type: list[int]
        """

        self._linked_transactions = linked_transactions

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
        if issubclass(AccountingTransactionBody, dict):
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
        if not isinstance(other, AccountingTransactionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
