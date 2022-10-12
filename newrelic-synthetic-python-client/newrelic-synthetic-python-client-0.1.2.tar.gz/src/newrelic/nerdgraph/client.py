from dataclasses import dataclass
import abc
import pathlib
import json
from typing import Dict

from requests import Response, Session

from newrelic.utils.log import log


@dataclass
class NerdGraphConfig:
    endpoint: str = ""
    api_key: str = ""
    account_id: str = ""

    @classmethod
    def from_json_file(cls, filepath: pathlib.Path) -> "NerdGraphConfig":
        return cls(**json.loads(filepath.read_text()))

    def to_dict(self) -> Dict:
        return {
            "endpoint": self.endpoint,
            "api_key": self.api_key,
            "account_id": self.account_id
        }


class NerdGraphClient:
    def __init__(
        self,
        config: NerdGraphConfig,
        session: Session = Session()
    ) -> None:
        self.session = session
        self.config = config
        self.account_id = self.config.account_id
        self.headers = {
            "API-Key": self.config.api_key
        }

    def request(self, ql: str) -> Response:
        log.trace(f"{ql=}")
        return self.session.post(
            self.config.endpoint,
            json={"query": ql},
            headers=self.headers
        )


class NewRelicModule(abc.ABC):
    def __init__(self, client: NerdGraphClient) -> None:
        self.client = client
