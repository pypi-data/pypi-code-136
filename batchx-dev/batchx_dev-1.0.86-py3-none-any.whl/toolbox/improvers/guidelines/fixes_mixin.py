from functools import partial

from ..functiondict_mixin import FunctionDictMixin


class Fixes:
    @property
    def available_fixes(self):
        return dict(
            stylize_latin_abbreviations=self.stylize_latin_abbreviations,
            no_spaces_before_a_colon=self.no_spaces_before_a_colon,
            avoid_contractions=self.avoid_contractions,
        )

    def stylize_latin_abbreviations(
        self, line: str, verbose: bool | None = None
    ) -> str:
        """
        Automagically add commas after 'i.e.' and 'e.g.'

        Note that such double punctuation (for example: 'e.g.,') is still a matter of active debate.
        Long story short, it almost always happens in American English and tends to be avoided in British English.

        Hence, this function enforces the American convention, not a universal truth.

        However, regional conventions aside, this function also enforces **consistency** across the documentation,
        which is a virtue by itself.

        See [here](https://english.stackexchange.com/questions/16172/should-i-always-use-a-comma-after-e-g-or-i-e)
        for a very informative discussion (which links to various authoratative sources) on this topic.

        Args:
            line (str): Line to be checked and modified if appropriate.
        """
        if verbose is None:
            verbose = self.verbose

        new_line = (
            line.replace("i.e. ", "i.e., ")
            .replace("I.e. ", "I.e., ")
            .replace("e.g. ", "e.g., ")
            .replace("E.g. ", "E.g., ")
        )
        if new_line != line and verbose:
            msg = """
            [STYLE GUIDE] Follow American convention for latin abbreviations; write 'i.e.,' and 'e.g.,'. 
                REPLACED THIS: 
                    {l}
                BY THIS:
                    {n}
            """.format(
                l=line, n=new_line
            )
            print(msg)
        return new_line

    def no_spaces_before_a_colon(self, line: str, verbose: bool | None = None) -> str:
        if verbose is None:
            verbose = self.verbose

        new_line = line.replace(" :", ":")

        if new_line != line and verbose:
            msg = """
            [STYLE GUIDE] Do not leave a space in front of a colon.
                REPLACED THIS: 
                    {l}
                BY THIS:
                    {n}
            """.format(
                l=line, n=new_line
            )
            print(msg)
        return new_line

    def avoid_contractions(self, line: str, verbose: bool | None = None) -> str:
        if verbose is None:
            verbose = self.verbose

        new_line = line.replace("n't", " not").replace("'ll", " will")

        if new_line != line and verbose:
            msg = """
            [STYLE GUIDE] Avoid contractions such as can't, don't, etc.
                REPLACED THIS: 
                    {l}
                BY THIS:
                    {n}
            """.format(
                l=line, n=new_line
            )
            print(msg)
        return new_line


class FixesMixin(Fixes, FunctionDictMixin):
    def do_fixes(self, line, key: str | None = None) -> str:
        """Do all fixes. This may or may not involve transforming the manifest."""
        return self.do_functions(line, key=key, kind="fixes")

    def add_fix(
        self,
        fix: str,
        key: str | None = None,
        **kwargs,
    ):

        return self.add_function(function=fix, key=key, kind="fixes", **kwargs)

    def add_fixes(
        self,
        fixes: list[str],
        key: str | None = None,
        **kwargs,
    ):
        for fix in fixes:
            self.add_fix(fix, key=key, **kwargs)
        return

    def add_all_fixes(self, key: str | None = None, **kwargs):
        """
        Associate all available fixes with a particular key.

        Args:
            key (str | None, optional): Key for this collection of fixes. Defaults to None.
        """
        return self.add_fixes(self.available_fixes, key=key, **kwargs)
