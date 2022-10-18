"""
Collector plugin for DNF packages
"""
import os
import shutil

from configparser import ConfigParser
from os import PathLike
from pathlib import Path
from typing import Dict, List, Optional, Union
from urllib.parse import quote_plus, urlparse

from hoppr_cyclonedx_models.cyclonedx_1_4 import Component
from packageurl import PackageURL  # type: ignore

from hoppr import __version__
from hoppr.base_plugins.collector import BatchCollectorPlugin
from hoppr.base_plugins.hoppr import hoppr_process, hoppr_rerunner
from hoppr.configs.credentials import Credentials
from hoppr.context import Context
from hoppr.hoppr_types.purl_type import PurlType
from hoppr.result import Result


def _artifact_string(purl: PackageURL) -> str:
    artifact_string = purl.name

    if purl.version is not None:
        artifact_string = "-".join([artifact_string, purl.version])
    if purl.qualifiers.get("arch") is not None:
        artifact_string = ".".join([artifact_string, purl.qualifiers.get("arch")])

    return artifact_string


def _repo_proxy(url: str) -> str:
    proxy = os.getenv("https_proxy", "_none_")
    no_proxy_urls = [
        item for item in os.getenv("no_proxy", "").split(",") if item != ""
    ]

    parsed_url = urlparse(url)

    for pattern in no_proxy_urls:
        if pattern in parsed_url.netloc:
            proxy = "_none_"
            break

    return proxy


class CollectDnfPlugin(BatchCollectorPlugin):
    """
    Collector plugin for DNF packages
    """

    required_commands: List[str] = ["dnf"]
    supported_purl_types: List[str] = ["rpm"]

    def __init__(
        self,
        context: Context,
        config: Optional[Dict] = None,
        config_file: Union[str, PathLike] = Path.cwd().joinpath(
            ".hoppr-dnf", "dnf.conf"
        ),
    ) -> None:
        super().__init__(
            context=context,
            config=config,
        )

        self.password_list: List[str] = []
        self.manifest_repos: List[str] = []

        for repo in self.context.manifest.consolidated_repositories[PurlType.RPM]:
            self.manifest_repos.append(repo.url)

        self.config_file = Path(config_file)

        if self.config and "dnf_command" in self.config:
            self.required_commands = [self.config["dnf_command"]]

        self.base_command = [
            self.required_commands[0],
            "--quiet",
            "--disableexcludes=all",
            f"--config={self.config_file}",
            "--disablerepo=*",
            "--enablerepo=hoppr-tmp-*",
        ]

    def _get_component_path(self, found_url: str) -> Union[Path, None]:
        """
        Create subdirectory path consisting of found URL
        with the manifest repo and RPM file name removed
        """
        for repo in self.manifest_repos:
            if found_url.startswith(repo):
                found_url_path = Path(found_url)
                subdir = found_url_path.relative_to(repo).parent

                return self.directory_for(
                    self.supported_purl_types[0], repo, subdir=str(subdir)
                )

        return None

    def get_version(self) -> str:
        return __version__

    @hoppr_process
    def pre_stage_process(self) -> Result:
        repo_config = ConfigParser()
        repo_config["main"] = {
            "cachedir": f"{self.config_file.parent / 'cache'}",
        }

        for idx, repo in enumerate(
            self.context.manifest.consolidated_repositories[PurlType.RPM]
        ):
            temp_repo = f"hoppr-tmp-{idx}"
            creds = Credentials.find_credentials(repo.url)

            self.get_logger().info(f"Creating repo {temp_repo} for url {repo.url}")

            # Create temporary repository file
            repo_config[temp_repo] = {
                "baseurl": f"{repo.url}",
                "enabled": "1",
                "name": f"Hoppr temp repository {idx}",
                "priority": "1",
                "proxy": _repo_proxy(repo.url),
                "module_hotfixes": "true",
            }

            if creds is not None:
                repo_config[temp_repo]["username"] = f"{creds.username}"
                repo_config[temp_repo]["password"] = f"{creds.password}"

        try:
            # Create repo config dir in user directory
            config_dir = self.config_file.parent
            config_dir.mkdir(parents=True, exist_ok=True)

            with self.config_file.open(mode="w+", encoding="utf-8") as repo_file:
                repo_config.write(repo_file, space_around_delimiters=False)
        except OSError as ex:
            return Result.fail(f"Unable to write DNF repository config file: {ex}")

        # Populate user DNF cache
        command = [
            *self.base_command,
            "check-update",
            "makecache",
        ]

        # Generate cache to use when downloading components
        result = self.run_command(command, self.password_list)

        if result.returncode != 0:
            return Result.fail("Failed to populate DNF cache.")

        return Result.success()

    @hoppr_rerunner
    def collect(self, comp: Component) -> Result:
        """
        Copy a component to the local collection directory structure
        """

        purl = PackageURL.from_string(comp.purl)
        artifact = _artifact_string(purl)

        self.get_logger().info(f"Copying DNF package from {purl}")

        # Try getting RPM URL
        command = [*self.base_command, "repoquery", "--location", artifact]
        result = self.run_command(command, self.password_list)

        # If RPM URL not found, no need to try downloading it
        if result.returncode != 0 or len(result.stdout.decode("utf-8")) == 0:
            msg = f"{self.required_commands[0]} failed to locate package for {purl}"
            self.get_logger().debug(msg)

            return Result.retry(msg)

        # Taking the first URL if multiple are returned
        found_url = result.stdout.decode("utf-8").strip().split("\n")[0]
        target_dir = self._get_component_path(found_url)

        # Return failure if found RPM URL is not from a repo defined in the manifest
        if target_dir is None:
            return Result.fail(
                "Successfully found RPM file but URL does not match any repository in manifest."
                f" (Found URL: '{found_url}')"
            )

        # Download the RPM file to the new directory
        command = [*self.base_command, "download", f"--destdir={target_dir}", artifact]
        result = self.run_command(command, password_list=self.password_list)

        if result.returncode != 0:
            msg = f"Failed to download DNF artifact {purl.name} version {purl.version}"
            return Result.retry(msg)

        return Result.success()

    @hoppr_process
    def post_stage_process(self) -> Result:
        # Find repodata folders created when cache was generated
        search_root = self.config_file.parent.joinpath("cache")
        paths = list(search_root.rglob("hoppr-tmp-*/repodata"))

        repo_config = ConfigParser()
        repo_config.read(filenames=self.config_file, encoding="utf-8")

        # Loop over repos defined in the temp dnf.conf file
        for section in repo_config.sections():
            # Loop over repodata folders in DNF cache
            for folder in paths:
                # Check if full repodata path contains temp repo name
                if section in str(folder):
                    # Get temp repo's URL as defined in manifest
                    repo_url = repo_config[section]["baseurl"]
                    target_dir = Path(
                        self.context.collect_root_dir,
                        "rpm",
                        quote_plus(repo_url),
                        "repodata",
                    )

                    shutil.copytree(src=folder, dst=target_dir, dirs_exist_ok=True)

        if self.config_file.exists():
            try:
                self.config_file.unlink()
            except FileNotFoundError as ex:
                return Result.fail(f"Failed to remove temporary DNF config file: {ex}")

        return Result.success()
