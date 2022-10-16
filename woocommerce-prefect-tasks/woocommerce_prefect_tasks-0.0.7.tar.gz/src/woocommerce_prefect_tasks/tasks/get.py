from ..api import Api

from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs

from typing import Any


class Get(Task):
    def __init__(self, aws_secret_name: str = None, aws_secret_region: str = None, event: dict = None, **kwargs: Any):
        self.aws_secret_region = aws_secret_region
        self.aws_secret_name = aws_secret_name
        self.event = event
        super().__init__(**kwargs)

    @defaults_from_attrs("event", "aws_secret_region", "aws_secret_name")
    def run(self, aws_secret_name: str = None, aws_secret_region: str = None, event: dict = None) -> dict:

        if not event:
            raise ValueError('An event must be provided.')

        try:
            wc_api = Api(aws_secret_name=aws_secret_name, aws_secret_region=aws_secret_region)
            resource = wc_api.api_client.get(endpoint=event.get('endpoint', None),
                                             **event.get('kwargs', None) or dict())

        except Exception as e:
            print(e)
            raise e

        return resource.json()
