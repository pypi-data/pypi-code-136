from typing import List, Dict, Union, Callable, Optional, Any
import os
import sys
import importlib.machinery
import importlib.util
import types
import argparse

from .functional import takewhile, dropwhile


class Semver:
    def __init__(self, version_string: str):
        self._version: List[int] = [*map(int, version_string.split("."))]

    def greater_than(self, other: Union["Semver", str]) -> bool:
        if isinstance(other, str):
            other = Semver(other)
            return self.greater_than(other)
        elif isinstance(other, Semver):
            greater = False
            nolesser = True
            for x, y in zip(self._version, other._version):
                if x > y:
                    greater = True
                    break
                if y > x:
                    nolesser = False
            if len(other) < len(self):
                return nolesser or greater
            else:
                return nolesser and greater

    def equal_to(self, other: object) -> bool:
        if isinstance(other, str):
            other = Semver(other)
            return self.equal_to(other)
        elif isinstance(other, self.__class__):
            return len(self) == len(other) and\
                all([x == y for x, y in zip(self._version, other._version)])
        else:
            raise NotImplementedError(f"Cannot compare Semver and {type(other)}")

    def smaller_than(self, other: Union["Semver", str]) -> bool:
        if isinstance(other, str):
            other = Semver(other)
            return self.smaller_than(other)
        else:
            return not self.greater_than(other) and not self.equal_to(other)

    def geq(self, other: Union["Semver", str]) -> bool:
        return self.greater_than(other) or self.equal_to(other)

    def leq(self, other: Union["Semver", str]) -> bool:
        return self.smaller_than(other) or self.equal_to(other)

    def __ne__(self, other: object) -> bool:
        return not self.equal_to(other)

    def __eq__(self, other: object) -> bool:
        return self.equal_to(other)

    def __lt__(self, other: Union["Semver", str]) -> bool:
        return self.smaller_than(other)

    def __le__(self, other: Union["Semver", str]) -> bool:
        return self.leq(other)

    def __gt__(self, other: Union["Semver", str]) -> bool:
        return self.greater_than(other)

    def __ge__(self, other: Union["Semver", str]) -> bool:
        return self.geq(other)

    def __len__(self) -> int:
        return len(self._version)

    def __repr__(self) -> str:
        return ".".join(map(str, self._version))


def load_user_module(modname: str, search_path: List[str] = None) -> Optional[types.ModuleType]:
    """`search_paths` is a list of paths. Defaults to `sys.path`

    Args:
        modname: Name of the module
        search_path: Additional search path for the module

    """
    if search_path is not None:
        spec = importlib.machinery.PathFinder.find_spec(modname, search_path)
    else:
        if modname.endswith(".py"):
            modname = modname[:-3]
        spec = importlib.machinery.PathFinder.find_spec(modname)
    if spec is None:
        print(f"Could not find module {modname}")
        return None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[modname] = mod
    return mod
    # if spec.loader:
    #     spec.loader.exec_module(mod)
    #     return mod
    # else:
    #     return None


class hierarchical_parser:
    """Simple way to build a hierarchical argument parser with python.

    args:
        name: Name of the command
        usage: The usage string
        cmd_map: A :class:`dict` of mapping command names to functions
        gopts_parser: A :class:`argparse.ArgumentParser` to parse any global options
        version_str: Versioning string

    Example:
        def func_a(arglist):
            parser = argparse.ArgumentParser("something")
            parser.add_argument("-a")
            args = parser.parser_args(arglist)
            # rest of the code

        parser = hierarchical_parser("myparser", "myparser USAGE",
                    {"cmd_a": func_a, "cmd_b": func_b})
        parser()

    Optional global opts parser can also be given, which will parse any options
    before first command. If a global opts parser is given then the commands
    should accept the parsed global opts as a second argument.

    Example:
        def func_b(arglist, gopts):
            parser = argparse.ArgumentParser("something")
            parser.add_argument("-a")
            args = parser.parser_args(arglist)
            # rest of the code

        def global_opts_parser(arglist):
            parser = argparse.ArgumentParser("something")
            parser.add_argument("--verbosity")
            parser.add_argument("--logfile")
            args, _ = parser.parser_known_args(arglist)
            # can do something with args here
            return args # optional, will be passed on to commands

        parser = hierarchical_parser("myparser", "myparser USAGE",
                    {"cmd_a": func_a, "cmd_b": func_b}, global_opts_parser,
                    version_str="1.2.0")

    Global opts should be flags and should not be set, as that can cause
    confusion for the commands. *This may change in the future*.

    E.g., for the previous example, the following seems reasonable:
        $> mycommand -flag cmd_a -a

    However :code:`mycommand --verbosity debug --logfile some_file cmd_a -a`
    looks confusing. Therefore, global opts are only parsed till the first word
    not starting with "-" occurs. Hence for previous command, "debug" is parsed
    as a command and will raise an error as it's not in "cmd_map".

    """
    def __init__(self, name: str, usage: str, cmd_map: Dict[str, Callable[[List[str]], Any]],
                 gopts_parser: Optional[Callable[[List[str]], None]],
                 version_str: Optional[str] = None):
        self.name = name
        self.usage = usage
        self.cmd_map = cmd_map
        self.gopts_parser = gopts_parser
        self.version_str = version_str or "No version provided"

    # NOTE: The global opts is a bit tricky. If we don't parse and interpret the
    #       arguments here, then the actions will have to be provided alongside
    #       the args.
    #
    #       Or let the user parse and interpret the global opts but then help
    #       display and all must be controlled by the user.
    def __call__(self):
        parser = argparse.ArgumentParser(self.name, allow_abbrev=False, add_help=False,
                                         formatter_class=argparse.RawTextHelpFormatter,
                                         usage=self.usage)
        parser.add_argument("command", help=f"""Command to run.

command is one of {", ".join(map(lambda x: f'"{x}"', self.cmd_map.keys()))}

Type "{self.name} command --help" to get help about the individual commands.""")
        if self.version_str:
            parser.add_argument("--version", action="store_true", help="Print version and exit")
        if len(sys.argv) == 1:
            print("No command given\n")
            parser.print_help()
            sys.exit(1)
        elif sys.argv[1] in {"-h", "--help"}:
            parser.print_help()
            sys.exit(0)
        elif sys.argv[1] == "--version" and self.version_str:
            print(self.version_str)
            sys.exit(0)
        if sys.argv[1].startswith("-"):
            pre_cmd_args = [*takewhile(lambda x: x.startswith("-"), sys.argv[1:])]
            if self.gopts_parser is not None:
                gopts = self.gopts_parser(pre_cmd_args)
            else:
                msg = ", ".join(map(lambda x: f'"{x}"', pre_cmd_args))
                print(f"Unknown options {msg}")
                parser.print_help()
                sys.exit(1)
        else:
            gopts = None
        post_cmd_args = [*dropwhile(lambda x: x.startswith("-"), sys.argv[1:])]
        if not post_cmd_args:
            parser.print_help()
            sys.exit(1)
        try:
            args, sub_args = parser.parse_known_args(post_cmd_args)
        except Exception:
            parser.print_help()
            sys.exit(1)

        if args.command in self.cmd_map:
            if self.gopts_parser is not None:
                self.cmd_map[args.command](sub_args, gopts)
            else:
                self.cmd_map[args.command](sub_args)
        else:
            print(f"Unknown command \"{args.command}\"\n")
            parser.print_help()
            sys.exit(1)
