from typing import AnyStr

import aiofiles


async def write_file(path: str, content: AnyStr, mode: str = 'w'):
    async with aiofiles.open(path, mode) as file:
        await file.write(content)
