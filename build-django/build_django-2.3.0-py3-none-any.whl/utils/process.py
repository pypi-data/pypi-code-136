import sys
import asyncio
from pathlib import Path
from shlex import quote
from subprocess import SubprocessError
from asyncio.subprocess import PIPE, Process
from typing import Union, Iterable

SYS_ENCODING = sys.getdefaultencoding()


async def run_cmd(
    args: Iterable[str],
    cwd: Union[str, None, Path] = None,
    **kwargs
) -> Process:
    if cwd:
        args = (
            'cd',
            quote(str(cwd)),
            '&&',
            *args
        )

    cmd = ' '.join(args)

    kwargs = {
        'stdout': PIPE,
        'stderr': PIPE,
        **kwargs
    }

    process = await asyncio.create_subprocess_shell(cmd, **kwargs)

    result = await process.communicate()

    out, err = [
        item.decode(SYS_ENCODING)
        if isinstance(item, bytes) else item for item in result
    ]

    code = process.returncode

    if code != 0:
        raise SubprocessError(f'{code}: {err}')

    if out:
        print(out)

    return process
