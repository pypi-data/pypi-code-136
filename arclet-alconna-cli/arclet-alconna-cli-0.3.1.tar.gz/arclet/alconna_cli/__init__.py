from clilte import CommandLine
from arclet.alconna import alconna_version
from .plugins import Create, Cache, Lang, Analysis, Using

alc_cli = CommandLine("alconna", "Alconna-CLI", alconna_version)
alc_cli.add(Create, Cache, Lang, Analysis, Using)
