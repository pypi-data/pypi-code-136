"""Context manager for XRTC: login and set/get API."""
from requests import Session

from xrtc import (
    LoginCredentials,
    ConnectionConfiguration,
    ReceivedError,
    GetItemRequest,
    SetItemRequest,
    ReceivedData,
)


class XRTC:
    """Context manager for XRTC: login and set/get API."""

    def __init__(self, env_file_credentials: str = None, env_file_connection: str = None):
        """Initialize connection and credentials."""

        # Get credentials from .env file
        self._login_credentials = LoginCredentials(_env_file=env_file_credentials)

        # Set connection configuration
        self._connection_configuration = ConnectionConfiguration(_env_file=env_file_connection)

        # Requests session
        self._session = None

    def __enter__(self):
        """Open requests connection and login."""
        self._session = Session()

        login_response = self._session.post(
            self._connection_configuration.login_url,
            data=self._login_credentials.json(),
        )

        if login_response.status_code != 200:
            if login_response.status_code in (400, 401):
                raise Exception(
                    f"XRTC: Login failed: {ReceivedError.parse_raw(login_response.content).error.errormessage}"
                )

            raise Exception(f"XRTC: Login failed. Code: {login_response.status_code}")

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Close requests connection."""
        self._session.close()

    def set_item(self, items: list[dict]):
        """Wrapper for set item endpoint"""

        # Parse request parameters
        request_parameters = SetItemRequest(items=items)

        # Make request
        set_item_response = self._session.post(
            self._connection_configuration.set_url, data=request_parameters.json()
        )

        # Parse errors, if any
        if set_item_response.status_code != 200:
            if set_item_response.status_code in (400, 401):
                raise Exception(
                    f"XRTC: Set item failed: {ReceivedError.parse_raw(set_item_response.content).error.errormessage}"
                )

            raise Exception(f"XRTC: Set item failed. Code: {set_item_response.status_code}")

    def get_item(self, portals: list[dict] = None) -> ReceivedData:
        """Wrapper for get item endpoint"""

        # Parse request parameters
        request_parameters = GetItemRequest(portals=portals)

        # Make request
        get_item_response = self._session.post(
            self._connection_configuration.get_url, data=request_parameters.json()
        )

        if get_item_response.status_code != 200:
            if get_item_response.status_code in (400, 401):
                raise Exception(
                    f"XRTC: Get item failed: {ReceivedError.parse_raw(get_item_response.content).error.errormessage}"
                )

            raise Exception(f"XRTC: Get item failed. Code: {get_item_response.status_code}")

        return ReceivedData.parse_raw(get_item_response.content)
