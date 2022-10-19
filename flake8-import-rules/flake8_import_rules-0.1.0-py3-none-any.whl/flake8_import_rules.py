import ast
import yaml
import argparse
from os.path import basename, dirname

__version__ = "0.1.0"


class LintException(Exception):
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
    for rule_modname, rules in config.items():
        if is_fit(src_modname, rule_modname):
            for rule in rules:
                if is_fit(import_modname, rule["name"]):
                    return rule["allow"]
    return True


class ImportsFinder(ast.NodeVisitor):
    def __init__(self, current_module, config):
        self.current_module = current_module
        self.config = config
        self.errors = []

    def remember_error(self, node):
        self.errors.append((node.lineno, node.col_offset, "I013 denied import present"))

    def visit_Import(self, node):
        for alias in node.names:
            if not check(self.current_module, alias.name, self.config):
                self.remember_error(node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        dot_count = 0
        for letter in node.module:
            if letter == ".":
                dot_count += 1
            else:
                break

        current_module = self.current_module
        if dot_count > 0:
            # Handle .mod and ..mod imports
            current_module = ".".join(
                self.current_module.split(".")[: -dot_count + 1] + [node.module]
            )

        for alias in node.names:
            if alias.name == "*":
                name = node.module
            else:
                name = f"{current_module}.{alias.name}"

            if not check(self.current_module, name, self.config):
                self.remember_error(node)
        self.generic_visit(node)


class ImportRulesChecker(object):
    options = None
    name = "flake8-import-rules"
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename
        self.modname = (
            dirname(filename).replace("/", ".") + "." + basename(filename)[:-3]
        )

        self.config = ImportRulesChecker.config

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
        if options.import_rules:
            current_module = None
            cls.config = dict()
            rules = list()
            for line in options.import_rules.splitlines():
                if line == "":
                    continue
                if line[-1:] == "=":
                    if current_module is not None:
                        cls.config[current_module] = rules
                    current_module = line.rstrip()[:-1].strip()
                    rules = list()
                else:
                    if current_module is None:
                        assert (
                            False
                        ), 'Wrong import_rules config, module name "module=" should be first'
                    format_string = (
                        "Format of rule: [allow | deny] [the_mod_name | any]"
                    )
                    op, modname = line.split()
                    op = op.strip()
                    modname = modname.strip()
                    assert op == "allow" or op == "deny", (
                        "Keyword should be allow or deny. " + format_string
                    )
                    rules.append(dict(allow=op == "allow", name=modname))
            if current_module:
                cls.config[current_module] = rules

    def run(self):
        finder = ImportsFinder(self.modname, self.config)
        finder.visit(self.tree)
        for (a, b, c) in finder.errors:
            yield (a, b, c, ImportRulesChecker)
