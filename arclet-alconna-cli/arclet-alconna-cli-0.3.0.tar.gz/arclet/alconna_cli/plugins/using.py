from arclet.alconna import Option as Option  # noqa
from arclet.alconna import Arpamar, Alconna, CommandMeta, Args, ArgField, AllParam, config
from clilte import BasePlugin, PluginMetadata, CommandLine
from .cache import Cache


class Using(BasePlugin):
    def _init_plugin(self) -> Alconna:
        return Alconna(
            "using",
            Args["command#尝试使用的命令", AllParam, ArgField(completion=lambda: "foo bar")],
            meta=CommandMeta("依据创建的 Alconna 来解析输入的命令")
        )

    def dispatch(self, result: Arpamar):
        cache = CommandLine.current().get_plugin(Cache)
        command = result.command
        try:
            construct_command = cache.data['create']
        except KeyError:
            return print(config.lang.cli_command_not_found)
        using_result = {}
        exec(f"alc = {construct_command}", globals(), using_result)
        alc: Alconna = using_result['alc']
        alc.reset_namespace(f"{self.cli_name}/USING")
        res = alc.parse(' '.join(command))
        if res.matched:
            return print(config.lang.cli_command_matched.format(
                header=result.header,
                main_args=result.main_args,
                options=result.options,
                all_args=result.all_matched_args
            ))
        return print(config.lang.cli_command_not_matched.format(
            data=result.error_data, exception=result.error_info
        ))

    def meta(self) -> PluginMetadata:
        return PluginMetadata("using", "0.1.0", "依据创建的 Alconna 来解析输入的命令")
