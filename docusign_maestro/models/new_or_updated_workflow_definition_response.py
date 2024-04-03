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


class NewOrUpdatedWorkflowDefinitionResponse(object):
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
        'is_valid_workflow_definition': 'bool',
        'validation_errors': 'list[ValidationErrors]',
        'workflow_definition': 'WorkflowDefinition',
        'workflow_definition_id': 'str'
    }

    attribute_map = {
        'is_valid_workflow_definition': 'isValidWorkflowDefinition',
        'validation_errors': 'validationErrors',
        'workflow_definition': 'workflowDefinition',
        'workflow_definition_id': 'workflowDefinitionId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """NewOrUpdatedWorkflowDefinitionResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_valid_workflow_definition = None
        self._validation_errors = None
        self._workflow_definition = None
        self._workflow_definition_id = None
        self.discriminator = None

        setattr(self, "_{}".format('is_valid_workflow_definition'), kwargs.get('is_valid_workflow_definition', None))
        setattr(self, "_{}".format('validation_errors'), kwargs.get('validation_errors', None))
        setattr(self, "_{}".format('workflow_definition'), kwargs.get('workflow_definition', None))
        setattr(self, "_{}".format('workflow_definition_id'), kwargs.get('workflow_definition_id', None))

    @property
    def is_valid_workflow_definition(self):
        """Gets the is_valid_workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501


        :return: The is_valid_workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid_workflow_definition

    @is_valid_workflow_definition.setter
    def is_valid_workflow_definition(self, is_valid_workflow_definition):
        """Sets the is_valid_workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.


        :param is_valid_workflow_definition: The is_valid_workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_valid_workflow_definition is None:
            raise ValueError("Invalid value for `is_valid_workflow_definition`, must not be `None`")  # noqa: E501

        self._is_valid_workflow_definition = is_valid_workflow_definition

    @property
    def validation_errors(self):
        """Gets the validation_errors of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501


        :return: The validation_errors of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :rtype: list[ValidationErrors]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this NewOrUpdatedWorkflowDefinitionResponse.


        :param validation_errors: The validation_errors of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :type: list[ValidationErrors]
        """
        if self._configuration.client_side_validation and validation_errors is None:
            raise ValueError("Invalid value for `validation_errors`, must not be `None`")  # noqa: E501

        self._validation_errors = validation_errors

    @property
    def workflow_definition(self):
        """Gets the workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501


        :return: The workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :rtype: WorkflowDefinition
        """
        return self._workflow_definition

    @workflow_definition.setter
    def workflow_definition(self, workflow_definition):
        """Sets the workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.


        :param workflow_definition: The workflow_definition of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :type: WorkflowDefinition
        """
        if self._configuration.client_side_validation and workflow_definition is None:
            raise ValueError("Invalid value for `workflow_definition`, must not be `None`")  # noqa: E501

        self._workflow_definition = workflow_definition

    @property
    def workflow_definition_id(self):
        """Gets the workflow_definition_id of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501


        :return: The workflow_definition_id of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._workflow_definition_id

    @workflow_definition_id.setter
    def workflow_definition_id(self, workflow_definition_id):
        """Sets the workflow_definition_id of this NewOrUpdatedWorkflowDefinitionResponse.


        :param workflow_definition_id: The workflow_definition_id of this NewOrUpdatedWorkflowDefinitionResponse.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and workflow_definition_id is None:
            raise ValueError("Invalid value for `workflow_definition_id`, must not be `None`")  # noqa: E501

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
        if issubclass(NewOrUpdatedWorkflowDefinitionResponse, dict):
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
        if not isinstance(other, NewOrUpdatedWorkflowDefinitionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewOrUpdatedWorkflowDefinitionResponse):
            return True

        return self.to_dict() != other.to_dict()