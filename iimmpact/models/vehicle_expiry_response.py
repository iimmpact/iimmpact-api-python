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


class VehicleExpiryResponse(object):
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
        'vehicle_plate_number': 'str',
        'date_of_commencement': 'str',
        'expiry_date': 'str',
        'insurance_expiry_date': 'str'
    }

    attribute_map = {
        'vehicle_plate_number': 'Vehicle Plate Number',
        'date_of_commencement': 'Date of Commencement',
        'expiry_date': 'Expiry Date',
        'insurance_expiry_date': 'Insurance Expiry Date'
    }

    def __init__(self, vehicle_plate_number=None, date_of_commencement=None, expiry_date=None, insurance_expiry_date=None):  # noqa: E501
        """VehicleExpiryResponse - a model defined in Swagger"""  # noqa: E501

        self._vehicle_plate_number = None
        self._date_of_commencement = None
        self._expiry_date = None
        self._insurance_expiry_date = None
        self.discriminator = None

        if vehicle_plate_number is not None:
            self.vehicle_plate_number = vehicle_plate_number
        if date_of_commencement is not None:
            self.date_of_commencement = date_of_commencement
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if insurance_expiry_date is not None:
            self.insurance_expiry_date = insurance_expiry_date

    @property
    def vehicle_plate_number(self):
        """Gets the vehicle_plate_number of this VehicleExpiryResponse.  # noqa: E501


        :return: The vehicle_plate_number of this VehicleExpiryResponse.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_plate_number

    @vehicle_plate_number.setter
    def vehicle_plate_number(self, vehicle_plate_number):
        """Sets the vehicle_plate_number of this VehicleExpiryResponse.


        :param vehicle_plate_number: The vehicle_plate_number of this VehicleExpiryResponse.  # noqa: E501
        :type: str
        """

        self._vehicle_plate_number = vehicle_plate_number

    @property
    def date_of_commencement(self):
        """Gets the date_of_commencement of this VehicleExpiryResponse.  # noqa: E501


        :return: The date_of_commencement of this VehicleExpiryResponse.  # noqa: E501
        :rtype: str
        """
        return self._date_of_commencement

    @date_of_commencement.setter
    def date_of_commencement(self, date_of_commencement):
        """Sets the date_of_commencement of this VehicleExpiryResponse.


        :param date_of_commencement: The date_of_commencement of this VehicleExpiryResponse.  # noqa: E501
        :type: str
        """

        self._date_of_commencement = date_of_commencement

    @property
    def expiry_date(self):
        """Gets the expiry_date of this VehicleExpiryResponse.  # noqa: E501


        :return: The expiry_date of this VehicleExpiryResponse.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this VehicleExpiryResponse.


        :param expiry_date: The expiry_date of this VehicleExpiryResponse.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def insurance_expiry_date(self):
        """Gets the insurance_expiry_date of this VehicleExpiryResponse.  # noqa: E501


        :return: The insurance_expiry_date of this VehicleExpiryResponse.  # noqa: E501
        :rtype: str
        """
        return self._insurance_expiry_date

    @insurance_expiry_date.setter
    def insurance_expiry_date(self, insurance_expiry_date):
        """Sets the insurance_expiry_date of this VehicleExpiryResponse.


        :param insurance_expiry_date: The insurance_expiry_date of this VehicleExpiryResponse.  # noqa: E501
        :type: str
        """

        self._insurance_expiry_date = insurance_expiry_date

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
        if issubclass(VehicleExpiryResponse, dict):
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
        if not isinstance(other, VehicleExpiryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other