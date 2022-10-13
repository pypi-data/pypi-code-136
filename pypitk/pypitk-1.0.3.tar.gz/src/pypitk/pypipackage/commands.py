from typing import List
from .config import Config


def _form_command(__name: str, command: str):
    return f"# {__name.title()}:\n#    {command}"


def _filter_if_exists(__iter):
    return (value for value in iter(__iter) if value)


class Command:
    def __init__(self, __name: str, public: str, private: str = ""):
        self.name = __name
        self.public = public
        self.private = private if private else public

    @property
    def public_command(self):
        return _form_command(self.name, self.public) if self.public else ""

    @property
    def private_command(self):
        return _form_command(self.name, self.private) if self.private else ""


class Commands(List[Command]):

    @property
    def public_commands(self):
        return _filter_if_exists(command.public_command for command in self)

    @property
    def private_commands(self):
        return _filter_if_exists(command.private_command for command in self)

    def __get_command(self,name:str):
        result = None
        for command in self:
            if command.name == name:
                result = command
                break
        return result

    @property
    def install_locally(self):
        return self.__get_command(name="install_locally")



def commands(__config: Config):

    install_poetry = Command("install poetry", public="python3 -m pip install poetry")

    build = Command("build package", public="python3 -m poetry build")

    publish = Command(
        "publish package",
        public=f"python3 -m poetry publish -u <username> -p <password>",
        private=f"python3 -m poetry publish -u {__config.pypi_username} -p {__config.pypi_password}",
    )

    install_locally = Command(
        "install locally",
        public=f"python3 -m pip install {__config.package_name}=={__config.package_version}",
    )

    build_and_publish = Command(
        "build and publish package",
        public=f"{build.public};{publish.public}",
        private=f"{build.public};{publish.private}",
    )

    build_publish_and_install = Command(
        "build package; publish package; install package",
        public=f"{build_and_publish.public};{install_locally.public}",
        private=f"{build_and_publish.private};{install_locally.public}",
    )

    return Commands(
        (
            install_poetry,
            build,
            publish,
            install_locally,
            build_and_publish,
            build_publish_and_install,
        )
    )
