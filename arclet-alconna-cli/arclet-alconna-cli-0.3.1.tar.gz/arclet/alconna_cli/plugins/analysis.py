import re
from arclet.alconna import Arpamar, Alconna, CommandMeta, Args, ArgField, AllParam
from nepattern import pattern_map
from clilte import BasePlugin, PluginMetadata, CommandLine
from typing import List
from .cache import Cache


class Analysis(BasePlugin):
    def _init_plugin(self) -> Alconna:
        return Alconna(
            "analysis",
            Args["command", AllParam, ArgField(completion=lambda: "输入单行命令")],
            meta=CommandMeta("分析命令并转换为 Alconna 命令结构")
        )

    def dispatch(self, result: Arpamar):
        cache = CommandLine.current().get_plugin(Cache)
        command_parts: List[str] = result.command
        res = {}
        command_headers = command_parts.pop(0)
        if re.match(r"\W.*?", command_headers):
            res['header'] = [command_headers[0]]
            res['command'] = command_headers[1:]
        else:
            res['command'] = command_headers
        res['options'] = []
        for i, part in enumerate(command_parts):
            if not part.startswith("--"):
                continue
            _option = {"type": "Option", "name": part}
            _args = {}
            _arg_index = 0
            while i < len(command_parts) - 1:
                i += 1
                _arg_index += 1
                if command_parts[i].startswith("--"):
                    break
                _arg_key = f"{part[2:]}_arg_{_arg_index}"
                for k, v in pattern_map.items():
                    if not isinstance(k, str) or k == 'str':
                        continue
                    if v.validate(command_parts[i]).success:
                        command_parts[i] += f"%{k}" if v.origin != str else f"\"{k}\""
                        break
                else:
                    command_parts[i] += "%str"
                _args[_arg_key] = command_parts[i]
            if _args:
                _option['args'] = _args
            res['options'].append(_option)
        cache.data["analysis"] = res
        cache.save()
        print(res)

    def meta(self) -> PluginMetadata:
        return PluginMetadata("analysis", "0.1.0", "分析命令并转换为 Alconna 命令结构", ["dev"], ["RF-Tar-Railt"])
