# coding: utf-8

"""
    Maestro API

    Maestro authors and executes experiences that allow non-coders the ability to define Simple Business Process without having to write code and to deploy them seamlessly without having to have development expertise  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_maestro.client.configuration import Configuration


class DSWorkflowVariableFromVariable(object):
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
        'key': 'str',
        'property_name': 'str',
        'source': 'DSWorkflowVariableSourceTypesVariable',
        'step_id': 'str'
    }

    attribute_map = {
        'key': 'key',
        'property_name': 'propertyName',
        'source': 'source',
        'step_id': 'stepId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSWorkflowVariableFromVariable - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key = None
        self._property_name = None
        self._source = None
        self._step_id = None
        self.discriminator = None

        setattr(self, "_{}".format('key'), kwargs.get('key', None))
        setattr(self, "_{}".format('property_name'), kwargs.get('property_name', None))
        setattr(self, "_{}".format('source'), kwargs.get('source', None))
        setattr(self, "_{}".format('step_id'), kwargs.get('step_id', None))

    @property
    def key(self):
        """Gets the key of this DSWorkflowVariableFromVariable.  # noqa: E501


        :return: The key of this DSWorkflowVariableFromVariable.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DSWorkflowVariableFromVariable.


        :param key: The key of this DSWorkflowVariableFromVariable.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def property_name(self):
        """Gets the property_name of this DSWorkflowVariableFromVariable.  # noqa: E501


        :return: The property_name of this DSWorkflowVariableFromVariable.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this DSWorkflowVariableFromVariable.


        :param property_name: The property_name of this DSWorkflowVariableFromVariable.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and property_name is None:
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501

        self._property_name = property_name

    @property
    def source(self):
        """Gets the source of this DSWorkflowVariableFromVariable.  # noqa: E501


        :return: The source of this DSWorkflowVariableFromVariable.  # noqa: E501
        :rtype: DSWorkflowVariableSourceTypesVariable
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DSWorkflowVariableFromVariable.


        :param source: The source of this DSWorkflowVariableFromVariable.  # noqa: E501
        :type: DSWorkflowVariableSourceTypesVariable
        """
        if self._configuration.client_side_validation and source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def step_id(self):
        """Gets the step_id of this DSWorkflowVariableFromVariable.  # noqa: E501


        :return: The step_id of this DSWorkflowVariableFromVariable.  # noqa: E501
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """Sets the step_id of this DSWorkflowVariableFromVariable.


        :param step_id: The step_id of this DSWorkflowVariableFromVariable.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and step_id is None:
            raise ValueError("Invalid value for `step_id`, must not be `None`")  # noqa: E501

        self._step_id = step_id

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
        if issubclass(DSWorkflowVariableFromVariable, dict):
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
        if not isinstance(other, DSWorkflowVariableFromVariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSWorkflowVariableFromVariable):
            return True

        return self.to_dict() != other.to_dict()
