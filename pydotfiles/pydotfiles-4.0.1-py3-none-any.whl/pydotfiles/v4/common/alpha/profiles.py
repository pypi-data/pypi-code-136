# General imports
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True, order=True)
class Profile:
    name: str
    dependencies: list[str]

    @staticmethod
    def from_dict(data: Dict) -> list['Profile']:
        return [Profile.from_profile_dict(name, dependencies) for name, dependencies in data.items()]

    @staticmethod
    def from_profile_dict(name: str, dependencies: list[str]) -> 'Profile':
        return Profile(
            name=name,
            dependencies=dependencies
        )
