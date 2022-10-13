from __future__ import absolute_import, division, print_function, unicode_literals
from io import open

from abc import abstractmethod

import os

from ruamel.yaml import YAMLError, safe_load

import publisher.settings as settings
from publisher.exceptions import SingleProceduresNotFoundError, MissingYamlFileError, ValidationError, \
    CombinedValidationError, InvalidYamlFileError
from publisher.utils import get_content_directories
import yamale
from yamale import YamaleError
from ruamel.yaml.scanner import ScannerError
from .settings import PHASE_SCHEMA_PATH, PROCEDURE_SCHEMA_PATH, INFO_CARD_SCHEMA_PATH

class Validator(object):

    def __init__(self, working_directory):
        self.working_directory = working_directory

    @abstractmethod
    def validate(self):
        pass


class SingleProcedureValidator(Validator):

    def validate(self):
        procedure_directories = get_content_directories(self.working_directory)

        if len(procedure_directories) != 1:
            print(procedure_directories)
            raise SingleProceduresNotFoundError()


class YamlFileValidator(Validator):

    def __init__(self, yaml_file, schema):
        self.yaml_file = yaml_file
        self.schema = schema

    def validate(self):

        try:
            data = yamale.make_data(self.yaml_file, parser="ruamel")
        except IOError:
            raise MissingYamlFileError(self.yaml_file)
        except ScannerError:
            raise InvalidYamlFileError(
                "Invalid yaml syntax in {}".format(self.yaml_file)
            )

        try:
            yamale.validate(self.schema, data, strict=True)
        except YamaleError as yaml_error:
            invalid_keys = []
            issues = str(yaml_error).split("\n\t")[1:]
            for issue in issues:
                key = issue.split(":")[0]
                if key not in invalid_keys:
                    invalid_keys.insert(0, key)
            raise InvalidYamlFileError(
                "{}\nThe following keys have bad values or are missing:\n{}".format(
                    self.yaml_file, "\n".join(["\t - {}".format(key) for key in invalid_keys])
                )
            )


class ProcedureYamlFileValidator(YamlFileValidator):

    def __init__(self, procedure_directory):
        yaml_file = os.path.join(procedure_directory, "procedure.yml")

        schema = yamale.make_schema(PROCEDURE_SCHEMA_PATH)
        with open(INFO_CARD_SCHEMA_PATH) as include_yaml:
            info_card_includes = safe_load(include_yaml)
        schema.add_include(info_card_includes)

        super(ProcedureYamlFileValidator, self).__init__(yaml_file, schema)


class PhaseYamlFileValidator(YamlFileValidator):

    def __init__(self, phase_directory):
        yaml_file = os.path.join(phase_directory, 'phase.yml')

        schema = yamale.make_schema(PHASE_SCHEMA_PATH)
        with open(INFO_CARD_SCHEMA_PATH) as include_yaml:
            info_card_includes = safe_load(include_yaml)
        schema.add_include(info_card_includes)

        super(PhaseYamlFileValidator, self).__init__(yaml_file, schema)

class AssetDirectoryValidator(Validator):

    def __init__(self, base_directory):
        self.asset_directory = os.path.join(base_directory, 'assets')

    def validate(self):
        if not os.path.exists(self.asset_directory):
            os.mkdir(self.asset_directory)


def validate_procedure_directory():
    SingleProcedureValidator(settings.PROCEDURE_CHECKOUT_DIRECTORY).validate()


def validate_save():

    validate_procedure_directory()

    procedure_directory = os.path.join(settings.PROCEDURE_CHECKOUT_DIRECTORY,
                                       get_content_directories(settings.PROCEDURE_CHECKOUT_DIRECTORY)[0])

    validators = [ProcedureYamlFileValidator(procedure_directory), AssetDirectoryValidator(procedure_directory)]

    phase_directories = [os.path.join(procedure_directory, d) for d in get_content_directories(procedure_directory)]

    validators += [PhaseYamlFileValidator(d) for d in phase_directories]
    validators += [AssetDirectoryValidator(d) for d in phase_directories]

    errors = []

    for v in validators:
        try:
            v.validate()
        except ValidationError as e:
            errors.append(e)

    if len(errors) > 0:
        raise CombinedValidationError(errors)
