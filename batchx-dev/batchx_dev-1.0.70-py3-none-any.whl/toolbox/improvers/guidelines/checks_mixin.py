from functools import partial

from ..functiondict_mixin import FunctionDictMixin


class Checks:
    @property
    def available_checks(self):
        return dict(
            formal_style=self.formal_style,
            avoid_the_word_image=self.avoid_the_word_image,
            consistent_tool_reference=self.consistent_tool_reference,
        )

    def formal_style(self, line: str, verbose: bool | None = None) -> str:
        if verbose is None:
            verbose = self.verbose

        if line.find(" you ") > -1 or line.find(" we ") > -1:
            if verbose:
                msg = """
                [STYLE GUIDE] Prefer formal style: avoid "you" or "we".
                    CONSIDER REWRITING THIS: 
                        {l}
                """.format(
                    l=line
                )
                print(msg)
        else:
            pass
        return line

    def avoid_the_word_image(self, line: str, verbose: bool | None = None) -> str:
        if verbose is None:
            verbose = self.verbose

        if line.find(" image") > -1:
            if verbose:
                msg = """
                [STYLE GUIDE] Avoid using the word "image" to refer to a tool.
                    DOUBLE-CHECK THIS: 
                        {l}
                """.format(
                    l=line
                )
                print(msg)
        else:
            pass
        return line

    def consistent_tool_reference(
        self,
        line: str,
        tool_name: str,
        tool_version: str,
        window: int = 40,
        verbose: bool | None = None,
    ) -> str:
        if verbose is None:
            verbose = self.verbose

        def _fetch_excerpt(line: str, idx: int, window: int = 40):
            start_idx = max(idx - window, 0)
            stop_idx = min(idx + window, len(line) - 1)
            excerpt = line[start_idx:stop_idx]
            return excerpt

        tool_name_str = "{n}:".format(n=tool_name)
        tool_name_and_version_str = "{tns}{v}".format(tns=tool_name_str, v=tool_version)
        if (
            line.find(tool_name_str) > -1
            and not line.find(tool_name_and_version_str) > -1
        ):
            idx = line.find(tool_name_str)
            excerpt = _fetch_excerpt(line, idx, window=window)

            if verbose:
                msg = """
                [INCONSISTENCY ALERT] Version number in manifest does not match a detected tool reference
                    COMPARE THIS TEXT: {e}

                    MANIFEST VERSION: {v}
                """.format(
                    e=excerpt, v=tool_version
                )
                print(msg)
        else:
            pass
        return line


class ChecksMixin(Checks, FunctionDictMixin):
    def do_checks(self, line: str, key: str | None = None) -> None:
        """Do all checks. This will not transform anything, but warns you if something maybe could be done better."""

        return self.do_functions(line, key=key, kind="checks")

    def add_check(
        self,
        check: str,
        key: str | None = None,
        **kwargs,
    ):
        return self.add_function(function=check, key=key, kind="checks", **kwargs)

    def add_checks(
        self,
        checks: list[str],
        key: str | None = None,
        **kwargs,
    ):
        for check in checks:
            self.add_check(check, key=key, **kwargs)
        return

    def add_all_checks(self, key: str | None = None, **kwargs):
        """
        Associate all available checks with a particular key.

        Args:
            key (str | None, optional): Key for this collection of checks. Defaults to None.
        """
        return self.add_checks(self.available_checks, key=key, **kwargs)
