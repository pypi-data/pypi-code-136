import datetime
from typing import Optional
from urllib.parse import urljoin

from .. import Gender
from ..client import SDKClient, SDKResponse
from pydantic import BaseModel, Field, HttpUrl


class GetClient(BaseModel):
    uuid: str


class Client(BaseModel):
    uuid: str
    phone: str
    last_name: str = Field(alias="lname")
    first_name: str = Field(alias="fname")
    middle_name: Optional[str] = Field(alias="mname", default="")
    birth: datetime.date
    email: Optional[str]
    sex: Gender

    class Config:
        use_enum_values = True


class ClientService:
    def __init__(self, client: SDKClient, url: HttpUrl):
        self._client = client
        self._url = url

    def get_client(
        self, query: GetClient, timeout=3
    ) -> SDKResponse[Client]:
        return self._client.get(
            urljoin(str(self._url), f"mobil/rest/client/{query.uuid}/"),
            Client,
            timeout=timeout,
        )
