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


class DeployRequest(object):
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
        'deployment_status': 'DeployStatus'
    }

    attribute_map = {
        'deployment_status': 'deploymentStatus'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DeployRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deployment_status = None
        self.discriminator = None

        setattr(self, "_{}".format('deployment_status'), kwargs.get('deployment_status', None))

    @property
    def deployment_status(self):
        """Gets the deployment_status of this DeployRequest.  # noqa: E501


        :return: The deployment_status of this DeployRequest.  # noqa: E501
        :rtype: DeployStatus
        """
        return self._deployment_status

    @deployment_status.setter
    def deployment_status(self, deployment_status):
        """Sets the deployment_status of this DeployRequest.


        :param deployment_status: The deployment_status of this DeployRequest.  # noqa: E501
        :type: DeployStatus
        """
        if self._configuration.client_side_validation and deployment_status is None:
            raise ValueError("Invalid value for `deployment_status`, must not be `None`")  # noqa: E501

        self._deployment_status = deployment_status

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
        if issubclass(DeployRequest, dict):
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
        if not isinstance(other, DeployRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeployRequest):
            return True

        return self.to_dict() != other.to_dict()