from dataclasses import dataclass


@dataclass
class NearRpcConfig:
    provider_url: str


@dataclass
class NearConfig(NearRpcConfig):
    account_id: str
    private_key: str
    sbt_contract: str
