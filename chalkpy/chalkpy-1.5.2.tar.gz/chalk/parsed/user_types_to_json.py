import dataclasses
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel

from chalk._version import __version__
from chalk.config.project_config import load_project_config
from chalk.features import FeatureSetBase
from chalk.features.resolver import Resolver, SinkResolver
from chalk.importer import FailedImport
from chalk.parsed.json_conversions import convert_type_to_gql
from chalk.streams.stream import StreamResolver


def _get_classpath(x: object) -> Path:
    return Path(os.path.abspath(sys.modules[x.__module__].__file__))


def _convert_type_to_dict(t: Any) -> dict:
    return dataclasses.asdict(convert_type_to_gql(t))


def get_registered_types_as_json(scope_to: Path, failed: List[FailedImport], indent=2) -> str:
    features = [
        _convert_type_to_dict(feature)
        for x in FeatureSetBase.registry.values()
        if x.__module__ in sys.modules and _get_classpath(x).is_relative_to(scope_to)
        for feature in x.features
    ]
    stream_resolvers = [
        _convert_type_to_dict(t) for t in StreamResolver.registry if Path(t.filename).is_relative_to(scope_to)
    ]
    resolvers = [_convert_type_to_dict(t) for t in Resolver.registry if Path(t.filename).is_relative_to(scope_to)]
    sink_resolvers = [
        _convert_type_to_dict(t) for t in SinkResolver.registry if Path(t.filename).is_relative_to(scope_to)
    ]

    class EnvironmentSettings(BaseModel):
        id: str
        runtime: Optional[str]
        requirements: Optional[str]
        requires_packages: Optional[List[str]]
        dockerfile: Optional[str]

    class ProjectSettings(BaseModel):
        project: str
        environments: Optional[List[EnvironmentSettings]]

    def read_packages(filename: str) -> Optional[List[str]]:
        reqs = list()
        try:
            with open(filename) as f:
                for r in f.readlines():
                    cleaned = re.sub("#.*", "", r).removesuffix("\n").strip()
                    if cleaned != "":
                        reqs.append(cleaned)
            return reqs
        except OSError:
            return None

    config = load_project_config()
    if config is not None:
        config = ProjectSettings(
            project=config.project,
            environments=config.environments
            and [
                EnvironmentSettings(
                    id=i,
                    runtime=e.runtime,
                    requirements=e.requirements,
                    dockerfile=e.dockerfile,
                    requires_packages=read_packages(
                        os.path.join(
                            os.path.dirname(config.local_path),
                            e.requirements,
                        )
                    ),
                )
                for i, e in config.environments.items()
            ],
        ).dict()

    return json.dumps(
        dict(
            streams=stream_resolvers,
            sinks=sink_resolvers,
            resolvers=resolvers,
            features=features,
            config=config,
            failed=[d.dict() for d in failed],
            chalkpy={"version": __version__},
        ),
        indent=indent,
    )
