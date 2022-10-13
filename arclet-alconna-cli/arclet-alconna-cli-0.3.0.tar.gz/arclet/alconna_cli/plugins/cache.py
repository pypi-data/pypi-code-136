import json
import os
from typing import Dict, Any
from arclet.alconna import Arpamar, Alconna, Option, CommandMeta
from clilte import BasePlugin, PluginMetadata
from pathlib import Path


class Cache(BasePlugin):
    path: Path
    data: Dict[str, Any]

    def _init_plugin(self) -> Alconna:
        self.path = Path('.alc_cli.json')
        if self.path.exists():
            with self.path.open('r+', encoding='UTF-8') as f_obj:
                self.data = json.load(f_obj)
        else:
            self.data = {}
        return Alconna(
            "cache",
            Option("clear", help_text="清理缓存"),
            Option("show", help_text="显示内容"),
            meta=CommandMeta("管理缓存")
        )

    def dispatch(self, result: Arpamar):
        if result.find("show"):
            print(f'in "{os.getcwd()}{os.sep}{self.path.name}":')
            return print(self.data)
        if result.find("clear"):
            self.data.clear()
            if self.path.exists():
                print(f"removed {os.getcwd()}{os.sep}{self.path.name}.")
                return self.path.unlink(True)
            return print("cache cleared")
        return print(self.command.get_help())

    def meta(self) -> PluginMetadata:
        return PluginMetadata("cache", "0.1.0", "管理缓存", ["cache", "dev"], ["RF-Tar-Railt"])

    def save(self):
        with self.path.open('w+', encoding='UTF-8') as f_obj:
            json.dump(self.data, f_obj, ensure_ascii=False, indent=4)
