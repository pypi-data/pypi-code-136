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


class EditActivitiesResultDto(object):
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
        'activity_batch_id': 'str',
        'time_started': 'Instant',
        'time_ended': 'Instant',
        'activity_results': 'list[str]'
    }

    attribute_map = {
        'activity_batch_id': 'activityBatchId',
        'time_started': 'timeStarted',
        'time_ended': 'timeEnded',
        'activity_results': 'activityResults'
    }

    def __init__(self, activity_batch_id=None, time_started=None, time_ended=None, activity_results=None):
        """
        EditActivitiesResultDto - a model defined in Swagger
        """

        self._activity_batch_id = None
        self._time_started = None
        self._time_ended = None
        self._activity_results = None

        if activity_batch_id is not None:
          self.activity_batch_id = activity_batch_id
        if time_started is not None:
          self.time_started = time_started
        if time_ended is not None:
          self.time_ended = time_ended
        if activity_results is not None:
          self.activity_results = activity_results

    @property
    def activity_batch_id(self):
        """
        Gets the activity_batch_id of this EditActivitiesResultDto.

        :return: The activity_batch_id of this EditActivitiesResultDto.
        :rtype: str
        """
        return self._activity_batch_id

    @activity_batch_id.setter
    def activity_batch_id(self, activity_batch_id):
        """
        Sets the activity_batch_id of this EditActivitiesResultDto.

        :param activity_batch_id: The activity_batch_id of this EditActivitiesResultDto.
        :type: str
        """

        self._activity_batch_id = activity_batch_id

    @property
    def time_started(self):
        """
        Gets the time_started of this EditActivitiesResultDto.

        :return: The time_started of this EditActivitiesResultDto.
        :rtype: Instant
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this EditActivitiesResultDto.

        :param time_started: The time_started of this EditActivitiesResultDto.
        :type: Instant
        """

        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this EditActivitiesResultDto.

        :return: The time_ended of this EditActivitiesResultDto.
        :rtype: Instant
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this EditActivitiesResultDto.

        :param time_ended: The time_ended of this EditActivitiesResultDto.
        :type: Instant
        """

        self._time_ended = time_ended

    @property
    def activity_results(self):
        """
        Gets the activity_results of this EditActivitiesResultDto.

        :return: The activity_results of this EditActivitiesResultDto.
        :rtype: list[str]
        """
        return self._activity_results

    @activity_results.setter
    def activity_results(self, activity_results):
        """
        Sets the activity_results of this EditActivitiesResultDto.

        :param activity_results: The activity_results of this EditActivitiesResultDto.
        :type: list[str]
        """

        self._activity_results = activity_results

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
        if not isinstance(other, EditActivitiesResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
