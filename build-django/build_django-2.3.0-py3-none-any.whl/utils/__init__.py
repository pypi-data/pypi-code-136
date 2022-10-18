import secrets
import asyncio
from shlex import quote
from typing import Iterable

import aiofiles

from .process import run_cmd, Process
from .files import write_file


def generate_env(debug: bool = False, hosts: str = '*') -> str:
    items = [
        f'SECRET_KEY={secrets.token_hex(128)}',
        f'ALLOWED_HOSTS={hosts}'
    ]

    if debug:
        items.append('DEBUG=True')

    return '\n\n'.join(items)


def edit_settings(lines: Iterable[str]) -> list[str]:
    result = []

    for line in lines:
        if line.startswith('BASE_DIR'):
            result.append('\nfrom environ import Env\n')

            result.append(f'\n{line}\n')

            result.append('\nenv = Env(DEBUG=(bool, False))\n')
            
            result.append('\nEnv.read_env(BASE_DIR / \'.env\')\n')

        elif line.startswith('SECRET_KEY'):
            result.append(f'SECRET_KEY = env(\'SECRET_KEY\')\n')
        elif line.startswith('ALLOWED_HOSTS'):
            result.append('ALLOWED_HOSTS = env.tuple(\'ALLOWED_HOSTS\')')
        elif line.startswith('DEBUG'):
            result.append('DEBUG = env(\'DEBUG\')\n')
        else:
            result.append(line)

    return result


async def write_settings(path: str):
    async with aiofiles.open(path, 'r+') as file:
        lines = await file.readlines()

        result = edit_settings(lines)

        await file.seek(0)

        await file.writelines(result)


async def write_requirements(path: str, pip_path: str):
    async with aiofiles.open(path, 'w') as file:
        await run_cmd((pip_path, 'freeze'), stdout=file)


async def install_package(pip_path: str, package: str, *args: str) -> Process:
    return await run_cmd((
        pip_path,
        'install',
        '--require-virtualenv',
        '-v',
        '--disable-pip-version-check',
        *args,
        quote(package)
    ))


async def install_packages(
    pip_path: str,
    packages: Iterable[str],
    *args: str
) -> list[Process]:
    added = set()

    tasks = []

    for package in packages:
        if package in added:
            continue

        added.add(package)

        tasks.append(install_package(pip_path, package, *args))

    return await asyncio.gather(*tasks)
