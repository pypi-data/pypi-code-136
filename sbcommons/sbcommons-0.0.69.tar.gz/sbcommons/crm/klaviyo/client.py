import json
import logging
import time
from typing import Dict, Callable
from typing import List

import requests
from requests.structures import CaseInsensitiveDict

from sbcommons.crm.client import CrmClient
from sbcommons.crm.klaviyo.metric import KlaviyoMetric
from sbcommons.crm.klaviyo.metric import KlaviyoMetricError


class KlaviyoClient(CrmClient):
    """ A client class to interact with Klaviyo's API.

    Attributes:
        token (Dict[str, str]): A Dict with two keys, the PUBLIC_API_KEY and PRIVATE_API_KEY
            required to make requests to Klaviyo. Inherited from CrmClient.
        list_id (int): Identifier of the list to use for pushing/retrieving customers.
        session (requests.Session): The session object for the Klaviyo connection. Inherited from
            CrmClient.
        rate_limit (int): Amounts of second to wait after getting a rate limited error (HTTP 429),
            in order to make a successful request again. Inherited from CrmClient.
        max_rate_limit_retries (int): Number of times to retry making a request if a rate limited
            error occurs (status code 429/Too Many Requests). Inherited from CrmClient.
    """

    _KLAVIYO_IDENTIFY_URL = 'https://a.klaviyo.com/api/identify'
    _KLAVIYO_UNSUBSCRIBE_URL = 'https://a.klaviyo.com/api/v1/people/exclusions'
    _KLAVIYO_TRACK_URL = 'https://a.klaviyo.com/api/track'

    def __init__(self, token: Dict[str, str], list_id: int = None, rate_limit=10,
                 max_rate_limit_retries=2, logger: logging.Logger = None):
        CrmClient.__init__(self, token=token, rate_limit=rate_limit,
                           max_rate_limit_retries=max_rate_limit_retries)
        self.list_id = list_id
        # If logger argument is None, use default logger
        self._logger = logger or logging.getLogger(__name__)

    @property
    def klaviyo_identify_url(self):
        return self._KLAVIYO_IDENTIFY_URL

    @property
    def klaviyo_unsubscribe_url(self):
        return self._KLAVIYO_UNSUBSCRIBE_URL

    @property
    def klaviyo_track_url(self):
        return self._KLAVIYO_TRACK_URL

    @property
    def logger(self) -> logging.Logger:
        """ Returns the logger object to be used by the instance. """
        return self._logger

    def connect(self):
        """ Performs the necessary actions required to be able to make requests to Klaviyo.

        This method is automatically called when this class is used in a context manager i.e. when
        __enter__ is called.
        """
        self.session.mount('https://', self._retry_adapter(retries=3, backoff_factor=4))
        self.session.headers = self._build_base_header()

    def close(self):
        """  Performs necessary actions to terminate the connection with Klaviyo. """
        self.session.close()

    def _build_base_header(self) -> CaseInsensitiveDict:
        return CaseInsensitiveDict({
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def get_public_api_key(self):
        return self.token['PUBLIC_API_KEY']

    def get_private_api_key(self):
        return self.token['PRIVATE_API_KEY']

    def get_public_private_api_key(self):
        return self.get_public_api_key(), self.get_private_api_key()

    def get_events(self, since_ts: str, metric_name: str) -> List[Dict[str, str]]:
        """ Gets all Klaviyo events for <metric_name>, since the specified time <since_ts>.

            Args:
                since_ts: A unix timestamp with the seconds since epoch in UTC.
                metric_name: Name of the Klaviyo metric.

            Returns:
                A list of event dictionaries.

            Raises:
                KlaviyoError if the metric with the specified name is not found.
        """
        # Get id of metric given the name
        metric_id = self.get_metric_id(metric_name=metric_name)

        # Configure URL and URL arguments to get events for <metric_id> since <since_ts>
        url_args = KlaviyoMetric.get_metric_events_url_args(
            since=since_ts, key=self.get_private_api_key()
        )
        url = KlaviyoMetric.get_metric_events_url(metric_id=metric_id)

        # Get all events in batches
        event_list = []
        while True:
            # Get data with Klaviyo client
            res = self._request(method='GET', url=f'{url}?{url_args}').json()
            # Add data to list
            event_list.extend(res['data'])
            # If there are no more pages then break the loop
            if res['next'] is None:
                break
            # Get timestamp for the next page of data we will request
            next_timestamp = res['next'].split('.')[0]
            # Update url args with acquired timestamp for the next call
            url_args = KlaviyoMetric.get_metric_events_url_args(since=next_timestamp,
                                                                key=self.get_private_api_key())
            # Sleep for a bit - Klaviyo allows 350 calls per second before a rate limited error
            time.sleep(0.01)

        return event_list

    def get_metric_id(self, metric_name: str) -> str:
        """ Calls the Klaviyo API to get the metric id given a metric name.

        k_client: KlaviyoClient object for making the call.

        Returns:
            The metric id character string.

        Raises:
            KlaviyoError if the metric with the specified name is not found.
        """
        # Make API call and get metric data
        url_args = KlaviyoMetric.get_metrics_info_url_args(key=self.get_private_api_key())
        url = f'{KlaviyoMetric.metrics_info_url}?{url_args}'
        res = self._request(method='GET', url=url).json()

        # Iterate over data and return correct metric_id
        metric_list = res['data']
        for metric in metric_list:
            if metric['name'] == metric_name:
                return metric['id']

        raise KlaviyoMetricError(f'Metric with name {metric_name} not found.')

    def get_global_exclusions(self, count: int = 500000) -> requests.Response:
        """ Returns global exclusions/unsubscribes.

         Global exclusions are distinct from list exclusions in that these email addresses will not
         receive any emails from any list.

         https://developers.klaviyo.com/en/reference/get-global-exclusions

        Args:
            count: The number of results to return.

        Returns:
            The requests.Response object with the exclusions/unsubscribes.
        """
        url_args = f'reason=unsubscribed&count={count}&api_key={self.get_private_api_key()}'
        url = f'{self.klaviyo_unsubscribe_url}?{url_args}'
        response = self._request(method="GET", url=url)
        return response

    def update_profiles(self, update_data: List[Dict], store: str = 'N/A'):
        """ Updates the profile attributes specified in <update_data>

        Args:
            update_data: A list of dictionaries where each dictionary represents a profile and
                includes the attributes that are going to be updated and their corresponding values.
            store: Store name for which we run the update. This is used for logging failed updates.
        """
        def format_payload_json(record, **kwargs):
            f = {'token': self.get_public_api_key(), 'properties': record}
            data = json.dumps(f, indent=4)
            email = record['$email']
            return email, data

        self._klaviyo_request(update_data, store, url=self._KLAVIYO_IDENTIFY_URL,
                              method=format_payload_json)

    def create_event_in_metric(self, update_data: List[Dict], store: str = 'N/A'):
        """ Updates a Klaviyo metric with event attributes specified in <update_data>

        Args:
            update_data: A list of dictionaries where each dictionary represents a customer's email,
            event name, metric name, token and also includes the attributes that are going to be
            updated and their corresponding values.
            store: Store name for which we run the update. This is used for logging failed updates.
        """
        def format_payload_json(record, **kwargs):
            email = record.pop('customer_email')
            f = {'token': self.get_public_api_key(),
                 'event': record.pop('event_name'),
                 'customer_properties': {'$email': email},
                 'properties': record
                 }
            data = json.dumps(f, indent=4)
            return email, data

        self._klaviyo_request(update_data, store, url=self._KLAVIYO_TRACK_URL,
                              method=format_payload_json)

    def _klaviyo_request(self, update_data: List[Dict], store: str,
                         url: str, method: Callable, **kwargs):
        """ Calls a request.post method

               Args:
                   update_data: A list of dictionaries where each dictionary represents a
                       customer's profile and includes the attributes that are going to
                       be updated and their corresponding values.
                   store: Store name for which we run the update. This is used for logging
                       failed updates.
                   url: endpoint /api url
                   method: a callable function that returns a json formatted str.
               """
        for record in update_data:
            email, data = method(record, **kwargs)
            try:
                self._request(method='POST', url=url, data=data)
                # print(email + ' updated for ' + store)
            except Exception:
                self.logger.exception(f"Failed to update {email} for {store}")
