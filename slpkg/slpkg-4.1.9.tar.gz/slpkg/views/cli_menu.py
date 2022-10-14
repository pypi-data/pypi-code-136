#!/usr/bin/python3
# -*- coding: utf-8 -*-


from slpkg.configs import Configs


def usage(status: int):
    colors = Configs.colour
    color = colors()

    BOLD = color['BOLD']
    RED = color['RED']
    CYAN = color['CYAN']
    YELLOW = color['YELLOW']
    ENDC = color['ENDC']

    args = [f'{BOLD}USAGE:{ENDC} {Configs.prog_name} [{YELLOW}OPTIONS{ENDC}] [{CYAN}COMMAND{ENDC}] <packages>\n',
            f'{BOLD}DESCRIPTION:{ENDC}',
            '  Packaging tool that interacts with the SBo repository.\n',
            f'{BOLD}COMMANDS:{ENDC}',
            f'  {RED}update{ENDC}                    Update the package lists.',
            f'  {CYAN}upgrade{ENDC}                   Upgrade all the packages.',
            f'  {CYAN}build{ENDC} <packages>          Build only the packages.',
            f'  {CYAN}install{ENDC} <packages>        Build and install the packages.',
            f'  {CYAN}remove{ENDC} <packages>         Remove installed packages.',
            f'  {CYAN}find{ENDC} <packages>           Find installed packages.',
            f'  {CYAN}search{ENDC} <packages>         Search packages on repository.',
            f'  {CYAN}clean-logs{ENDC}                Clean dependencies log tracking.',
            f'  {CYAN}clean-tmp{ENDC}                 Delete all the downloaded sources.\n',
            f'{BOLD}OPTIONS:{ENDC}',
            f'  {YELLOW}--yes{ENDC}                     Answer Yes to all questions.',
            f'  {YELLOW}--jobs{ENDC}                    Set it for multicore systems.',
            f'  {YELLOW}--resolve-off{ENDC}             Turns off dependency resolving.',
            f'  {YELLOW}--reinstall{ENDC}               Use this option if you want to upgrade.',
            f'  {YELLOW}--skip-installed{ENDC}          Skip installed packages.',
            f'  {YELLOW}--download-only{ENDC}           Download only the packages.\n',
            '  -h, --help                Show this message and exit.',
            '  -v, --version             Print version and exit.\n',
            'If you need more information try to use slpkg manpage.']

    for opt in args:
        print(opt)
    raise SystemExit(status)
