# General imports
from pathlib import Path
from typing import Dict, Optional, Set
from collections import defaultdict
from logging import getLogger
from tempfile import mkdtemp as mktempdir
from datetime import datetime
from os import walk as os_walk
from os import path as os_path
from dataclasses import dataclass
from shutil import copy2 as shutil_copy2
from os import chmod as os_chmod

# Project imports
from pydotfiles.v4.common import Configuration
from pydotfiles.v4.common.alpha import AlphaManifest, AlphaCore, AlphaDefaultSettings, AlphaDeveloperEnvironments, \
    OSName, ActionType, OperatingSystem, Environment
from pydotfiles.v4.common.alpha.action import Action
from .io import template_run_script, template_copy_file, template_symlink_file, template_starter_helper_functions, template_dev_environment_setup
from .os import template_os_packages, template_os_applications, template_os_default_dock, template_os_default_setting_files

logger = getLogger(__name__)


class Builder:
    """
    Generates profile build packages, which are self-contained,
    'single use' dotfiles that aren't dynamically managed by pydotfiles,
    but are instead meant for easy 1-time installations.

    This is to help support a lighter-weight entry into automated dotfiles,
    without requiring users to commit to a whole dynamically updated ecosystem
    """

    def __init__(self, configurations: list[Configuration], base_dir: Path):
        # Maps from a given profile name to the file paths that are defined there
        self.profile_map: Dict[str, list[Path]] = defaultdict(list)
        self.profile_dependencies: Dict[str, list[str]] = defaultdict(list)
        self.profile_file_types: Dict[Path, type] = {}
        # self.manifests: Dict[Path, AlphaManifest] = {}
        self.dev_environments: Dict[Path, AlphaDeveloperEnvironments] = {}
        self.default_settings: Dict[Path, AlphaDefaultSettings] = {}
        self.core: Dict[Path, AlphaCore] = {}
        self.defined_os: set[OSName] = set()
        self.base_dir = base_dir

        for configuration in configurations:
            if isinstance(configuration.data, AlphaCore):
                self.core[configuration.file_path] = configuration.data
                self.profile_map[configuration.data.profile].append(configuration.file_path)
                self.profile_file_types[configuration.file_path] = AlphaCore
                if configuration.data.os is not None:
                    self.defined_os.add(configuration.data.os.name)
            elif isinstance(configuration.data, AlphaManifest):
                # self.manifests[configuration.file_path] = configuration.data
                for profile in configuration.data.profiles:
                    dependencies = self.profile_dependencies[profile.name]
                    for dependency in profile.dependencies:
                        dependencies.append(dependency)
                self.profile_file_types[configuration.file_path] = AlphaManifest
            elif isinstance(configuration.data, AlphaDeveloperEnvironments):
                self.dev_environments[configuration.file_path] = configuration.data
                self.profile_map[configuration.data.profile].append(configuration.file_path)
                self.profile_file_types[configuration.file_path] = AlphaDeveloperEnvironments
            elif isinstance(configuration.data, AlphaDefaultSettings):
                logger.error("FIXME THIS SHOULDN'T EXIST")
                self.default_settings[configuration.file_path] = configuration.data
                self.profile_file_types[configuration.file_path] = AlphaDefaultSettings

    def build(self, profiles: Optional[list[str]], specified_oses: Optional[list[str]]) -> Dict[str, Path]:
        active_profiles = self.__get_active_profiles(profiles)
        package_paths: Dict[str, Path] = {}

        for active_os in self.__get_active_os(specified_oses):
            for active_profile in active_profiles:
                build_data = self.__get_build_files(active_profile, active_os)
                package_paths[f"{active_os}.{active_profile}"] = self.__build_package(build_data, active_os, active_profile)
        return package_paths

    def __get_active_profiles(self, profiles: Optional[list[str]]) -> set[str]:
        # When no profiles are passed in we generate all of them
        if profiles is None:
            # .key() only returns a set-like object, not a full set object with a .intersection method,
            # so we wrap the iterable returned in a set
            filtered_profiles = set(self.profile_dependencies.keys())
        else:
            filtered_profiles = set(profiles)
        active_profiles = filtered_profiles.intersection(self.profile_dependencies.keys())
        logger.debug(f"Generating build packages for the following active profiles: {active_profiles}")
        return active_profiles

    def __get_active_os(self, specified_oses: Optional[list[str]]) -> set[OSName]:
        # When no OSes are passed in we generate all of them
        if specified_oses is None:
            filtered_oses = self.defined_os
        else:
            filtered_oses = set([OSName[specified_os] for specified_os in specified_oses])
        active_oses = filtered_oses.intersection(self.defined_os)
        logger.debug(f"Building the following OSes: {active_oses}")
        return active_oses

    ##
    # WARNING: Everything below this line is terrible 6am code, come back and refactor after
    ##

    def __get_build_files(self, profile: str, active_os: OSName) -> list[Configuration]:
        dependency_paths = self.__map_profile_to_dependencies(profile)
        dependencies = []
        for dependency_path in dependency_paths:
            dependency_type = self.profile_file_types.get(dependency_path)
            if dependency_type == AlphaCore:
                core_data = self.core.get(dependency_path)
                if core_data.os is None or core_data.os.name is active_os:
                    logger.debug(
                        f"Profile {profile} on {active_os.value} has the following dependency path: {dependency_path}")
                    dependencies.append(Configuration(dependency_path, core_data))
            elif dependency_type == AlphaDeveloperEnvironments:
                developer_environment_data = self.dev_environments.get(dependency_path)
                logger.debug(
                    f"Profile {profile} on {active_os.value} has the following dependency path: {dependency_path}")
                dependencies.append(Configuration(dependency_path, developer_environment_data))
        return dependencies

    def __map_profile_to_dependencies(self, profile: str) -> list[Path]:
        combined_dependencies = []
        for dependency in self.profile_dependencies[profile]:
            for dependency_path in self.profile_map[dependency]:
                combined_dependencies.append(dependency_path)
        return combined_dependencies

    def __build_package(self, build_data: list[Configuration], active_os: OSName, active_profile: str) -> Path:
        dirpath = Path(mktempdir(None, f"pydotfiles-{datetime.now().isoformat()}-{active_os.value}-{active_profile}-"))
        # build_data = self.__consolidate_requirements(build_data)

        is_installation_init_written = False
        for build_datum in build_data:
            package_builder = PackageBuilder(build_datum.data, build_datum.file_path, dirpath, self.base_dir, active_os)

            if not is_installation_init_written:
                package_builder.write_init()
                is_installation_init_written = True
            package_builder.build()
            package_builder.write_tail()
        return dirpath

    def __consolidate_requirements(self, build_data: list[Configuration]) -> list[Configuration]:
        """
        Note: not working, pathing gets messed up depending on load order, so avoid this for now

        One thing that we'd like to do is to consolidate any configurations such as OS-level/package-level
        configurations so that they can occur all at once, instead of sporadically.
        """
        final_build_data = []
        os_build_data = []

        for build_datum in build_data:
            if isinstance(build_datum.data, AlphaCore):
                if build_datum.data.os is None:
                    final_build_data.append(build_datum)
                else:
                    os_build_data.append(build_datum)

        maybe_consolidated_data = self.__consolidate_os_build_data(os_build_data)
        if maybe_consolidated_data is not None:
            final_build_data.append(maybe_consolidated_data)
        return final_build_data

    def __consolidate_os_build_data(self, build_data: list[Configuration]) -> Optional[Configuration]:
        if len(build_data) == 0:
            return None

        if len(build_data) == 1:
            return build_data[0]

        consolidated_data = {"profile": "consolidated("}
        consolidated_actions = []
        consolidated_os = {
            "packages": [],
            "applications": [],
            "default_dock": [],
            "default_settings_files": [],
        }

        for build_datum in build_data:
            data: AlphaCore = build_datum.data
            consolidated_data["version"] = data.version
            consolidated_data["schema"] = data.schema

            # In reality this value isn't used in later code, so it's fine if this is inaccurate
            consolidated_data["profile"] += data.profile

            for action in data.actions:
                consolidated_actions.append(action.to_dict())

            original_os: OperatingSystem = data.os
            consolidated_os["name"] = original_os.name.value

            if original_os.shell is not None and consolidated_os.get("shell") is None:
                consolidated_os["shell"] = original_os.shell.value

            for package in original_os.packages:
                consolidated_os["packages"].append(package)

            for application in original_os.applications:
                consolidated_os["applications"].append(application)

            for default_dock_item in original_os.default_dock:
                consolidated_os["default_dock"].append(default_dock_item)

            for default_settings_file in original_os.default_settings_files:
                consolidated_os["default_settings_files"].append(default_settings_file)

        consolidated_data["profile"] += ")"
        consolidated_data["actions"] = consolidated_actions
        consolidated_data["os"] = consolidated_os

        return Configuration(
            file_path=build_data[0].file_path,
            data=AlphaCore.from_dict(consolidated_data)
        )

