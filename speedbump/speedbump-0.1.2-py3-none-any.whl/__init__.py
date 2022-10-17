import os
from pathlib import Path

from github import Github
from sh import git
from yaml import dump

github = Github(os.getenv("GITHUB_TOKEN"))


def conf_item(package_ecosystem: str, directory: str):
    return {
        "package-ecosystem": package_ecosystem,
        "directory": directory,
        "schedule": {"interval": "daily"},
    }


def make_conf(file_path):
    if ".github/workflows" in file_path:
        return conf_item("github-actions", "/")

    if file_path.endswith(("requirements.txt", "setup.py")):
        path, _, _ = file_path.rpartition("/")
        return conf_item("pip", "/" + path)

    if file_path.endswith("package.json"):
        path, _, _ = file_path.rpartition("/")
        return conf_item("npm", "/" + path)

    if file_path.endswith("Dockerfile"):
        path, _, _ = file_path.rpartition("/")
        return conf_item("docker", "/" + path)

    if file_path.endswith("pom.xml"):
        path, _, _ = file_path.rpartition("/")
        return conf_item("maven", "/" + path)

    return False


def run():
    files = set(git("ls-files"))

    config = dict(version=2, updates=[])
    configured_ecosystems = set()

    for f in files:
        update_conf = make_conf(f.strip())
        if update_conf:
            eco_dir = (
                update_conf["package-ecosystem"],
                update_conf["directory"],
            )
            if eco_dir not in configured_ecosystems:
                config["updates"].append(update_conf)
                configured_ecosystems.add(eco_dir)

    project_root = Path.cwd()
    github_dir = project_root / ".github"
    github_dir.mkdir(exist_ok=True)

    if config["updates"]:
        with open(github_dir / "dependabot.yml", "w") as conf_file:
            print(conf_file)
            conf_file.write(dump(config, sort_keys=False))
