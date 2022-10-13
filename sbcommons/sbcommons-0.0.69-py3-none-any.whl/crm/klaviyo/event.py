""" Class representing an event on Klaviyo """
from abc import ABC, abstractmethod
from functools import reduce
from typing import Dict
from typing import List

import pandas as pd


class KlaviyoEvent(ABC):
    """ Base Klaviyo event class"""

    @classmethod
    @property
    @abstractmethod
    def metric_name(cls) -> str:
        """ The name of the metric the event corresponds to. """
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def column_paths(cls):
        """ A dict that maps the path of each event json column to the name of that column. """
        raise NotImplementedError

    @staticmethod
    def get_json_col(json_dict: dict, column_path: str) -> str:
        """ Extracts the element in the json string specified by <column_path>

        Args:
            json_dict: A dict corresponding to the json file.
            column_path: The path to the element we want to extract. E.g. column_path = x.y.z if we
                want to extract value from {x: {y: {z: value}}}.

        """
        return reduce(lambda d, key: d.get(key) if d else None, column_path.split('.'), json_dict)

    @classmethod
    def events_to_df(cls, events_list: List[dict]):
        """ Converts the metric events in events_list to a pandas DataFrame.

        events_list: A list of json files where each json file represents an event.

        Returns:
            A pandas DataFrame with a number of columns extracted from each event specified by
                <column_paths>. For example, for ReceivedKlaviyoEvent we extract the following
                columns: i) campaign_name, customer_id_hash, message_sendtime.
        """
        parsed_events = []
        for event in events_list:
            parsed_event = {}
            for column_path, column_name in cls.column_paths.items():
                column_value = cls.get_json_col(event, column_path)
                if column_value:
                    parsed_event[column_name] = column_value
            parsed_events.append(parsed_event)
        df = pd.DataFrame(parsed_events)
        return df

    @classmethod
    def get_event_class_by_metric_name(cls, metric_name: str):
        """ Gets a KlaviyoEvent object (subclass) given the metric name.

        Args:
            metric_name: The name of the metric.

        Returns:
            A KlaviyoEvent subclass where the metric_name property is equal to the metric_name
            argument passed into this function. E.g. if <metric_name> == 'Received Email',
            the function returns ReceivedKlaviyoEvent.
        """
        for klaviyo_event in KlaviyoEvent.__subclasses__():
            if klaviyo_event.metric_name == metric_name:
                return klaviyo_event


class ReceivedKlaviyoEvent(KlaviyoEvent):
    """ An event corresponding to the received e-mail metric

    Attributes:
        column_paths (Dict[str, str]): A dictionary that maps the path to each column in the json
            to the snake case name of that column.
        metric_name (str): The metric name that corresponds to received e-mail Klaviyo events.
    """

    column_paths = {
        'event_properties.Campaign Name': 'campaign_name',
        'person.customerhashID': 'customer_id_hash',
        'datetime': 'message_sendtime'
    }
    metric_name = 'Received Email'

    def __init__(self, customer_id_hash: str, campaign_name: str, message_sendtime: str):
        super(ReceivedKlaviyoEvent, self).__init__()
        self.customer_id_hash = customer_id_hash
        self.campaign_name = campaign_name
        self.message_sendtime = message_sendtime


class OpenedKlaviyoEvent(KlaviyoEvent):
    """ An event corresponding to the opened e-mail metric

    Attributes:
        column_paths (Dict[str, str]): A dictionary that maps the path to each column in the json
            to the snake case name of that column.
        metric_name (str): The metric name that corresponds to opened e-mail Klaviyo events.
    """

    column_paths = {
        'event_properties.Campaign Name': 'campaign_name',
        'person.customerhashID': 'customer_id_hash',
    }
    metric_name = 'Opened Email'

    def __init__(self, customer_id_hash: str, campaign_name: str):
        super(OpenedKlaviyoEvent, self).__init__()
        self.customer_id_hash = customer_id_hash
        self.campaign_name = campaign_name


class ClickedKlaviyoEvent(KlaviyoEvent):
    """ An event corresponding to the clicked e-mail metric.

    Attributes:
        column_paths (Dict[str, str]): A dictionary that maps the path to each column in the json
            to the snake case name of that column.
        metric_name (str): The metric name that corresponds to clicked e-mail Klaviyo events.
    """

    column_paths = {
        'event_properties.Campaign Name': 'campaign_name',
        'person.customerhashID': 'customer_id_hash',
    }
    metric_name = 'Clicked Email'

    def __init__(self, customer_id_hash: str, campaign_name: str):
        super(ClickedKlaviyoEvent, self).__init__()
        self.customer_id_hash = customer_id_hash
        self.campaign_name = campaign_name
