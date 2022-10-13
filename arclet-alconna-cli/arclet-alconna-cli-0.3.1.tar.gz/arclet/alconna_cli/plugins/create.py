import re
from nepattern import BasePattern, PatternModel
from arclet.alconna import Arpamar, Alconna, Option, Args, CommandMeta, ArgField
from clilte import BasePlugin, PluginMetadata, CommandLine
from typing import List
from .cache import Cache

args_type = BasePattern(
    r"(\[.+])*",
    PatternModel.REGEX_CONVERT,
    list,
    lambda _, x: [re.split("[:=]", p) for p in re.findall(r"\[(.*?)]", x)],
)


class Create(BasePlugin):
    def _init_plugin(self) -> Alconna:
        return Alconna(
            "create",
            Option("--command", Args["command_name", str], help_text="指定命令名称"),
            Option("--header", Args["command_header", List[str]], help_text="传入命令头"),
            Option(
                "--args",
                Args["main_args", args_type, ArgField(default_factory=list)],
                help_text="传入主参数",
            ),
            Option(
                "--option",
                Args["option_name", str][
                    "option_args", args_type, ArgField(default_factory=list)
                ],
                help_text="创建命令选项",
            ),
            Option("--analysed|-A", help_text="从已经分析的命令结构中创建Alconna"),
            meta=CommandMeta("开始创建 Alconna 命令"),
        )

    def analysed(self, result: Arpamar):
        cache = CommandLine.current().get_plugin(Cache)
        try:
            analysed_args = cache.data["analysis"]
        except KeyError:
            print("请先分析命令")
            return
        header_text = analysed_args.get("header")
        args_text = analysed_args.get("main_args")
        options = analysed_args.get("options")
        command_name = analysed_args.get("command")
        option_text = ""
        if options:
            option_text = "\n    options=[\n"
            for option in options:
                _opt_name = option.get("name")
                if _opt_args := option.get("args"):
                    _opt_args_text = "Args["
                    for _opt_arg_name, _opt_arg_value in _opt_args.items():
                        _opt_args_text += (
                            f"\"{_opt_arg_name}\": {_opt_arg_value.split('%')[1]}, "
                        )
                    _opt_args_text = f"{_opt_args_text[:-2]}]"
                    _opt = f'\tOption("{_opt_name}", {_opt_args_text}),\n'
                else:
                    _opt = f'\tOption("{_opt_name}"),\n'
                option_text += _opt
            option_text = option_text[:-2] + "\n    ],"

        if header_text:
            construct_command = (
                f"Alconna(\n"
                f"    header={header_text},\n"
                f'    command="{command_name}",'
                f"    {option_text}\n"
                f")"
            )
        else:
            construct_command = (
                f"Alconna(\n"
                f'    command="{command_name}",'
                f"    {option_text}\n"
                f")"
            )
        print(construct_command)
        cache.data["create"] = construct_command
        cache.save()
        return

    def dispatch(self, result: Arpamar):
        cache = CommandLine.current().get_plugin(Cache)
        if result.find("analysed"):
            return self.analysed(result)
        command = result.query("command.args")
        option = result.query("option.args")
        header = result.query("header.args")
        if not command:
            print("你没有指定命令名称")
            return
        option_texts = []
        if option:
            if isinstance(option, list):
                for o in option:
                    opt_name = o["option_name"]
                    if o["option_args"]:
                        arg_text = "["
                        for arg in o["option_args"]:
                            arg[1] = (
                                f'"{arg[1]}"'
                                if arg[1] not in ["str", "int", "float", "bool", "..."]
                                else arg[1]
                            )
                            arg_text += f'"{arg[0]}":{arg[1]}, '
                        arg_text = f"{arg_text[:-2]}]"
                        option_texts.append(f'Option("{opt_name}", Args{arg_text}),')
                    else:
                        option_texts.append(f'Option("{opt_name}"),')
            else:
                opt_name = option["option_name"]
                if option["option_args"]:
                    arg_text = "["
                    for arg in option["option_args"]:
                        arg[1] = (
                            f'"{arg[1]}"'
                            if arg[1] not in ["str", "int", "float", "bool", "..."]
                            else arg[1]
                        )
                        arg_text += f'"{arg[0]}":{arg[1]}, '
                    arg_text = f"{arg_text[:-2]}]"
                    option_texts.append(f'Option("{opt_name}", Args{arg_text}),')
                else:
                    option_texts.append(f'Option("{opt_name}"),')
        option_text = (
            ("\n    options=[\n\t" + "\n\t".join(option_texts) + "\n    ],")
            if option_texts
            else ""
        )
        if header:
            header_text = "["
            for h in header:
                header_text += f'"{h}", '
            header_text = f"{header_text[:-2]}]"
            construct_command = (
                f"Alconna(\n"
                f"    header={header_text},\n"
                f"    command=\"{command['command_name']}\","
                f"    {option_text}\n"
                f") "
            )
        else:
            construct_command = (
                f"Alconna(\n"
                f"    command=\"{command['command_name']}\","
                f"    {option_text}\n"
                f")"
            )
        print(construct_command)
        cache.data["create"] = construct_command
        cache.save()

    def meta(self) -> PluginMetadata:
        return PluginMetadata("create", "0.1.0")
