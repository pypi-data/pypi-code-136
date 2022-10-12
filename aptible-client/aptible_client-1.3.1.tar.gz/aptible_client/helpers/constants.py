import os

AUTH_API_URL = os.getenv("AUTH_API_URL", "https://auth.aptible.com")
CLOUD_API_URL = os.getenv("CLOUD_API_URL", "https://cloud-api.cloud.aptible.com")
ORGANIZATION_ID = os.getenv("ORGANIZATION_ID")
ENVIRONMENT_ID = os.getenv("ENVIRONMENT_ID")

ASSET_DELIMITER = "__"
