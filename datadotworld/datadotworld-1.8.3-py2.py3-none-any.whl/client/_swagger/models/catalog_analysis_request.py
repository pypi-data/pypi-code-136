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


class CatalogAnalysisRequest(object):
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
        'collections': 'list[str]',
        'title': 'str',
        'type_label': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'properties': 'dict(str, JsonNode)'
    }

    attribute_map = {
        'collections': 'collections',
        'title': 'title',
        'type_label': 'typeLabel',
        'description': 'description',
        'tags': 'tags',
        'properties': 'properties'
    }

    def __init__(self, collections=None, title=None, type_label=None, description=None, tags=None, properties=None):
        """
        CatalogAnalysisRequest - a model defined in Swagger
        """

        self._collections = None
        self._title = None
        self._type_label = None
        self._description = None
        self._tags = None
        self._properties = None

        if collections is not None:
          self.collections = collections
        if title is not None:
          self.title = title
        if type_label is not None:
          self.type_label = type_label
        if description is not None:
          self.description = description
        if tags is not None:
          self.tags = tags
        if properties is not None:
          self.properties = properties

    @property
    def collections(self):
        """
        Gets the collections of this CatalogAnalysisRequest.
        Catalog Collection to which this metadata resource is added. Required for POST and PUT.Available catalog collection can be discovered via appropriate discovery endpoints.

        :return: The collections of this CatalogAnalysisRequest.
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """
        Sets the collections of this CatalogAnalysisRequest.
        Catalog Collection to which this metadata resource is added. Required for POST and PUT.Available catalog collection can be discovered via appropriate discovery endpoints.

        :param collections: The collections of this CatalogAnalysisRequest.
        :type: list[str]
        """

        self._collections = collections

    @property
    def title(self):
        """
        Gets the title of this CatalogAnalysisRequest.
        Title of the metadata resource. Required for POST and PUT.

        :return: The title of this CatalogAnalysisRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CatalogAnalysisRequest.
        Title of the metadata resource. Required for POST and PUT.

        :param title: The title of this CatalogAnalysisRequest.
        :type: str
        """
        if title is not None and len(title) > 60:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `60`")
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")

        self._title = title

    @property
    def type_label(self):
        """
        Gets the type_label of this CatalogAnalysisRequest.
        Indicates the type of metadata resource. Some examples of valid values are Report, Tableau dashboard, Glossary, Table, Database view etc. Default values will be assumed if not provided. Defaults to Report for analysis resources, Glossary for Glossary resources, Table for Table resources and Column for Column resources. Once specified during creation, this cannot be changed via PATCH. Only a PUT can change the type 

        :return: The type_label of this CatalogAnalysisRequest.
        :rtype: str
        """
        return self._type_label

    @type_label.setter
    def type_label(self, type_label):
        """
        Sets the type_label of this CatalogAnalysisRequest.
        Indicates the type of metadata resource. Some examples of valid values are Report, Tableau dashboard, Glossary, Table, Database view etc. Default values will be assumed if not provided. Defaults to Report for analysis resources, Glossary for Glossary resources, Table for Table resources and Column for Column resources. Once specified during creation, this cannot be changed via PATCH. Only a PUT can change the type 

        :param type_label: The type_label of this CatalogAnalysisRequest.
        :type: str
        """

        self._type_label = type_label

    @property
    def description(self):
        """
        Gets the description of this CatalogAnalysisRequest.
        A short, but descriptive statement about the metadata resource.

        :return: The description of this CatalogAnalysisRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CatalogAnalysisRequest.
        A short, but descriptive statement about the metadata resource.

        :param description: The description of this CatalogAnalysisRequest.
        :type: str
        """
        if description is not None and len(description) > 120:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `120`")
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")

        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this CatalogAnalysisRequest.
        A collection of tags to identify the relevance of metadata resource. Tags with no spaces is defacto standard

        :return: The tags of this CatalogAnalysisRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CatalogAnalysisRequest.
        A collection of tags to identify the relevance of metadata resource. Tags with no spaces is defacto standard

        :param tags: The tags of this CatalogAnalysisRequest.
        :type: list[str]
        """

        self._tags = tags

    @property
    def properties(self):
        """
        Gets the properties of this CatalogAnalysisRequest.
        Custom properties for the metadata resource mapped to API BindingsCan be simple name-value string pairs or nested values for a string name. See examples for details.

        :return: The properties of this CatalogAnalysisRequest.
        :rtype: dict(str, JsonNode)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CatalogAnalysisRequest.
        Custom properties for the metadata resource mapped to API BindingsCan be simple name-value string pairs or nested values for a string name. See examples for details.

        :param properties: The properties of this CatalogAnalysisRequest.
        :type: dict(str, JsonNode)
        """

        self._properties = properties

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
        if not isinstance(other, CatalogAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
