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


class DSIdvStep(object):
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
        'config': 'RecordToNever',
        'id': 'str',
        'input': 'DSIdvStepInput',
        'name': 'str',
        'output': 'dict(str, object)',
        'type': 'DSWorkflowStepTypesDSIdv'
    }

    attribute_map = {
        'config': 'config',
        'id': 'id',
        'input': 'input',
        'name': 'name',
        'output': 'output',
        'type': 'type'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSIdvStep - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config = None
        self._id = None
        self._input = None
        self._name = None
        self._output = None
        self._type = None
        self.discriminator = None

        setattr(self, "_{}".format('config'), kwargs.get('config', None))
        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('input'), kwargs.get('input', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('output'), kwargs.get('output', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))

    @property
    def config(self):
        """Gets the config of this DSIdvStep.  # noqa: E501


        :return: The config of this DSIdvStep.  # noqa: E501
        :rtype: RecordToNever
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this DSIdvStep.


        :param config: The config of this DSIdvStep.  # noqa: E501
        :type: RecordToNever
        """
        if self._configuration.client_side_validation and config is None:
            raise ValueError("Invalid value for `config`, must not be `None`")  # noqa: E501

        self._config = config

    @property
    def id(self):
        """Gets the id of this DSIdvStep.  # noqa: E501


        :return: The id of this DSIdvStep.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DSIdvStep.


        :param id: The id of this DSIdvStep.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def input(self):
        """Gets the input of this DSIdvStep.  # noqa: E501


        :return: The input of this DSIdvStep.  # noqa: E501
        :rtype: DSIdvStepInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this DSIdvStep.


        :param input: The input of this DSIdvStep.  # noqa: E501
        :type: DSIdvStepInput
        """
        if self._configuration.client_side_validation and input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")  # noqa: E501

        self._input = input

    @property
    def name(self):
        """Gets the name of this DSIdvStep.  # noqa: E501


        :return: The name of this DSIdvStep.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DSIdvStep.


        :param name: The name of this DSIdvStep.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def output(self):
        """Gets the output of this DSIdvStep.  # noqa: E501

        A Record of strings to Strings, Variables, or Transformation Expressions  # noqa: E501

        :return: The output of this DSIdvStep.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this DSIdvStep.

        A Record of strings to Strings, Variables, or Transformation Expressions  # noqa: E501

        :param output: The output of this DSIdvStep.  # noqa: E501
        :type: dict(str, object)
        """
        if self._configuration.client_side_validation and output is None:
            raise ValueError("Invalid value for `output`, must not be `None`")  # noqa: E501

        self._output = output

    @property
    def type(self):
        """Gets the type of this DSIdvStep.  # noqa: E501


        :return: The type of this DSIdvStep.  # noqa: E501
        :rtype: DSWorkflowStepTypesDSIdv
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DSIdvStep.


        :param type: The type of this DSIdvStep.  # noqa: E501
        :type: DSWorkflowStepTypesDSIdv
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(DSIdvStep, dict):
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
        if not isinstance(other, DSIdvStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSIdvStep):
            return True

        return self.to_dict() != other.to_dict()
