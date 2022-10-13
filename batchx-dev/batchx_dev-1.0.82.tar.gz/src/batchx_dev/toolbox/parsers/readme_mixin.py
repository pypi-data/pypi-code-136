from pathlib import Path
from ..utils import URLS


class ReadMeMixin:
    section_headers = dict(
        context="# Context",
        inputs="# Inputs",
        outputs="# Outputs",
        examples="# Examples",
        links="# Links",
        tool_versions="# Tool versions",
    )

    intra_section_separator = "\n\n"
    inter_section_separator = intra_section_separator + "\n"

    documentation_urls = URLS

    # Generate sections
    def readme_title(self):
        return self.title

    def readme_context(self):
        h1 = self.section_headers.get("context")
        return h1

    def readme_inputs(self):
        contents = []

        h1 = self.section_headers.get("inputs")

        if len(self.required_inputs) > 0:
            # Depending on one or multiple int
            h2 = "## Required inputs\n\nThis tool has the following **required** {i}:".format(
                i="input" if len(self.required_inputs) == 1 else "inputs"
            )
            ri = []
            for i, n in enumerate(self.required_inputs):
                l = self._single_parameter_string(name=n, index=i + 1, kind="inputs")
                ri.append(l)
            ri = self.intra_section_separator.join(ri)
            contents.extend([h2, ri])

        if len(self.optional_inputs) > 0:
            h3 = "## Optional inputs\n\nThis tool provides additional configuration through the following **optional** {i}:".format(
                i="input" if len(self.optional_inputs) == 1 else "inputs"
            )
            oi = []
            for i, n in enumerate(self.optional_inputs):
                l = self._single_parameter_string(name=n, index=i + 1, kind="inputs")
                oi.append(l)
            oi = self.intra_section_separator.join(oi)
            contents.extend([h3, oi])

        if len(contents) > 0:
            contents = [h1] + contents
            return self.intra_section_separator.join(contents)
        else:
            return ""

    def _single_parameter_string(self, name: str, index: int = 1, kind="inputs"):
        parameter = getattr(self, kind).get(name)
        def_value = parameter.get("default", None)

        l = "{i}. **`{n}`**\n\n    {d}".format(i=index, n=name, d=parameter.description)

        if def_value is not None:
            a = " (default: `{v}`).".format(v=def_value)

            # if necessary, remove full stop at end of `l`, before adding `a`.
            l = l.rstrip(".") + a
        else:
            pass

        return l

    def readme_outputs(self):
        contents = []

        h1 = self.section_headers.get("outputs")

        if len(self.required_outputs) > 0:
            h2 = "## Required outputs\n\nThis tool will **always** provide the following {o}:".format(
                o="output" if len(self.required_outputs) == 1 else "outputs"
            )
            ro = []
            for i, n in enumerate(self.required_outputs):
                l = self._single_parameter_string(name=n, index=i + 1, kind="outputs")
                ro.append(l)
            ro = self.intra_section_separator.join(ro)
            contents.extend([h2, ro])

        if len(self.optional_outputs) > 0:
            h3 = "## Optional outputs\n\nThis tool will **optionally** provide the following {o}:".format(
                o="output" if len(self.optional_outputs) == 1 else "outputs"
            )
            oo = []
            for i, n in enumerate(self.optional_outputs):
                l = self._single_parameter_string(name=n, index=i + 1, kind="outputs")
                oo.append(l)
            oo = self.intra_section_separator.join(oo)
            contents.extend([h3, oo])

        if len(contents) > 0:
            contents = [h1] + contents
            return self.intra_section_separator.join(contents)
        else:
            return ""

    def readme_examples(self):
        h1 = self.section_headers.get("examples")
        return h1

    def readme_links(self):
        h1 = self.section_headers.get("links")
        return h1

    def readme_versions(self):
        h1 = self.section_headers.get("tool_versions")
        return h1

    # Write Readme
    def write_sections(self):
        generators = dict(
            title=self.readme_title,
            context=self.readme_context,
            inputs=self.readme_inputs,
            outputs=self.readme_outputs,
            examples=self.readme_examples,
            links=self.readme_links,
            tool_versions=self.readme_versions,
        )
        sections = {k: g() for k, g in generators.items()}
        return sections

    def write(self, sections, file: str | Path = "readme.md"):

        if file is None:
            return self.inter_section_separator.join(list(sections.values()))
        else:
            with open(file, "w") as f:
                print(self.write(sections, file=None), file=f)
            return "Wrote auto-generated readme stub to {}".format(file)

    # Read Readme
    def read_sections(self, file: str | Path = "readme.md"):
        with open(file, "r") as f:
            lines = f.readlines()

        sections = {k: "" for k in self.section_headers.keys()}
        sections["title"] = ""
        active_section = "title"

        for l in lines:
            if l.startswith("#"):
                for k, v in self.section_headers.items():
                    if l.startswith(v):
                        active_section = k

            sections[active_section] = sections[active_section] + l

        sections = {k: s.rstrip("\n") for k, s in sections.items()}

        return sections

    # alias
    def readme(self, file: str | Path = "readme.md", overwrite=False):
        if file is None:
            sections = self.write_sections()
            return self.write(sections, file=file)
        elif overwrite or not Path(file).exists():
            sections = self.write_sections()
            return self.write(sections, file=file)
        else:
            old_sections = self.read_sections(file)
            new_sections = self.write_sections()

            sections = dict(
                title=new_sections.get("title"),
                context=old_sections.get("context"),
                inputs=new_sections.get("inputs"),
                outputs=new_sections.get("outputs"),
                examples=old_sections.get("examples"),
                links=old_sections.get("links"),
                tool_versions=old_sections.get("tool_versions"),
            )
            return self.write(sections, file=file)
