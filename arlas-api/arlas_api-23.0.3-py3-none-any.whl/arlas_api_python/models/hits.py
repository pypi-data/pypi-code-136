# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections  # noqa: E501

    OpenAPI spec version: 23.0.1
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Hits(object):
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
        'collection': 'str',
        'hits': 'list[Hit]',
        'nbhits': 'int',
        'totalnb': 'int',
        'links': 'dict(str, Link)'
    }

    attribute_map = {
        'collection': 'collection',
        'hits': 'hits',
        'nbhits': 'nbhits',
        'totalnb': 'totalnb',
        'links': 'links'
    }

    def __init__(self, collection=None, hits=None, nbhits=None, totalnb=None, links=None):  # noqa: E501
        """Hits - a model defined in Swagger"""  # noqa: E501

        self._collection = None
        self._hits = None
        self._nbhits = None
        self._totalnb = None
        self._links = None
        self.discriminator = None

        if collection is not None:
            self.collection = collection
        if hits is not None:
            self.hits = hits
        if nbhits is not None:
            self.nbhits = nbhits
        if totalnb is not None:
            self.totalnb = totalnb
        if links is not None:
            self.links = links

    @property
    def collection(self):
        """Gets the collection of this Hits.  # noqa: E501


        :return: The collection of this Hits.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this Hits.


        :param collection: The collection of this Hits.  # noqa: E501
        :type: str
        """

        self._collection = collection

    @property
    def hits(self):
        """Gets the hits of this Hits.  # noqa: E501


        :return: The hits of this Hits.  # noqa: E501
        :rtype: list[Hit]
        """
        return self._hits

    @hits.setter
    def hits(self, hits):
        """Sets the hits of this Hits.


        :param hits: The hits of this Hits.  # noqa: E501
        :type: list[Hit]
        """

        self._hits = hits

    @property
    def nbhits(self):
        """Gets the nbhits of this Hits.  # noqa: E501


        :return: The nbhits of this Hits.  # noqa: E501
        :rtype: int
        """
        return self._nbhits

    @nbhits.setter
    def nbhits(self, nbhits):
        """Sets the nbhits of this Hits.


        :param nbhits: The nbhits of this Hits.  # noqa: E501
        :type: int
        """

        self._nbhits = nbhits

    @property
    def totalnb(self):
        """Gets the totalnb of this Hits.  # noqa: E501


        :return: The totalnb of this Hits.  # noqa: E501
        :rtype: int
        """
        return self._totalnb

    @totalnb.setter
    def totalnb(self, totalnb):
        """Sets the totalnb of this Hits.


        :param totalnb: The totalnb of this Hits.  # noqa: E501
        :type: int
        """

        self._totalnb = totalnb

    @property
    def links(self):
        """Gets the links of this Hits.  # noqa: E501


        :return: The links of this Hits.  # noqa: E501
        :rtype: dict(str, Link)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Hits.


        :param links: The links of this Hits.  # noqa: E501
        :type: dict(str, Link)
        """

        self._links = links

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
        if issubclass(Hits, dict):
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
        if not isinstance(other, Hits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
