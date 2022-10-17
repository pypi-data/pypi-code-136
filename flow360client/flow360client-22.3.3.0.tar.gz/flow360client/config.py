import os
from dataclasses import dataclass


@dataclass
class WebConfig:
    AWS_REGION: str
    FLOW360_WEB_API_ENDPONT: str
    PORTAL_API_ENDPONT: str
    # auth info
    auth = None
    user = None

    # other
    auth_retry = 0


ProdConfig = WebConfig(
    AWS_REGION="us-gov-west-1",
    FLOW360_WEB_API_ENDPONT="https://flow360-api.simulation.cloud",
    PORTAL_API_ENDPONT="https://portal-api.simulation.cloud"
)

DevConfig = WebConfig(
    AWS_REGION="us-east-1",
    FLOW360_WEB_API_ENDPONT="https://flow360-api.dev-simulation.cloud",
    PORTAL_API_ENDPONT="https://portal-api.dev-simulation.cloud"
)

UatConfig = WebConfig(
    AWS_REGION="us-gov-west-1",
    FLOW360_WEB_API_ENDPONT="https://uat-flow360-api.simulation.cloud",
    PORTAL_API_ENDPONT="https://uat-portal-api.simulation.cloud"
)

Config = ProdConfig

if os.getenv("FLOW360_ENV") == "dev":
    Config = DevConfig

if os.getenv("FLOW360_ENV") == "uat":
    Config = UatConfig