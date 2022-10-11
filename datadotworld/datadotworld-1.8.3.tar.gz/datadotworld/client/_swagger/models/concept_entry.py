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


class ConceptEntry(object):
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
        'alt_label': 'str',
        'iri': 'str',
        'pref_label': 'str'
    }

    attribute_map = {
        'alt_label': 'altLabel',
        'iri': 'iri',
        'pref_label': 'prefLabel'
    }

    def __init__(self, alt_label=None, iri=None, pref_label=None):
        """
        ConceptEntry - a model defined in Swagger
        """

        self._alt_label = None
        self._iri = None
        self._pref_label = None

        if alt_label is not None:
          self.alt_label = alt_label
        if iri is not None:
          self.iri = iri
        if pref_label is not None:
          self.pref_label = pref_label

    @property
    def alt_label(self):
        """
        Gets the alt_label of this ConceptEntry.

        :return: The alt_label of this ConceptEntry.
        :rtype: str
        """
        return self._alt_label

    @alt_label.setter
    def alt_label(self, alt_label):
        """
        Sets the alt_label of this ConceptEntry.

        :param alt_label: The alt_label of this ConceptEntry.
        :type: str
        """

        self._alt_label = alt_label

    @property
    def iri(self):
        """
        Gets the iri of this ConceptEntry.

        :return: The iri of this ConceptEntry.
        :rtype: str
        """
        return self._iri

    @iri.setter
    def iri(self, iri):
        """
        Sets the iri of this ConceptEntry.

        :param iri: The iri of this ConceptEntry.
        :type: str
        """

        self._iri = iri

    @property
    def pref_label(self):
        """
        Gets the pref_label of this ConceptEntry.

        :return: The pref_label of this ConceptEntry.
        :rtype: str
        """
        return self._pref_label

    @pref_label.setter
    def pref_label(self, pref_label):
        """
        Sets the pref_label of this ConceptEntry.

        :param pref_label: The pref_label of this ConceptEntry.
        :type: str
        """

        self._pref_label = pref_label

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
        if not isinstance(other, ConceptEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
