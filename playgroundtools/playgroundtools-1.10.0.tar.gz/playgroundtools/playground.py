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
from .util import delete_key, format_dict, get_full_path, get_key, set_key


def load_json(name, input):
    """Returns the JSON-decoded version of input."""
    try:
        return json.loads(input)
    except json.JSONDecodeError as err:
        raise PGJSONFormatError(name, str(err))


def format_config(config, custom, args):
    """Formats the keys and values of a configuration."""
    format_map = {
        "name": args.name,
        **custom
    }
    return format_dict(config, format_map)


def get_options(custom_format, args):
    """Returns formatting options based on defaults and args."""
    options = {}
    if args.options:
        options = load_json('options', args.options)
    return {**custom_format, **options}


def get_playground_dir(args):
    """Retrieves the playground directory from args."""
    playground_dir = get_full_path(args.name)
    if not playground_dir.exists():
        raise PGDoesNotExistError(playground_dir)
    return playground_dir


def get_config():
    """Get the configuration for the package."""
    try:
        config_json = load_text_resource("config.json")
        return load_json("config.json", config_json)
    except FileNotFoundError:
        raise PGConfigNotFoundError


def set_config(config):
    """Sets the config to the input specified."""
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
    config_map = {
        "new": clean_config_new,
        "delete": clean_config_delete,
        "run": clean_config_run,
        "config": clean_config_config,
    }
    params = [args]
    if raw_config:
        params.append(raw_config)
    return config_map[args.command](*params)


def clean_config_new(args, raw_config):
    """Cleans the configuration for the new command."""
    try:
        type_config = raw_config[args.type]
    except KeyError:
        raise PGInvalidConfError(args.type)
    try:
        lib = type_config["lib"] + args.lib
        cleaned = {
            "dir": get_full_path(args.name),
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

    custom_format = type_config.get("format", {})
    options = get_options(custom_format, args)
    return format_config(cleaned, options, args)


def clean_config_run(args):
    """Cleans the configuration for the run command."""
    playground_dir = get_playground_dir(args)
    settings = get_settings(playground_dir)
    try:
        return {
            "dir": playground_dir,
            "settings": {
                "python": settings["python"],
                "module": args.module if args.module else settings["module"],
                "args": args.args if args.args else settings["args"],
            },
        }
    except KeyError as err:
        raise PGInvalidSettingError(err.args)


def clean_config_delete(args):
    """Cleans the configuration for the delete command."""
    return {"dir": get_playground_dir(args)}


def clean_config_config(args, raw_config):
    """Cleans the configuration for the config command."""
    new_config = raw_config
    subcommands = {
        "delete": clean_config_conf_delete,
        "set": clean_config_conf_set,
    }
    func = subcommands.get(args.subcommand, clean_config_conf_read)
    return func(args, new_config)


def clean_config_conf_delete(args, config):
    """Cleans the configuration for the config delete command."""
    cleaned = config
    try:
        if args.key:
            keys = args.key.split(".")
            config = delete_key(keys, config)
        elif args.file:
            file_path = get_full_path(args.file)
            with open(file_path) as f:
                custom_config = load_json(file_path, f.read())
            for key in custom_config:
                del cleaned[key]
    except KeyError:
        raise PGInvalidConfError(args.type)
    return cleaned


def clean_config_conf_set(args, config):
    """Cleans the configuration for the config set command."""
    cleaned = config
    if args.key:
        keys = args.key.split(".")
        value = load_json("input", args.value)
        set_key(keys, value, cleaned)
    elif args.file:
        file_path = get_full_path(args.file)
        with open(file_path) as f:
            custom_config = load_json(file_path, f.read())
        cleaned.update(custom_config)
    return cleaned


def clean_config_conf_read(args, config):
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
