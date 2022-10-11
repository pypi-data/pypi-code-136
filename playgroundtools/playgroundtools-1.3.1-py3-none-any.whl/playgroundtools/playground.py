import json

from .exceptions import (
    PGConfigNotFoundError,
    PGDoesNotExistError,
    PGInvalidConfError,
    PGInvalidSettingError,
    PGJSONFormatError,
    PGSettingsNotFoundError,
    PGTypeNotFoundError,
)
from .resources import load_file_resources, load_text_resources
from .util import get_key, get_playground_dir, set_key


def load_json(name, input):
    try:
        return json.loads(input)
    except json.JSONDecodeError as err:
        raise PGJSONFormatError(name, str(err))


def get_config():
    """Get the configuration for the package."""
    try:
        config_json = load_text_resources("config.json")
        return load_json("config.json", config_json)
    except FileNotFoundError:
        raise PGConfigNotFoundError


def set_config(config):
    try:
        config_path = load_file_resources("config.json")
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    except FileNotFoundError:
        raise PGConfigNotFoundError


def get_settings(playground_dir):
    """Retrieve the settings for a given playground."""
    settings_path = playground_dir / "settings.json"
    try:
        with open(settings_path) as f:
            return load_json(settings_path, f.read())
    except FileNotFoundError:
        raise PGSettingsNotFoundError(playground_dir)


def clean_config(args, raw_config={}):
    """Returns config options in a more usable format."""
    config = {}
    if args.command == "config":
        cleaned = clean_config_config(args, raw_config)
    else:
        playground_dir = get_playground_dir(args)
        if args.command == "new":
            cleaned = clean_config_new(args, raw_config)
        else:
            cleaned = {}
            if not playground_dir.exists():
                raise PGDoesNotExistError(playground_dir)
            if args.command == "run":
                cleaned = clean_config_run(playground_dir)
        config.update(dir=playground_dir)
    config.update(cleaned)
    return config


def clean_config_new(args, raw_config):
    """Cleans the configuration for the new command."""
    try:
        type_config = raw_config[args.type]
    except KeyError:
        raise PGTypeNotFoundError(args.type)
    lib = type_config["lib"] + args.lib
    verbosity = args.verbose if hasattr(args, "verbose") else 1
    try:
        return {
            "verbosity": verbosity,
            "folders": type_config["folders"] + ["requirements"],
            "files": {
                **type_config["files"],
                "requirements/requirements.in": lib,
            },
            "lib": lib,
            "settings": {
                "module": type_config["module"],
                "args": type_config["args"],
            },
        }
    except KeyError as err:
        raise PGInvalidConfError(err.args, args.type)


def clean_config_run(playground_dir):
    """Cleans the configuration for the run command."""
    settings = get_settings(playground_dir)
    try:
        return {
            "settings": {
                "python": settings["python"],
                "module": settings["module"],
                "args": settings["args"],
            }
        }
    except KeyError as err:
        raise PGInvalidSettingError(err.args)


def clean_config_config(args, raw_config):
    """Cleans the configuration for the config command."""
    new_config = raw_config
    if args.subcommand == "add":
        new_config[args.type] = load_json("input", args.value)

    elif args.subcommand == "delete":
        try:
            del new_config[args.type]
        except KeyError:
            raise PGTypeNotFoundError(args.type)

    elif args.subcommand == "edit":
        keys = args.key.split(".")
        value = load_json("input", args.value)
        set_key(keys, value, new_config)

    elif args.read:
        keys = args.read.split(".")
        value = get_key(keys, new_config)
        new_config = {"value": value}

    return new_config
