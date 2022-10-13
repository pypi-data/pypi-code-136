import json

from .exceptions import (
    PGConfigNotFoundError,
    PGDoesNotExistError,
    PGInvalidConfError,
    PGInvalidSettingError,
    PGJSONFormatError,
    PGSettingsNotFoundError,
)
from .resources import load_file_resource, load_text_resource
from .util import get_full_path, get_key, set_key


def load_json(name, input):
    try:
        return json.loads(input)
    except json.JSONDecodeError as err:
        raise PGJSONFormatError(name, str(err))


def get_config():
    """Get the configuration for the package."""
    try:
        config_json = load_text_resource("config.json")
        return load_json("config.json", config_json)
    except FileNotFoundError:
        raise PGConfigNotFoundError


def set_config(config):
    try:
        with load_file_resource("config.json") as config_path:
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
        playground_dir = get_full_path(args.name)
        if args.command == "new":
            cleaned = clean_config_new(args, raw_config)
        else:
            cleaned = {}
            if not playground_dir.exists():
                raise PGDoesNotExistError(playground_dir)
            if args.command == "run":
                cleaned = clean_config_run(args, playground_dir)
        config.update(dir=playground_dir)
    config.update(cleaned)
    return config


def clean_config_new(args, raw_config):
    """Cleans the configuration for the new command."""
    try:
        type_config = raw_config[args.type]
    except KeyError:
        raise PGInvalidConfError(args.type)
    lib = type_config["lib"] + args.lib
    try:
        return {
            "verbosity": args.verbose,
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
        keys = (args.type, *err.args)
        key = ".".join(keys)
        raise PGInvalidConfError(key)


def clean_config_run(args, playground_dir):
    """Cleans the configuration for the run command."""
    settings = get_settings(playground_dir)
    try:
        return {
            "settings": {
                "python": settings["python"],
                "module": args.module if args.module else settings["module"],
                "args": args.args if args.args else settings["args"],
            }
        }
    except KeyError as err:
        raise PGInvalidSettingError(err.args)


def clean_config_config(args, raw_config):
    """Cleans the configuration for the config command."""
    new_config = raw_config
    subcommands = {
        "add": clean_config_add,
        "delete": clean_config_delete,
        "edit": clean_config_edit,
    }
    func = subcommands.get(args.subcommand, clean_config_read)
    return func(args, new_config)


def clean_config_add(args, config):
    """Cleans the configuration for the config add command."""
    cleaned = config
    if args.type:
        cleaned[args.type] = {}
        if args.value:
            cleaned[args.type] = load_json("input", args.value)
    elif args.file:
        file_path = get_full_path(args.file)
        with open(file_path) as f:
            custom_config = load_json(file_path, f.read())
        cleaned.update(custom_config)
    return cleaned


def clean_config_delete(args, config):
    """Cleans the configuration for the config delete command."""
    cleaned = config
    try:
        if args.type:
            del cleaned[args.type]
        elif args.file:
            file_path = get_full_path(args.file)
            with open(file_path) as f:
                custom_config = load_json(file_path, f.read())
            for key in custom_config:
                del cleaned[key]
    except KeyError:
        raise PGInvalidConfError(args.type)
    return cleaned


def clean_config_edit(args, config):
    """Cleans the configuration for the config edit command."""
    cleaned = config
    keys = args.key.split(".")
    value = load_json("input", args.value)
    set_key(keys, value, cleaned)
    return cleaned


def clean_config_read(args, config):
    """Cleans the configuration for the config command with no args."""
    cleaned = config
    if args.read:
        keys = args.read.split(".")
        try:
            value = get_key(keys, cleaned)
        except KeyError:
            raise PGInvalidConfError(args.read)
        cleaned = {"value": value}
    return cleaned
