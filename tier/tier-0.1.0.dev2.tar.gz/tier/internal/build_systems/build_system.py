# std
from __future__ import annotations

# internal
from tier.internal.configs.abstract_config import SubConfig
from tier.internal.errors import TierException
from tier.internal.build_systems.abstract_build_system import AbstractBuildSystem


def get(config: SubConfig) -> AbstractBuildSystem:
    from tier.internal.build_systems.poetry import Poetry
    build_backend = config.get('build-system.build-backend')
    if build_backend == Poetry.build_backend():
        return Poetry(config)
    else:
        raise TierException('Could not determine build system')
