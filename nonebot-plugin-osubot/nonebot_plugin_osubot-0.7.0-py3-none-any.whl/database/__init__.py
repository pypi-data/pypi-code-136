from tortoise import Tortoise
from nonebot.log import logger
from pathlib import Path

db = Path() / 'data' / 'osu' / 'osu.sqlite'

DATABASE = {
    "connections": {
        'osu': {
            "engine": "tortoise.backends.sqlite",
            "credentials": {"file_path": db},
        },
    },
    "apps": {
        "osu": {
            "models": ['nonebot_plugin_osubot.database.models'],
            "default_connection": "osu",
        }
    },
}


async def connect():
    """
    建立数据库连接
    """
    if not db.exists():
        db.parent.mkdir(parents=True, exist_ok=True)
    try:
        await Tortoise.init(DATABASE)
        await Tortoise.generate_schemas()
        logger.opt(colors=True).success("<u><y>[数据库]</y></u><g>连接成功</g>")
    except Exception as e:
        logger.opt(colors=True).warning(f"<u><y>[数据库]</y></u><r>连接失败:{e}</r>")
        raise e


async def disconnect():
    """
    断开数据库连接
    """
    await Tortoise.close_connections()
    logger.opt(colors=True).success("<u><y>[数据库]</y></u><r>连接已断开</r>")
