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


class DSSignStepInput(object):
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
        'documents': 'list[object]',
        'email_blurb': 'object',
        'email_subject': 'object',
        'is_embedded_sign': 'bool',
        'signers': 'list[ESignSigner]'
    }

    attribute_map = {
        'documents': 'documents',
        'email_blurb': 'emailBlurb',
        'email_subject': 'emailSubject',
        'is_embedded_sign': 'isEmbeddedSign',
        'signers': 'signers'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSSignStepInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._documents = None
        self._email_blurb = None
        self._email_subject = None
        self._is_embedded_sign = None
        self._signers = None
        self.discriminator = None

        setattr(self, "_{}".format('documents'), kwargs.get('documents', None))
        setattr(self, "_{}".format('email_blurb'), kwargs.get('email_blurb', None))
        setattr(self, "_{}".format('email_subject'), kwargs.get('email_subject', None))
        setattr(self, "_{}".format('is_embedded_sign'), kwargs.get('is_embedded_sign', None))
        setattr(self, "_{}".format('signers'), kwargs.get('signers', None))

    @property
    def documents(self):
        """Gets the documents of this DSSignStepInput.  # noqa: E501

        A list of #/definitions/ESignDocuments. Each element is: ESignDocument Object. This object should be any of the following object models: [#/definitions/ESignDocumentFromPreviousStep, #/definitions/ESignDocumentFromESignTemplate]  # noqa: E501

        :return: The documents of this DSSignStepInput.  # noqa: E501
        :rtype: list[object]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this DSSignStepInput.

        A list of #/definitions/ESignDocuments. Each element is: ESignDocument Object. This object should be any of the following object models: [#/definitions/ESignDocumentFromPreviousStep, #/definitions/ESignDocumentFromESignTemplate]  # noqa: E501

        :param documents: The documents of this DSSignStepInput.  # noqa: E501
        :type: list[object]
        """
        if self._configuration.client_side_validation and documents is None:
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def email_blurb(self):
        """Gets the email_blurb of this DSSignStepInput.  # noqa: E501

        Reference of #/definitions/StringOrVariableOrTransformation. Object stands for a String or a Variable or a Transformation. This object should be any of the following object models or types: [string, #/definitions/DSWorkflowVariable, #/definitions/DSWorkflowTransformationExpression]  # noqa: E501

        :return: The email_blurb of this DSSignStepInput.  # noqa: E501
        :rtype: object
        """
        return self._email_blurb

    @email_blurb.setter
    def email_blurb(self, email_blurb):
        """Sets the email_blurb of this DSSignStepInput.

        Reference of #/definitions/StringOrVariableOrTransformation. Object stands for a String or a Variable or a Transformation. This object should be any of the following object models or types: [string, #/definitions/DSWorkflowVariable, #/definitions/DSWorkflowTransformationExpression]  # noqa: E501

        :param email_blurb: The email_blurb of this DSSignStepInput.  # noqa: E501
        :type: object
        """

        self._email_blurb = email_blurb

    @property
    def email_subject(self):
        """Gets the email_subject of this DSSignStepInput.  # noqa: E501

        Reference of #/definitions/StringOrVariableOrTransformation. Object stands for a String or a Variable or a Transformation. This object should be any of the following object models or types: [string, #/definitions/DSWorkflowVariable, #/definitions/DSWorkflowTransformationExpression]  # noqa: E501

        :return: The email_subject of this DSSignStepInput.  # noqa: E501
        :rtype: object
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this DSSignStepInput.

        Reference of #/definitions/StringOrVariableOrTransformation. Object stands for a String or a Variable or a Transformation. This object should be any of the following object models or types: [string, #/definitions/DSWorkflowVariable, #/definitions/DSWorkflowTransformationExpression]  # noqa: E501

        :param email_subject: The email_subject of this DSSignStepInput.  # noqa: E501
        :type: object
        """

        self._email_subject = email_subject

    @property
    def is_embedded_sign(self):
        """Gets the is_embedded_sign of this DSSignStepInput.  # noqa: E501


        :return: The is_embedded_sign of this DSSignStepInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_embedded_sign

    @is_embedded_sign.setter
    def is_embedded_sign(self, is_embedded_sign):
        """Sets the is_embedded_sign of this DSSignStepInput.


        :param is_embedded_sign: The is_embedded_sign of this DSSignStepInput.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_embedded_sign is None:
            raise ValueError("Invalid value for `is_embedded_sign`, must not be `None`")  # noqa: E501

        self._is_embedded_sign = is_embedded_sign

    @property
    def signers(self):
        """Gets the signers of this DSSignStepInput.  # noqa: E501


        :return: The signers of this DSSignStepInput.  # noqa: E501
        :rtype: list[ESignSigner]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this DSSignStepInput.


        :param signers: The signers of this DSSignStepInput.  # noqa: E501
        :type: list[ESignSigner]
        """
        if self._configuration.client_side_validation and signers is None:
            raise ValueError("Invalid value for `signers`, must not be `None`")  # noqa: E501

        self._signers = signers

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
        if issubclass(DSSignStepInput, dict):
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
        if not isinstance(other, DSSignStepInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSSignStepInput):
            return True

        return self.to_dict() != other.to_dict()
