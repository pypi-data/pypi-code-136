from sphinxcli.types import Builder

PYPROJECT_TABLE_NAME = "sphinxcli"
LIST_SEPARATOR = ":"
DEFAULT_SOURCE_PATH = "."
DEFAULT_TARGET_PATH = "build"
DEFAULT_TARGET_LANG = "en"
DEFAULT_LANGUAGES = ["en"]
DEFAULT_LC_MESSAGES = "en"
DEFAULT_BUILDERS: list[Builder] = ["html"]
DEFAULT_TARGET_ORDER = "builder"
