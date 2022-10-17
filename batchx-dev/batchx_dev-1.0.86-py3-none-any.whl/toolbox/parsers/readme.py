import json
import re
from pathlib import Path

import mistletoe
from mistletoe.ast_renderer import ASTRenderer


class MarkdownLoaderMixin:
    _INITIAL_SECTION_NAME = "Title"

    # load-methods
    def load(self):
        self.load_lines()
        self.load_ast()
        self.load_dict()
        return

    def load_lines(self):
        with open(self.fp, "r") as f:
            lines = f.readlines()

        self._lines = lines
        return

    def load_ast(self):

        with open(self.fp, "r") as f:
            ast = mistletoe.markdown(f, renderer=ASTRenderer)

        self._ast = json.loads(ast)

        return

    def load_dict(self):
        contents = dict()
        active_section = self._INITIAL_SECTION_NAME
        for l in self._lines:
            for (h, level), r in self.regexes.items():
                if re.match(r, l):
                    active_section = h
                else:
                    pass

            if contents.get(active_section) is None:
                contents[active_section] = [l]
            else:
                contents[active_section].append(l)

        self.__dictionary__ = contents
        return

    # save-methods
    def serialize(self):
        lines = []
        for k, l in self.items():
            lines.extend(l)
        return lines

    def save(self, fp: str | Path | None = None, return_fp: bool = False):
        if fp is None:
            fp = self.fp

        with open(fp, "w") as f:
            f.writelines(self.serialize())

        print("Saved file to: {}".format(fp))
        if return_fp: 
            return fp
        else:
            return 

    # mirror dict behavior
    def dict(self):
        return self.__dictionary__

    # dict-like behavior
    def keys(self):
        return self.dict().keys()

    def values(self):
        return self.dict().values()

    def items(self):
        return self.dict().items()

    def get(self, key, default=None):
        return self.dict().get(key, default)

    # properties
    @property
    def fp(self):
        return getattr(self, "_fp", None)

    @fp.setter
    def fp(self, value: str | Path):
        assert isinstance(value, str | Path), "Must be filepath."
        self._fp = Path(value)
        return

    @property
    def headings(self):
        def _get_headings(children: list[dict] | dict):
            if isinstance(children, dict):
                children = [children]
            headings = []
            for c in children:
                c_type = c.get("type")
                c_level = c.get("level")
                c_children = c.get("children", [])
                if c_type == "Heading":
                    header = c_children[0].get("content")
                    headings.append((header, c_level))
                else:
                    pass

                headings.extend(_get_headings(c_children))
            return headings

        headings = _get_headings(self._ast)
        headings.insert(0, (self._INITIAL_SECTION_NAME, 1))  # Title is not part of AST
        headings = [(h, l) for h, l in headings if h is not None]
        return headings

    @property
    def regexes(self):
        def _regex(header: str, level: int):
            return r"#{{{l}}}\s*{h}[^\S\r\n]*[\n]".format(l=level, h=header.strip())

        return {(h, l): _regex(h, l) for h, l in self.headings}

    @property
    def markdown(self):
        return getattr(self, "_markdown", None)

    @markdown.setter
    def markdown(self, value: str | Path):
        self.fp = value
        self.load()
        return


class Readme(MarkdownLoaderMixin):
    def __init__(self, readme_fp: str | Path):
        self.fp = readme_fp
        self.load()
        return
