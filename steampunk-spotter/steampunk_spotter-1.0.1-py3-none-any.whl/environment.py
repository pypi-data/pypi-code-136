import json
import platform
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Optional, List, Dict, Any

import pkg_resources
import pydantic.dataclasses
import yaml
from pydantic.json import pydantic_encoder


class _EnvironmentDataclassConfig:
    extra = "forbid"
    # all dataclass arguments are optional because this is a discovery process
    # but use
    allow_mutation = False


@pydantic.dataclasses.dataclass(config=_EnvironmentDataclassConfig)
class EnvironmentAnsibleVersion:
    """Discovered Ansible versions (per edition, i.e. full, base, core)"""

    ansible_core: Optional[str] = None
    ansible_base: Optional[str] = None
    ansible: Optional[str] = None


@pydantic.dataclasses.dataclass(config=_EnvironmentDataclassConfig)
class Environment:
    """User environment/workspace state discovery (retrieves system info and versions of installed packages)"""

    python_version: Optional[str] = None
    ansible_version: Optional[EnvironmentAnsibleVersion] = None
    installed_collections: Optional[List[Dict[str, Optional[str]]]] = None
    ansible_config: Optional[Dict[str, Any]] = None
    galaxy_yml: Optional[Dict[str, Any]] = None
    collection_requirements: Optional[Dict[str, Any]] = None
    cli_scan_args: Optional[Dict[str, Any]] = None

    @staticmethod
    def _get_python_version() -> str:
        """
        Get python version
        :return: Version string
        """
        return platform.python_version()

    @staticmethod
    def _get_ansible_core_python_version() -> Optional[str]:
        """
        Get ansible-core python package version
        :return: Version string
        """
        try:
            return pkg_resources.get_distribution("ansible-core").version
        except pkg_resources.DistributionNotFound:
            return None

    @staticmethod
    def _get_ansible_base_python_version() -> Optional[str]:
        """
        Get ansible-base python package version
        :return: Version string
        """
        try:
            return pkg_resources.get_distribution("ansible-base").version
        except pkg_resources.DistributionNotFound:
            return None

    @staticmethod
    def _get_ansible_version() -> Optional[str]:
        """
        Get Ansible version
        :return: Version string
        """
        try:
            output = subprocess.check_output(["ansible", "--version"], stderr=subprocess.DEVNULL).decode("utf-8")
            return output.splitlines()[0].lower().replace("ansible", "").strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None

    @staticmethod
    def _get_installed_ansible_collections() -> List[Dict[str, Optional[str]]]:
        """
        Get installed Ansible collections
        :return: Dict with Ansible collection names and their versions
        """
        installed_collections = []
        try:
            output = subprocess.check_output(["ansible-galaxy", "collection", "list", "--format", "json"],
                                             stderr=subprocess.DEVNULL).decode(
                "utf-8")
            for location, value in json.loads(output).items():
                for fqcn, version in value.items():
                    installed_collections.append({"fqcn": fqcn,
                                                  "version": version.get("version", None),
                                                  "location": location})
            return installed_collections
        except (subprocess.CalledProcessError, FileNotFoundError):
            return installed_collections

    @staticmethod
    def _get_ansible_config() -> Dict[str, Any]:
        """
        Get Ansible config current settings
        :return: Dict with Ansible config current settings specified as key-value pairs
        """
        ansible_config = {}
        try:
            output = subprocess.check_output(["ansible-config", "dump", "--only-changed"],
                                             stderr=subprocess.DEVNULL).decode("utf-8")
            for line in output.splitlines():
                if line:
                    key, value = line.split("=", maxsplit=1)
                    ansible_config[key.strip()] = value.strip()
            return ansible_config
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ansible_config

    @staticmethod
    def _get_galaxy_yml(path: Path) -> Dict[str, Any]:
        """
        Get galaxy.yml contents
        :param path: Path to directory where collection requirements reside
        :return: Contents of galaxy.yml file
        """
        try:
            with (path / "galaxy.yml").open("r", encoding="utf-8") as stream:
                try:
                    parsed = yaml.safe_load(stream)
                    if not (isinstance(parsed, dict) and all(isinstance(k, str) for k in parsed.keys())):
                        print("Failed basic format checking for the collection galaxy.yml file. Ignoring.")
                        return {}
                    return parsed
                except yaml.YAMLError:
                    return {}
        except OSError:
            return {}

    @staticmethod
    def _get_collection_requirements(path: Path) -> Dict[str, Any]:
        """
        Get Ansible collection requirements from requirements.yml or collections/requirements.yml
        :param path: Path to directory where collection requirements reside
        :return: Contents of requirements.yml or collections/requirements.yml file
        """
        try:
            # TODO: Update discovery as requirements.yml files can be anywhere
            search_path = path
            if path.is_file():
                search_path = path.parent

            possible_requirements_yml_paths = (search_path / "requirements.yml",
                                               search_path / "requirements.yaml",
                                               search_path / "collections" / "requirements.yml",
                                               search_path / "collections" / "requirements.yaml")

            requirements_yml_path = None
            for possible_requirements_yml_path in possible_requirements_yml_paths:
                if possible_requirements_yml_path.exists():
                    requirements_yml_path = possible_requirements_yml_path
                    break

            if requirements_yml_path:
                with requirements_yml_path.open("r", encoding="utf-8") as stream:
                    try:
                        parsed = yaml.safe_load(stream)
                        if not (isinstance(parsed, dict) and all(isinstance(k, str) for k in parsed.keys())):
                            print("Failed basic format checking for the collection requirements file. Ignoring.")
                            return {}
                        return parsed
                    except yaml.YAMLError:
                        return {}
            else:
                return {}
        except OSError:
            return {}

    @classmethod
    def from_local_discovery(cls, paths: List[Path]) -> "Environment":
        """Set workspace variables discovered locally on user's system.

        :param paths: List of paths to directory where to look for local files
        """
        # TODO: Add support to combine multiple galaxy.yml and requirements.yml, right now we use just the first one
        return cls(
            python_version=cls._get_python_version(),
            ansible_version=EnvironmentAnsibleVersion(
                ansible_core=cls._get_ansible_core_python_version(),
                ansible_base=cls._get_ansible_base_python_version(),
                ansible=cls._get_ansible_version(),
            ),
            installed_collections=cls._get_installed_ansible_collections(),
            ansible_config=cls._get_ansible_config(),
            galaxy_yml=cls._get_galaxy_yml(paths[0]) if paths else {},
            collection_requirements=cls._get_collection_requirements(paths[0]) if paths else {}
        )

    @classmethod
    def from_config_file(cls, config_path: Path) -> "Environment":
        """
        Set workspace variables from environment

        :param config_path: Configuration file path (must exist)
        """
        try:
            if not config_path.exists():
                print(f"Error: config file at {config_path} does not exist.")
                sys.exit(1)

            with config_path.open("r") as config_file:
                config = yaml.safe_load(config_file)
                return cls(
                    ansible_version=EnvironmentAnsibleVersion(
                        ansible_core=config.get("ansible_version")
                    )
                )
        except yaml.YAMLError as e:
            print(f"Invalid configuration file: {e}")
            sys.exit(1)

    @classmethod
    def from_extra_vars(cls, extra_vars: Dict[str, Any]) -> "Environment":
        """
        Set workspace variables from extra vars
        :param extra_vars: Dict of variables
        """
        return cls(
            ansible_version=EnvironmentAnsibleVersion(
                ansible_core=extra_vars.get("ansible_version")
            )
        )

    def combine(self, other: "Environment") -> "Environment":
        """
        Combines two dataclasses into one, overriding with values from `other`.

        Null values in `other` do not override original values.
        """
        original_dict_copy = deepcopy(pydantic_encoder(self))
        other_dict_copy = deepcopy(pydantic_encoder(other))
        other_dict_without_nulls = {k: v for k, v in other_dict_copy.items() if v is not None}
        original_dict_copy.update(other_dict_without_nulls)
        return self.__class__(**original_dict_copy)