##
# Build package methods
##


@dataclass(frozen=True, order=True)
class Symlink:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    script_destination_file: Path
    is_sudo: bool


@dataclass(frozen=True, order=True)
class Copy:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    script_destination_file: Path
    is_sudo: bool


@dataclass(frozen=True, order=True)
class RunScript:
    initial_origin_file: Path
    destination_in_build_package: Path
    script_origin_file: Path
    # No need for script destination file since the command is just being executed,
    # and not copied or symlinked elsewhere
    is_sudo: bool


class PackageBuilder:
    def __init__(self, data: AlphaCore | AlphaDeveloperEnvironments, file_path: Path, dirpath: Path, base_dir: Path, active_os: OSName):
        self.data = data
        self.file_path = file_path
        self.dirpath = dirpath
        self.installation_script = Path.joinpath(dirpath, "install.sh")
        self.base_dir = base_dir
        self.active_os = active_os

    def write_init(self) -> None:
        with self.installation_script.open('a') as init_fp:
            init_fp.write(f"#!/usr/bin/env bash\n\n# Fails on the first error\nset -e\n\n{template_starter_helper_functions()}")
        os_chmod(self.installation_script, 0o744)

    def write_tail(self) -> None:
        with self.installation_script.open('a') as init_fp:
            init_fp.write("\n")

    def build(self):
        if isinstance(self.data, AlphaCore):
            self.__add_to_build_package_core(self.data)
        elif isinstance(self.data, AlphaDeveloperEnvironments):
            self.__add_to_build_package_developer_env(self.data)

    def __add_to_build_package_core(self, data: AlphaCore) -> None:
        if data.os is not None:
            self.__add_os_to_build_package(data.os)
        self.__add_actions_to_build_package(data.actions)

    def __add_os_to_build_package(self, data: OperatingSystem) -> None:
        self.__add_os_to_install_script(data)

    def __add_os_to_install_script(self, data: OperatingSystem) -> None:
        os_instructions = ""
        os_instructions += template_os_packages(data)
        os_instructions += template_os_applications(data)
        os_instructions += template_os_default_dock(data)
        os_instructions += template_os_default_setting_files(data)

        with self.installation_script.open('a') as install_fp:
            install_fp.write(os_instructions)

    def __add_actions_to_build_package(self, data: list[ActionType]) -> None:
        for datum in data:
            self.__add_action_to_build_package(datum)

    def __add_action_to_build_package(self, data: ActionType) -> None:
        action_switcher = {
            Action.copy: self.__add_copy_files,
            Action.script: self.__add_run_scripts,
            Action.symlink: self.__add_symlinks,
        }

        action_switcher.get(data.action)(data)

    def __add_copy_files(self, data: ActionType) -> None:
        copy_actions = self.__get_copy_actions(data)
        # for copy_action in copy_actions:
        #     logger.debug(f"Adding in copy\n--------\n{copy_action}")
        self.__copy_files_to_build_package(copy_actions)
        self.__add_copy_instruction_to_install_script(copy_actions)

    def __get_copy_actions(self, data: ActionType) -> Set[Copy]:
        files_to_copy = set()
        for file_name, destination_name in data.files.items():
            if file_name == "*":
                files_to_copy = self.__get_files_to_copy(self.file_path.parent, Path(destination_name), data.sudo, data.hidden) | files_to_copy
            else:
                if data.absolute:
                    files_to_copy.add(Copy(
                        initial_origin_file=None,
                        destination_in_build_package=None,
                        script_origin_file=Path(file_name),
                        script_destination_file=Path(destination_name),
                        is_sudo=data.sudo
                    ))
                    continue

                files_to_copy.add(Copy(
                    initial_origin_file=self.file_path.parent.joinpath(Path(file_name)),
                    destination_in_build_package=self.dirpath.joinpath(
                        self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir)),
                    script_origin_file=self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir),
                    script_destination_file=Path(destination_name),
                    is_sudo=data.sudo
                ))
        return files_to_copy

    def __get_files_to_copy(self, directory: Path, destination_dir: Path, is_sudo: bool, is_hidden: bool) -> Set[Copy]:
        files_to_copy = set()
        for path_prefix, directory_names, file_names in os_walk(directory):
            for file_name_path in file_names:
                if file_name_path.endswith(".json") or file_name_path.endswith(".yaml") or file_name_path.endswith(".yml") or file_name_path.endswith(".symlink"):
                    continue

                destination_file = Path(f"{'.' if is_hidden else ''}{file_name_path}")
                files_to_copy.add(Copy(
                    initial_origin_file=Path(os_path.join(path_prefix, file_name_path)),
                    destination_in_build_package=self.dirpath.joinpath(
                        Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir)),
                    script_origin_file=Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir),
                    script_destination_file=destination_dir.joinpath(destination_file),
                    is_sudo=is_sudo
                ))
        return files_to_copy

    def __add_copy_instruction_to_install_script(self, copies: set[Copy]) -> None:
        copy_instruction = ""
        for copy in copies:
            copy_instruction += template_copy_file(copy.script_origin_file, copy.script_destination_file)
        with self.installation_script.open('a') as install_fp:
            install_fp.write(copy_instruction)

    def __add_run_scripts(self, data: ActionType) -> None:
        run_scripts = self.__get_runscripts(data)
        for run_script in run_scripts:
            logger.debug(f"Adding in run script:\n---------------{run_script}---------------\n")
        self.__copy_files_to_build_package(run_scripts)
        self.__add_runscript_instructions_to_install_script(run_scripts)

    def __get_runscripts(self, data: ActionType) -> set[RunScript]:
        files_to_execute = set()
        for file_name, destination_name in data.files.items():
            if file_name == "*":
                # In group symlinks, destination_name is a directory
                wildcard_scripts = self.__get_files_to_execute(self.file_path.parent, Path(destination_name), data.sudo, data.hidden)
                files_to_execute = wildcard_scripts | files_to_execute
            else:
                if data.absolute:
                    files_to_execute.add(RunScript(
                        initial_origin_file=None,
                        destination_in_build_package=None,
                        script_origin_file=Path(file_name),
                        is_sudo=data.sudo
                    ))
                    continue

                files_to_execute.add(RunScript(
                    initial_origin_file=self.file_path.parent.joinpath(Path(file_name)),
                    destination_in_build_package=self.dirpath.joinpath(
                        self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir)),
                    script_origin_file=self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir),
                    is_sudo=data.sudo
                ))

        # logger.debug(f"The script files to execute are: {files_to_execute}")
        return files_to_execute

    def __get_files_to_execute(self, directory: Path, destination_dir: Path, is_sudo: bool, is_hidden: bool) -> Set[RunScript]:
        files_to_execute = set()
        for path_prefix, directory_names, file_names in os_walk(directory):
            for file_name_path in file_names:
                # We cheat here a bit and say "if you're specifying a wildcard execute script operation,
                # then every file in this directory that's not a symlink or copy operation can be executed,
                # and we don't check for whether the executable bit (since we're lazy, we can add it in later
                # if it turns out useful
                if not file_name_path.endswith(".symlink") and not file_name_path.endswith(".json") and not file_name_path.endswith(".yaml") and not file_name_path.endswith(".yml"):
                    files_to_execute.add(RunScript(
                        initial_origin_file=Path(os_path.join(path_prefix, file_name_path)),
                        destination_in_build_package=self.dirpath.joinpath(Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir)),
                        script_origin_file=Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir),
                        is_sudo=is_sudo
                    ))
        return files_to_execute

    def __add_runscript_instructions_to_install_script(self, run_scripts: set[RunScript]) -> None:
        script_instruction = ""
        for run_script in run_scripts:
            script_instruction += template_run_script(run_script.script_origin_file, run_script.is_sudo)
        with self.installation_script.open('a') as install_fp:
            install_fp.write(script_instruction)

    def __add_symlinks(self, data: ActionType) -> None:
        symlinks = self.__get_symlinks(data)
        # for symlink in symlinks:
        #     logger.debug(f"Adding in symlink\n--------\n{symlink}")
        self.__copy_files_to_build_package(symlinks)
        self.__add_symlink_instruction_to_install_script(symlinks)

    def __get_symlinks(self, data: ActionType) -> set[Symlink]:
        files_to_symlink = set()
        for file_name, destination_name in data.files.items():
            if file_name == "*":
                # In group symlinks, destination_name is a directory
                wildcard_symlinks = self.__get_files_to_symlink(self.file_path.parent, Path(destination_name), data.sudo, data.hidden)
                files_to_symlink = wildcard_symlinks | files_to_symlink
            else:
                if data.absolute:
                    files_to_symlink.add(Symlink(
                        initial_origin_file=None,
                        destination_in_build_package=None,
                        script_origin_file=Path(file_name),
                        script_destination_file=Path(destination_name),
                        is_sudo=data.sudo
                    ))
                    continue

                files_to_symlink.add(Symlink(
                    initial_origin_file=self.file_path.parent.joinpath(Path(file_name)),
                    destination_in_build_package=self.dirpath.joinpath(
                        self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir)),
                    script_origin_file=self.file_path.parent.joinpath(Path(file_name)).relative_to(self.base_dir),
                    script_destination_file=Path(destination_name),
                    is_sudo=data.sudo
                ))

        # logger.debug(f"The files to symlink are: {files_to_symlink}")
        return files_to_symlink

    def __get_files_to_symlink(self, directory: Path, destination_dir: Path, is_sudo: bool, is_hidden: bool) -> Set[Symlink]:
        files_to_symlink = set()
        for path_prefix, directory_names, file_names in os_walk(directory):
            for file_name_path in file_names:
                if file_name_path.endswith(".symlink"):
                    destination_file = Path(f"{'.' if is_hidden else ''}{file_name_path}".replace(".symlink", ""))
                    files_to_symlink.add(Symlink(
                        initial_origin_file=Path(os_path.join(path_prefix, file_name_path)),
                        destination_in_build_package=self.dirpath.joinpath(Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir)),
                        script_origin_file=Path(os_path.join(path_prefix, file_name_path)).relative_to(self.base_dir),
                        script_destination_file=destination_dir.joinpath(destination_file),
                        is_sudo=is_sudo
                    ))
        return files_to_symlink

    def __copy_files_to_build_package(self, actions: set[Copy] | set[Symlink] | set[RunScript]) -> None:
        for action in actions:
            if action.initial_origin_file is None:
                logger.debug(f"Skipping file copying since no file was given (absolute path)")
                continue
            logger.debug(f"Copying the file {action.initial_origin_file} to {action.destination_in_build_package}")
            try:
                action.destination_in_build_package.parent.mkdir(parents=True, exist_ok=True)
                shutil_copy2(action.initial_origin_file, action.destination_in_build_package)
            except FileNotFoundError:
                logger.exception(f"The action was: {action}")

    def __add_symlink_instruction_to_install_script(self, symlinks: set[Symlink]) -> None:
        symlink_instruction = ""
        for symlink in symlinks:
            symlink_instruction += template_symlink_file(symlink.script_origin_file, symlink.script_destination_file, symlink.is_sudo)
        with self.installation_script.open('a') as install_fp:
            install_fp.write(symlink_instruction)

    def __add_to_build_package_developer_env(self, data: AlphaDeveloperEnvironments) -> None:
        for environment in data.environments:
            self.__add_dev_environment_to_install_script(environment)

    def __add_dev_environment_to_install_script(self, data: Environment) -> None:
        dev_environment_setup = template_dev_environment_setup(data, self.active_os)
        with self.installation_script.open('a') as install_fp:
            install_fp.write(dev_environment_setup)
