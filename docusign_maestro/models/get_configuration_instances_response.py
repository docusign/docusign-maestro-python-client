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


class GetConfigurationInstancesResponse(object):
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
        'config_instances': 'list[GetConfigurationInstancesResponseConfigInstances]',
        'count': 'float',
        'workflow_definition_id': 'str'
    }

    attribute_map = {
        'config_instances': 'configInstances',
        'count': 'count',
        'workflow_definition_id': 'workflowDefinitionId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """GetConfigurationInstancesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_instances = None
        self._count = None
        self._workflow_definition_id = None
        self.discriminator = None

        setattr(self, "_{}".format('config_instances'), kwargs.get('config_instances', None))
        setattr(self, "_{}".format('count'), kwargs.get('count', None))
        setattr(self, "_{}".format('workflow_definition_id'), kwargs.get('workflow_definition_id', None))

    @property
    def config_instances(self):
        """Gets the config_instances of this GetConfigurationInstancesResponse.  # noqa: E501


        :return: The config_instances of this GetConfigurationInstancesResponse.  # noqa: E501
        :rtype: list[GetConfigurationInstancesResponseConfigInstances]
        """
        return self._config_instances

    @config_instances.setter
    def config_instances(self, config_instances):
        """Sets the config_instances of this GetConfigurationInstancesResponse.


        :param config_instances: The config_instances of this GetConfigurationInstancesResponse.  # noqa: E501
        :type: list[GetConfigurationInstancesResponseConfigInstances]
        """

        self._config_instances = config_instances

    @property
    def count(self):
        """Gets the count of this GetConfigurationInstancesResponse.  # noqa: E501


        :return: The count of this GetConfigurationInstancesResponse.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this GetConfigurationInstancesResponse.


        :param count: The count of this GetConfigurationInstancesResponse.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def workflow_definition_id(self):
        """Gets the workflow_definition_id of this GetConfigurationInstancesResponse.  # noqa: E501


        :return: The workflow_definition_id of this GetConfigurationInstancesResponse.  # noqa: E501
        :rtype: str
        """
        return self._workflow_definition_id

    @workflow_definition_id.setter
    def workflow_definition_id(self, workflow_definition_id):
        """Sets the workflow_definition_id of this GetConfigurationInstancesResponse.


        :param workflow_definition_id: The workflow_definition_id of this GetConfigurationInstancesResponse.  # noqa: E501
        :type: str
        """

        self._workflow_definition_id = workflow_definition_id

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
        if issubclass(GetConfigurationInstancesResponse, dict):
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
        if not isinstance(other, GetConfigurationInstancesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetConfigurationInstancesResponse):
            return True

        return self.to_dict() != other.to_dict()