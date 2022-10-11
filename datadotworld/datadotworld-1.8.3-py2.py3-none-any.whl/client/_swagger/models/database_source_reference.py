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


class DatabaseSourceReference(object):
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
        'owner': 'str',
        'id': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'id': 'id'
    }

    def __init__(self, owner=None, id=None):
        """
        DatabaseSourceReference - a model defined in Swagger
        """

        self._owner = None
        self._id = None

        if owner is not None:
          self.owner = owner
        if id is not None:
          self.id = id

    @property
    def owner(self):
        """
        Gets the owner of this DatabaseSourceReference.
        Owner Agent

        :return: The owner of this DatabaseSourceReference.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DatabaseSourceReference.
        Owner Agent

        :param owner: The owner of this DatabaseSourceReference.
        :type: str
        """
        if owner is not None and len(owner) > 128:
            raise ValueError("Invalid value for `owner`, length must be less than or equal to `128`")
        if owner is not None and len(owner) < 1:
            raise ValueError("Invalid value for `owner`, length must be greater than or equal to `1`")
        if owner is not None and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9]){1,29}[a-z0-9]', owner):
            raise ValueError("Invalid value for `owner`, must be a follow pattern or equal to `/[a-z0-9](?:-(?!-)|[a-z0-9]){1,29}[a-z0-9]/`")

        self._owner = owner

    @property
    def id(self):
        """
        Gets the id of this DatabaseSourceReference.
        data.world database connection identifier 

        :return: The id of this DatabaseSourceReference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseSourceReference.
        data.world database connection identifier 

        :param id: The id of this DatabaseSourceReference.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, DatabaseSourceReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
