import json
from argparse import ArgumentParser
from pathlib import Path

from .ead_validator import EadValidator

parser = ArgumentParser(description="EAD Validator")
parser.add_argument("ead_file", help="Path to an EAD file to be validated")
parser.add_argument("ead_schema_dir", help="Path to a directory containing EAD schema files")
parser.add_argument("namespaces_dir", help="Path to a directory containing namespace files")
parser.add_argument("ead_settings_file", help="Path to an ead-settings file")
parser.add_argument(
    "--config-file", help="Path to a config file that should additionally be validated against the given EAD"
)
parser.add_argument("--enable-legacy-support", action="store_true", help="Include allowed legacy schemas")
args = parser.parse_args()

ead_validator = EadValidator(
    Path(args.ead_schema_dir),
    Path(args.namespaces_dir),
    Path(args.ead_settings_file),
    enable_legacy_support=args.enable_legacy_support,
)

with open(args.ead_file, encoding="utf-8") as f:
    ead = json.load(f)

if args.config_file:
    with open(args.config_file, encoding="utf-8") as f:
        config = json.load(f)
    ead_validator.validate_with_config(ead, config)
else:
    ead_validator.validate(ead)
