import sys
from typing import Union

from . import exceptions


class Namespace(object):
    def __repr__(self):
        attr = [i for i in self.__dir__() if not i.startswith('__')]
        repr = 'Namespace('

        for c, a in enumerate(attr):
            value = self.__getattribute__(a)

            if isinstance(value, str):
                value = f'"{value}"'

            if c == len(attr) - 1:
                repr += f'{a}={value})'
            else:
                repr += f'{a}={value}, '

        return repr


class ArgEasy(object):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        version: str = None
    ) -> None:
        """Create a new instance of ArgEasy.

        :param name: Application name, defaults to None
        :type name: str, optional
        :param description: Application description, defaults to None
        :type description: str, optional
        :param version: Application version, defaults to None
        :type version: str, optional
        """

        self._commands = {}
        self._flags = {}

        self._actions = [
            'store_true',
            'store_false',
            'append',
            'default'
        ]

        self.namespace = Namespace()

        self.project_name = name
        self.description = description
        self.version = version

        # add default flags
        self.add_flag('--help', 'View the help', action='store_true')
        self.add_flag('--version', 'View the version', action='store_true')

    def add_argument(
        self,
        name: str,
        help: str,
        action: str = 'default',
        max_append: str = '*'
    ) -> None:
        """Adds a new argument.

        The available actions are:
        default (returns the next argument as value),
        store_true, store_false, and append.

        :param name: Argument name
        :type name: str
        :param help: Usage help for the argument
        :type help: str
        :param action: Argument action, defaults to 'default'
        :type action: str, optional
        :param max_append: If the action is "append", this
        parameter sets the maximum number of items, defaults to '*'
        :type max_append: str, optional
        :raises Exception: Action not recognized
        """

        if action not in self._actions:
            raise Exception('Action not recognized')

        self._commands[name] = {
            'help': help,
            'action': action,
            'max_append': max_append
        }

        setattr(self.namespace, name, None)

    def add_flag(
        self,
        name: str,
        help: str,
        action: str = 'default',
        max_append: str = '*'
    ) -> None:
        """Adds a new flag.

        The available actions are:
        default (returns the next argument as value),
        store_true, store_false, and append.

        The flag name can have only
        one hyphen if the flag has
        only one letter (-h), or two
        hyphens if it is a word
        (--help).

        :param name: Flag name
        :type name: str
        :param help: Help text
        :type help: str
        :param action: Flag action, defaults to 'default'
        :type action: str, optional
        :param required: If flag is required, defaults to False
        :type required: bool, optional
        """

        if action not in self._actions:
            raise Exception('Action not recognized')

        self._flags[name] = {
            'help': help,
            'action': action,
            'max_append': max_append
        }

        name = name.strip('-')
        name = name.replace('-', '_')

        setattr(self.namespace, name, None)

    def _print_help(self) -> None:
        print(f'usage: [command] [**optional] [flags]')
        if self.description:
            print(f'\n{self.description}')

        if self._commands:
            print('\ncommands:')
            for cmd, info in self._commands.items():
                print(f'    {cmd}: {info["help"]}')

        if self._flags:
            print('\nflags:')
            for flag, info in self._flags.items():
                print(f'    {flag}: {info["help"]}')

        sys.exit(0)

    def _print_version(self) -> None:
        if not self.project_name:
            print(f'Project: {self.version}')
        else:
            print(f'{self.project_name}: {self.version}')

        sys.exit(0)

    def _get_args(self) -> tuple:
        args = sys.argv[1:]
        arg_flags = [a for a in args if a.startswith('-')]

        return args, arg_flags

    def _append_arguments(self, args: list, max_append: str, index: int) -> Union[None, list]:
        if max_append == '*':
            arg_list = args[index + 1:]
        else:
            max_append = int(max_append) + (index + 1)

            if not len(args[index + 1:]) > max_append:
                arg_list = args[index + 1:max_append]
            else:
                return None

        arguments = []

        for a in arg_list:
            if a.startswith('-'):
                break
            else:
                arguments.append(a)

        return arguments

    def _get_flags(self, args: list, arg_flags: list) -> dict:
        for flag, info in self._flags.items():
            value = None

            if flag in arg_flags:
                action = info['action']
                flag_index = args.index(flag)
                max_append = info['max_append']

                if action == 'store_true':
                    value = True
                elif action == 'store_false':
                    value = False
                elif action == 'append':
                    if len(args[flag_index:]) == 1:
                        raise exceptions.InvalidFlagUseError(f'Invalid use of the flag "{flag}"')

                    value = self._append_arguments(args, max_append, flag_index)

                    if not value:
                        raise exceptions.InvalidFlagUseError(f'Invalid use of the flag "{flag}"')
                elif action == 'default':
                    if len(args[flag_index:]) < 2:
                        raise exceptions.InvalidFlagUseError(f'Invalid use of the flag "{flag}"')
                    else:
                        next_arg = flag_index + 1
                        value = args[next_arg]

            flag = flag.strip('-')
            flag = flag.replace('-', '_')

            setattr(self.namespace, flag, value)

    def _get_command(self, args: list, command: str):
        info = self._commands.get(command)

        if info:
            action = info['action']
            max_append = info['max_append']
            cmd_index = args.index(command)

            if action == 'store_true':
                value = True
            elif action == 'store_false':
                value = False
            elif action == 'append':
                value = self._append_arguments(args, max_append, cmd_index)

                if value is None:
                    raise exceptions.InvalidArgumentUseError('Invalid argument use')
            elif action == 'default':
                if len(args) < 2:
                    raise exceptions.InvalidArgumentUseError('Invalid argument use')
                else:
                    value = args[1]

            setattr(self.namespace, command, value)

    def parse(self) -> Namespace:
        """Formats the command line arguments
        and returns them in an object.
        
        Checks the obtained arguments 
        and determines the value of them
        by returning a Namespace object.

        If the argument has the value of
        "None", it means that it was not
        called by the command line.
        """

        args, args_flags = self._get_args()

        if len(args) == 0:
            self._print_help()
            return self.namespace

        command = args[0]

        if command not in self._commands and command not in self._flags:
            print(f'unrecognized command or flag: {command}')
            print('use --help to see flags and arguments')
            return self.namespace

        try:
            self._get_flags(args, args_flags)
        except exceptions.InvalidFlagUseError as err:
            print(err.message)
            sys.exit(0)

        try:
            self._get_command(args, command)
        except exceptions.InvalidArgumentUseError:
            print(f'Invalid use of the argument "{command}"')
            sys.exit(0)

        # check default flags
        if self.namespace.help:
            self._print_help()
        elif self.namespace.version:
            self._print_version()

        return self.namespace
