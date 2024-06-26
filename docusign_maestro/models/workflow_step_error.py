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


class WorkflowStepError(object):
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
        'code': 'str',
        'end_time': 'datetime',
        'error': 'WorkflowStepErrorError',
        'name': 'str',
        'start_time': 'datetime'
    }

    attribute_map = {
        'code': 'code',
        'end_time': 'endTime',
        'error': 'error',
        'name': 'name',
        'start_time': 'startTime'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """WorkflowStepError - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code = None
        self._end_time = None
        self._error = None
        self._name = None
        self._start_time = None
        self.discriminator = None

        setattr(self, "_{}".format('code'), kwargs.get('code', None))
        setattr(self, "_{}".format('end_time'), kwargs.get('end_time', None))
        setattr(self, "_{}".format('error'), kwargs.get('error', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('start_time'), kwargs.get('start_time', None))

    @property
    def code(self):
        """Gets the code of this WorkflowStepError.  # noqa: E501

        Error code message  # noqa: E501

        :return: The code of this WorkflowStepError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WorkflowStepError.

        Error code message  # noqa: E501

        :param code: The code of this WorkflowStepError.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def end_time(self):
        """Gets the end_time of this WorkflowStepError.  # noqa: E501

        Track the End time of the error retry/processed  # noqa: E501

        :return: The end_time of this WorkflowStepError.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WorkflowStepError.

        Track the End time of the error retry/processed  # noqa: E501

        :param end_time: The end_time of this WorkflowStepError.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def error(self):
        """Gets the error of this WorkflowStepError.  # noqa: E501


        :return: The error of this WorkflowStepError.  # noqa: E501
        :rtype: WorkflowStepErrorError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this WorkflowStepError.


        :param error: The error of this WorkflowStepError.  # noqa: E501
        :type: WorkflowStepErrorError
        """

        self._error = error

    @property
    def name(self):
        """Gets the name of this WorkflowStepError.  # noqa: E501

        The workflow step name where the error occurred  # noqa: E501

        :return: The name of this WorkflowStepError.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowStepError.

        The workflow step name where the error occurred  # noqa: E501

        :param name: The name of this WorkflowStepError.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def start_time(self):
        """Gets the start_time of this WorkflowStepError.  # noqa: E501

        Track Start time of the error occurred  # noqa: E501

        :return: The start_time of this WorkflowStepError.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WorkflowStepError.

        Track Start time of the error occurred  # noqa: E501

        :param start_time: The start_time of this WorkflowStepError.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

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
        if issubclass(WorkflowStepError, dict):
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
        if not isinstance(other, WorkflowStepError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowStepError):
            return True

        return self.to_dict() != other.to_dict()
