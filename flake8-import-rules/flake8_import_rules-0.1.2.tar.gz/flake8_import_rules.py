import ast
import yaml
import argparse
from os.path import basename, dirname, relpath
from textwrap import dedent

__version__ = "0.1.2"

class ConfigError(Exception):
    pass

def is_fit(current: str, rule: str):
    """Check if current module name match to rule module name"""
    clen = len(current)
    rlen = len(rule)
    return (
        rule == "any"
        or rule == "all"
        or (
            current.startswith(rule)
            and (clen == rlen or clen > rlen and current[rlen] == ".")
        )
    )


def check(src_modname: str, import_modname: str, config: dict) -> bool:
    """
    Args:
        src_modname: module name, where we are checking the imports
        import_modname: import to check
        config: dict like
                "foo":
                    "allow": True
                    "name": "bar"
    """
    with open("/tmp/zzz", "a") as f:
        f.write(f"{src_modname}, {import_modname}\n")
    for rule_modname, rules in config.items():
        if is_fit(src_modname, rule_modname):
            for rule in rules:
                if is_fit(import_modname, rule["name"]):
                    return rule["allow"]
    return True


class ImportsFinder(ast.NodeVisitor):
    def __init__(self, current_module, config, source):
        self.current_module = current_module
        self.config = config
        self.errors = []
        self.source = source

    def remember_error(self, node):
        line = ast.get_source_segment(self.source, node).replace("\n", " ")[:80]
        self.errors.append(
            (node.lineno, node.col_offset, f"I013 denied import: {line}")
        )

    def visit_Import(self, node):
        for alias in node.names:
            if not check(self.current_module, alias.name, self.config):
                self.remember_error(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):

        base = []
        if node.module is not None:
            base.append(node.module)
        if node.level > 0:
            # Handle .mod and ..mod imports
            base = self.current_module.split(".")[: -node.level] + base

        for alias in node.names:
            name = base.copy()

            if alias.name != "*":
                name.append(alias.name)

            if not check(self.current_module, ".".join(name), self.config):
                self.remember_error(node)
        self.generic_visit(node)


class ImportRulesChecker(object):
    options = None
    name = "flake8-import-rules"
    version = __version__

    def __init__(self, tree, filename, lines):
        self.tree = tree
        self.filename = filename
        self.modname = (
            dirname(relpath(filename)).replace("/", ".") + "." + basename(filename)[:-3]
        )
        self.source = "".join(lines)
        self.config = ImportRulesChecker.config

    @classmethod
    def raise_error(cls, line):
        format_string = (
            "Format of rule: [allow | deny] [module_name | any]"
        )
        raise ConfigError(f"Wrong format at: {line}\n{format_string}")


    @classmethod
    def add_options(cls, parser):
        parser.add_option(
            "--import-rules",
            default="",
            parse_from_config=True,
            help="Import rules for flake8-import-rules plugin",
        )

    @classmethod
    def parse_options(cls, options):
        cls.config = dict()
        if options.import_rules:
            rules_in = yaml.load(options.import_rules, yaml.Loader)
            for dest_module, module_rules in rules_in.items():
                rules = list()
                if isinstance(module_rules, str):
                    module_rules=[module_rules]
                for line in module_rules:
                    try:
                        op, modname = line.split()
                    except Exception:
                        cls.raise_error(line)
                    op = op.strip()
                    modname = modname.strip()
                    if not (op == "allow" or op == "deny"):
                        cls.raise_error(line)
                    rules.append(dict(allow=op == "allow", name=modname))
                cls.config[dest_module] = rules

    def run(self):
        if self.config:
            finder = ImportsFinder(self.modname, self.config, self.source)
            finder.visit(self.tree)
            for (a, b, c) in finder.errors:
                yield (a, b, c, ImportRulesChecker)
