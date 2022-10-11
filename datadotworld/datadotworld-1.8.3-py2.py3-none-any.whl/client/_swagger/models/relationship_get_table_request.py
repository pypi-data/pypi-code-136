# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RelationshipGetTableRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'by_resource_types': 'list[str]',
        'by_relation_types': 'list[str]'
    }

    attribute_map = {
        'by_resource_types': 'byResourceTypes',
        'by_relation_types': 'byRelationTypes'
    }

    def __init__(self, by_resource_types=None, by_relation_types=None):
        """
        RelationshipGetTableRequest - a model defined in Swagger
        """

        self._by_resource_types = None
        self._by_relation_types = None

        if by_resource_types is not None:
          self.by_resource_types = by_resource_types
        if by_relation_types is not None:
          self.by_relation_types = by_relation_types

    @property
    def by_resource_types(self):
        """
        Gets the by_resource_types of this RelationshipGetTableRequest.

        :return: The by_resource_types of this RelationshipGetTableRequest.
        :rtype: list[str]
        """
        return self._by_resource_types

    @by_resource_types.setter
    def by_resource_types(self, by_resource_types):
        """
        Sets the by_resource_types of this RelationshipGetTableRequest.

        :param by_resource_types: The by_resource_types of this RelationshipGetTableRequest.
        :type: list[str]
        """
        allowed_values = ["CATALOG", "ANALYSIS", "BUSINESS_TERM", "COLUMN", "DATA_TYPE", "DATASET", "PROJECT", "TABLE"]
        if not set(by_resource_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `by_resource_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(by_resource_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._by_resource_types = by_resource_types

    @property
    def by_relation_types(self):
        """
        Gets the by_relation_types of this RelationshipGetTableRequest.

        :return: The by_relation_types of this RelationshipGetTableRequest.
        :rtype: list[str]
        """
        return self._by_relation_types

    @by_relation_types.setter
    def by_relation_types(self, by_relation_types):
        """
        Sets the by_relation_types of this RelationshipGetTableRequest.

        :param by_relation_types: The by_relation_types of this RelationshipGetTableRequest.
        :type: list[str]
        """

        self._by_relation_types = by_relation_types

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RelationshipGetTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
