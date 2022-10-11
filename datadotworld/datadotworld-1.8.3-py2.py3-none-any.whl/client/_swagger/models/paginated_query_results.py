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


class PaginatedQueryResults(object):
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
        'count': 'int',
        'next_page_token': 'str',
        'records': 'list[QuerySummaryResponse]'
    }

    attribute_map = {
        'count': 'count',
        'next_page_token': 'nextPageToken',
        'records': 'records'
    }

    def __init__(self, count=None, next_page_token=None, records=None):
        """
        PaginatedQueryResults - a model defined in Swagger
        """

        self._count = None
        self._next_page_token = None
        self._records = None

        self.count = count
        if next_page_token is not None:
          self.next_page_token = next_page_token
        self.records = records

    @property
    def count(self):
        """
        Gets the count of this PaginatedQueryResults.

        :return: The count of this PaginatedQueryResults.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PaginatedQueryResults.

        :param count: The count of this PaginatedQueryResults.
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")
        if count is not None and count < 0:
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")

        self._count = count

    @property
    def next_page_token(self):
        """
        Gets the next_page_token of this PaginatedQueryResults.

        :return: The next_page_token of this PaginatedQueryResults.
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """
        Sets the next_page_token of this PaginatedQueryResults.

        :param next_page_token: The next_page_token of this PaginatedQueryResults.
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def records(self):
        """
        Gets the records of this PaginatedQueryResults.

        :return: The records of this PaginatedQueryResults.
        :rtype: list[QuerySummaryResponse]
        """
        return self._records

    @records.setter
    def records(self, records):
        """
        Sets the records of this PaginatedQueryResults.

        :param records: The records of this PaginatedQueryResults.
        :type: list[QuerySummaryResponse]
        """
        if records is None:
            raise ValueError("Invalid value for `records`, must not be `None`")

        self._records = records

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
        if not isinstance(other, PaginatedQueryResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
