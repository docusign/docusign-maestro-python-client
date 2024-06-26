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


class DSWorkflowLane(object):
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
        'lane_id': 'str',
        'lane_steps': 'list[object]'
    }

    attribute_map = {
        'lane_id': 'laneId',
        'lane_steps': 'laneSteps'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSWorkflowLane - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._lane_id = None
        self._lane_steps = None
        self.discriminator = None

        setattr(self, "_{}".format('lane_id'), kwargs.get('lane_id', None))
        setattr(self, "_{}".format('lane_steps'), kwargs.get('lane_steps', None))

    @property
    def lane_id(self):
        """Gets the lane_id of this DSWorkflowLane.  # noqa: E501


        :return: The lane_id of this DSWorkflowLane.  # noqa: E501
        :rtype: str
        """
        return self._lane_id

    @lane_id.setter
    def lane_id(self, lane_id):
        """Sets the lane_id of this DSWorkflowLane.


        :param lane_id: The lane_id of this DSWorkflowLane.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and lane_id is None:
            raise ValueError("Invalid value for `lane_id`, must not be `None`")  # noqa: E501

        self._lane_id = lane_id

    @property
    def lane_steps(self):
        """Gets the lane_steps of this DSWorkflowLane.  # noqa: E501

        A list of #/definitions/DSWorkflowStep. Each element is: A DS Workflow Step. This object should be any of the following object models: [#/definitions/DSServiceStep, #/definitions/DSTransformationStep, #/definitions/DSDocGenStep, #/definitions/DSSignStep]  # noqa: E501

        :return: The lane_steps of this DSWorkflowLane.  # noqa: E501
        :rtype: list[object]
        """
        return self._lane_steps

    @lane_steps.setter
    def lane_steps(self, lane_steps):
        """Sets the lane_steps of this DSWorkflowLane.

        A list of #/definitions/DSWorkflowStep. Each element is: A DS Workflow Step. This object should be any of the following object models: [#/definitions/DSServiceStep, #/definitions/DSTransformationStep, #/definitions/DSDocGenStep, #/definitions/DSSignStep]  # noqa: E501

        :param lane_steps: The lane_steps of this DSWorkflowLane.  # noqa: E501
        :type: list[object]
        """
        if self._configuration.client_side_validation and lane_steps is None:
            raise ValueError("Invalid value for `lane_steps`, must not be `None`")  # noqa: E501

        self._lane_steps = lane_steps

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
        if issubclass(DSWorkflowLane, dict):
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
        if not isinstance(other, DSWorkflowLane):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSWorkflowLane):
            return True

        return self.to_dict() != other.to_dict()
