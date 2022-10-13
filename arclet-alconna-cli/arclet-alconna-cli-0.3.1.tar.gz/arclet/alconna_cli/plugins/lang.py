from arclet.alconna import Arpamar, Alconna, Option, CommandMeta, Args, ArgField, config
from clilte import BasePlugin, PluginMetadata


class Lang(BasePlugin):
    def _init_plugin(self) -> Alconna:
        return Alconna(
            "lang",
            Option("--list", help_text="展示所有支持的语言类型"),
            Option(
                "--set-default|-S",
                Args["lang", str, ArgField(completion=lambda: "比如 zh-CN")],
                help_text="设置默认使用的语言类型",
            ),
            meta=CommandMeta("语言配置相关功能")
        )

    def dispatch(self, result: Arpamar):
        if result.find('list'):
            return print(config.lang.types)
        if result.find("set-default"):
            try:
                config.lang.change_type(result.lang)
                print(config.lang.cli_lang_type_set_success.format(type=result.lang))
                return
            except ValueError:
                print(config.lang.cli_lang_type_set_failed)
        return print(self.command.get_help())

    def meta(self) -> PluginMetadata:
        return PluginMetadata("lang", "0.1.0", "语言配置相关功能", ["lang", "dev"], ["RF-Tar-Railt"])
