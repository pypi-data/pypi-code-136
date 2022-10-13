

from typing import Dict, List, Tuple

import click
from bluetarget.model_version import ModelVersion

from bluetarget.validation import validate_files, validate_model_class

from bluetarget.utils import clean_tmp, prepare_package
from bluetarget.model import Model


class BlueTarget:

    api_key: str
    model_id: str
    model_version_id: str

    environment: Dict = None
    metadata: Dict = None
    implementation: str = "py38"
    framework: str = None

    model: Model

    def __init__(self, api_key: str, model_id: str = None, model_version_id: str = None) -> None:
        self.api_key = api_key
        self.model_id = model_id
        self.model_version_id = model_version_id

        self.model = Model(api_key)

    def set_model_id(self, model_id: str) -> None:
        self.model_id = model_id
        self.model.set_model_id(model_id)

    def set_environment(self, environment: Dict) -> None:
        self.environment = environment

    def set_metadata(self, metadata: Dict) -> None:
        self.metadata = metadata

    def set_framework(self, framework: str) -> None:
        self.framework = framework

    def set_implementation(self, implementation: Dict) -> None:
        self.implementation = implementation

    def set_model_version_id(self, model_version_id: str) -> None:
        self.model_version_id = model_version_id

    def deploy(self, model_class: str, model_files: List[str], requirements_file: str, model_name: str = None, metadata: Dict = None, environment: Dict = None, algorithm: str = None, implementation: str = None, framework: str = None) -> Tuple[Model, ModelVersion]:

        metadata = self.metadata if metadata == None else metadata
        environment = self.environment if environment == None else environment
        implementation = self.implementation if implementation == None else implementation
        framework = self.framework if framework == None else framework

        if self.model_id == None:
            self.model.create(name=model_name)
        else:
            self.model.get(self.model_id)

        if self.model_version_id == None:
            model_version = self.model.create_version(
                model_class=model_class,
                model_files=model_files,
                metadata=metadata,
                requirements_file=requirements_file,
                algorithm=algorithm,
                environment=environment,
                implementation=implementation,
                framework=framework
            )
        else:
            model_version = self.model.get_version(self.model_version_id)

        files = [*model_files, requirements_file]

        validate_files(files)
        validate_model_class(model_class, model_files)

        package = prepare_package(files)

        model_version.upload_package(package_url=package)

        model_version.deploy()

        clean_tmp()

        click.secho('########################################', fg='yellow')
        click.secho(f"### MODEL ID: {self.model_id} ###", fg='yellow')
        click.secho('########################################', fg='yellow')

        return self.model, model_version

    def predict(self, inputs: List):
        return self.model.predict(inputs=inputs)

    def health(self):
        return self.model.health()
