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


class DrivingTestResponeEnquiryTestPart1(object):
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
        'date_of_test': 'str',
        'test_type': 'float',
        'license_class': 'float',
        'test_venue': 'str',
        'result': 'str'
    }

    attribute_map = {
        'date_of_test': 'Date of Test',
        'test_type': 'Test Type',
        'license_class': 'License Class',
        'test_venue': 'Test Venue',
        'result': 'Result'
    }

    def __init__(self, date_of_test=None, test_type=None, license_class=None, test_venue=None, result=None):  # noqa: E501
        """DrivingTestResponeEnquiryTestPart1 - a model defined in Swagger"""  # noqa: E501

        self._date_of_test = None
        self._test_type = None
        self._license_class = None
        self._test_venue = None
        self._result = None
        self.discriminator = None

        if date_of_test is not None:
            self.date_of_test = date_of_test
        if test_type is not None:
            self.test_type = test_type
        if license_class is not None:
            self.license_class = license_class
        if test_venue is not None:
            self.test_venue = test_venue
        if result is not None:
            self.result = result

    @property
    def date_of_test(self):
        """Gets the date_of_test of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501


        :return: The date_of_test of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :rtype: str
        """
        return self._date_of_test

    @date_of_test.setter
    def date_of_test(self, date_of_test):
        """Sets the date_of_test of this DrivingTestResponeEnquiryTestPart1.


        :param date_of_test: The date_of_test of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :type: str
        """

        self._date_of_test = date_of_test

    @property
    def test_type(self):
        """Gets the test_type of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501


        :return: The test_type of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :rtype: float
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this DrivingTestResponeEnquiryTestPart1.


        :param test_type: The test_type of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :type: float
        """

        self._test_type = test_type

    @property
    def license_class(self):
        """Gets the license_class of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501


        :return: The license_class of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :rtype: float
        """
        return self._license_class

    @license_class.setter
    def license_class(self, license_class):
        """Sets the license_class of this DrivingTestResponeEnquiryTestPart1.


        :param license_class: The license_class of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :type: float
        """

        self._license_class = license_class

    @property
    def test_venue(self):
        """Gets the test_venue of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501


        :return: The test_venue of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :rtype: str
        """
        return self._test_venue

    @test_venue.setter
    def test_venue(self, test_venue):
        """Sets the test_venue of this DrivingTestResponeEnquiryTestPart1.


        :param test_venue: The test_venue of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :type: str
        """

        self._test_venue = test_venue

    @property
    def result(self):
        """Gets the result of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501


        :return: The result of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DrivingTestResponeEnquiryTestPart1.


        :param result: The result of this DrivingTestResponeEnquiryTestPart1.  # noqa: E501
        :type: str
        """

        self._result = result

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
        if issubclass(DrivingTestResponeEnquiryTestPart1, dict):
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
        if not isinstance(other, DrivingTestResponeEnquiryTestPart1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
