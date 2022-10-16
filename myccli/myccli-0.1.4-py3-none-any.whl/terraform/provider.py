import os
from dataclasses import dataclass
from typing import Optional

from myccli.config import MyceliumConfiguration


@dataclass(frozen=True)
class TerraformProvider:
    name: str
    source: str
    version: str


@dataclass(frozen=True)
class AWSTerraformProvider(TerraformProvider):
    region: str


class TerraformProviderRegistry:
    def __init__(self, providers=None):
        self._providers = {}
        if providers is not None:
            for provider in providers:
                self.add_provider(provider)

    def add_provider(self, provider: TerraformProvider):
        if provider.name in self._providers:
            existing = self._providers[provider.name]
            if provider.version != existing.version:
                raise ValueError('Provider already exists with different version')
            return

        self._providers[provider.name] = provider

    def get_provider(self, name: str, version: Optional[str] = None) -> Optional[TerraformProvider]:
        assert version is None, 'Version control not implemented'
        return self._providers.get(name)

    def __iter__(self):
        return iter(self._providers.values())


def create_default_provider_registry(config: MyceliumConfiguration):
    aws_provider = AWSTerraformProvider(
        name='aws',
        source='hashicorp/aws',
        version='~> 4.30',
        region=config.aws_region,
    )

    docker_provider = TerraformProvider(
        name='docker',
        source='kreuzwerker/docker',
        version='2.22.0'
    )

    null_provider = TerraformProvider(
        name='null',
        source='hashicorp/null',
        version='3.1.1',
    )

    return TerraformProviderRegistry([
        aws_provider,
        docker_provider,
        null_provider,
    ])
