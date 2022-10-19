from typing import Optional

from pydantic import BaseSettings, Field, HttpUrl


class Settings(BaseSettings):
    api_key: Optional[str] = Field(default=None, env="YELP_API_KEY")
    base_url: HttpUrl = "https://api.yelp.com/v3"

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"}
