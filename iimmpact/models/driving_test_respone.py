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


class DrivingTestRespone(object):
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
        'enquiry_test_part_1': 'list[DrivingTestResponeEnquiryTestPart1]',
        'enquiry_practical_test': 'list[DrivingTestResponeEnquiryTestPart1]'
    }

    attribute_map = {
        'enquiry_test_part_1': 'Enquiry Test Part 1',
        'enquiry_practical_test': 'Enquiry Practical Test'
    }

    def __init__(self, enquiry_test_part_1=None, enquiry_practical_test=None):  # noqa: E501
        """DrivingTestRespone - a model defined in Swagger"""  # noqa: E501

        self._enquiry_test_part_1 = None
        self._enquiry_practical_test = None
        self.discriminator = None

        if enquiry_test_part_1 is not None:
            self.enquiry_test_part_1 = enquiry_test_part_1
        if enquiry_practical_test is not None:
            self.enquiry_practical_test = enquiry_practical_test

    @property
    def enquiry_test_part_1(self):
        """Gets the enquiry_test_part_1 of this DrivingTestRespone.  # noqa: E501


        :return: The enquiry_test_part_1 of this DrivingTestRespone.  # noqa: E501
        :rtype: list[DrivingTestResponeEnquiryTestPart1]
        """
        return self._enquiry_test_part_1

    @enquiry_test_part_1.setter
    def enquiry_test_part_1(self, enquiry_test_part_1):
        """Sets the enquiry_test_part_1 of this DrivingTestRespone.


        :param enquiry_test_part_1: The enquiry_test_part_1 of this DrivingTestRespone.  # noqa: E501
        :type: list[DrivingTestResponeEnquiryTestPart1]
        """

        self._enquiry_test_part_1 = enquiry_test_part_1

    @property
    def enquiry_practical_test(self):
        """Gets the enquiry_practical_test of this DrivingTestRespone.  # noqa: E501


        :return: The enquiry_practical_test of this DrivingTestRespone.  # noqa: E501
        :rtype: list[DrivingTestResponeEnquiryTestPart1]
        """
        return self._enquiry_practical_test

    @enquiry_practical_test.setter
    def enquiry_practical_test(self, enquiry_practical_test):
        """Sets the enquiry_practical_test of this DrivingTestRespone.


        :param enquiry_practical_test: The enquiry_practical_test of this DrivingTestRespone.  # noqa: E501
        :type: list[DrivingTestResponeEnquiryTestPart1]
        """

        self._enquiry_practical_test = enquiry_practical_test

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
        if issubclass(DrivingTestRespone, dict):
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
        if not isinstance(other, DrivingTestRespone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
