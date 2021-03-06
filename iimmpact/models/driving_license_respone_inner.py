# coding: utf-8

"""
    IIMMPACT API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-09-14T13:01:14Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DrivingLicenseResponeInner(object):
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
        'type_of_driving_license': 'str',
        'date_of_commencement': 'str',
        'expiry_date': 'str'
    }

    attribute_map = {
        'type_of_driving_license': 'Type of Driving License',
        'date_of_commencement': 'Date of Commencement',
        'expiry_date': 'Expiry Date'
    }

    def __init__(self, type_of_driving_license=None, date_of_commencement=None, expiry_date=None):  # noqa: E501
        """DrivingLicenseResponeInner - a model defined in Swagger"""  # noqa: E501

        self._type_of_driving_license = None
        self._date_of_commencement = None
        self._expiry_date = None
        self.discriminator = None

        if type_of_driving_license is not None:
            self.type_of_driving_license = type_of_driving_license
        if date_of_commencement is not None:
            self.date_of_commencement = date_of_commencement
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def type_of_driving_license(self):
        """Gets the type_of_driving_license of this DrivingLicenseResponeInner.  # noqa: E501


        :return: The type_of_driving_license of this DrivingLicenseResponeInner.  # noqa: E501
        :rtype: str
        """
        return self._type_of_driving_license

    @type_of_driving_license.setter
    def type_of_driving_license(self, type_of_driving_license):
        """Sets the type_of_driving_license of this DrivingLicenseResponeInner.


        :param type_of_driving_license: The type_of_driving_license of this DrivingLicenseResponeInner.  # noqa: E501
        :type: str
        """

        self._type_of_driving_license = type_of_driving_license

    @property
    def date_of_commencement(self):
        """Gets the date_of_commencement of this DrivingLicenseResponeInner.  # noqa: E501


        :return: The date_of_commencement of this DrivingLicenseResponeInner.  # noqa: E501
        :rtype: str
        """
        return self._date_of_commencement

    @date_of_commencement.setter
    def date_of_commencement(self, date_of_commencement):
        """Sets the date_of_commencement of this DrivingLicenseResponeInner.


        :param date_of_commencement: The date_of_commencement of this DrivingLicenseResponeInner.  # noqa: E501
        :type: str
        """

        self._date_of_commencement = date_of_commencement

    @property
    def expiry_date(self):
        """Gets the expiry_date of this DrivingLicenseResponeInner.  # noqa: E501


        :return: The expiry_date of this DrivingLicenseResponeInner.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this DrivingLicenseResponeInner.


        :param expiry_date: The expiry_date of this DrivingLicenseResponeInner.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

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
        if issubclass(DrivingLicenseResponeInner, dict):
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
        if not isinstance(other, DrivingLicenseResponeInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
