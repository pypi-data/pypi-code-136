import os

from pydantic import BaseModel


class Environment(BaseModel):
    postgres_url: str
    s3_endpoint_url: str | None
    s3_access_key_id: str
    s3_secret_access_key: str


def detect(key: str):
    key = key.upper()

    return Environment(
        postgres_url=os.environ[f"DATAPAC_ENV_{key}_POSTGRES_URI"],
        s3_endpoint_url=os.environ.get(f"DATAPAC_ENV_{key}_S3_ENDPOINT_URL", None),
        s3_access_key_id=os.environ[f"DATAPAC_ENV_{key}_S3_ACCESS_KEY_ID"],
        s3_secret_access_key=os.environ[f"DATAPAC_ENV_{key}_S3_SECRET_ACCESS_KEY"],
    )
