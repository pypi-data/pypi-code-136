import re
from pathlib import Path

from ..parsers import Readme
from .guidelines import ChecksMixin, EnrichmentsMixin, FixesMixin
from .renderers import RendersMixin


class ReadmeImproverInspectorMixin:
    def collect_subsections(self, section: str, include_section_itself: bool = True):
        subsections = []
        inside = False
        for h, l in self.rm.headings:
            if h == section:
                # encountered the section itself (from this point on, we are 'inside the section')
                section_level = l
                inside = True
                if include_section_itself:
                    subsections.append(h)
            elif inside == True and l > section_level:
                # if we were inside, and the next section has a higher level of indent => it is an actual subsection
                subsections.append(h)
            elif inside == True and l <= section_level:
                # if we were inside, and the next section does not have a higher level of indent => it is a sibling or even parent => we are no longer 'inside the section'
                inside = False
            else:
                # we were not inside, so whatever we encounter cannot be a subsection
                pass

        return subsections

    def collect_content(
        self,
        section: str,
        include_subsections: bool = True,
        filter_headings: bool = True,
        filter_whitespace: bool = True,
    ):
        content = []

        if include_subsections:
            subsections = self.collect_subsections(section, include_section_itself=True)
        else:
            subsections = [section]

        for s in subsections:
            subsection_content = self.rm.dict().get(s, [])
            if filter_headings and len(subsection_content) > 0:
                subsection_content = subsection_content[1:]

            if filter_whitespace:
                subsection_content = [
                    l for l in subsection_content if not re.match(r"\s+", l)
                ]
            content.extend(subsection_content)

        return content

    def remove_content(
        self,
        section: str,
        include_subsections: bool = True,
        keep_headings: bool = True,
    ):
        if include_subsections:
            subsections = self.collect_subsections(section, include_section_itself=True)
        else:
            subsections = [section]

        for s in subsections:
            subsection_content = self.rm.dict().get(s, [])
            if keep_headings and len(subsection_content) > 0:
                subsection_content = subsection_content[0:1]
            else:
                subsection_content = []

            self.rm.dict()[s] = subsection_content

        return

    @property
    def platform_defined_sections(self) -> list[str]:
        return getattr(self, "_platform_defined_sections", None)

    @platform_defined_sections.setter
    def platform_defined_sections(
        self, value: list[str] | tuple[str] | set[str]
    ) -> None:
        value = list(value)

        platform_defined_sections = []
        for e in value:
            platform_defined_sections.extend(self.collect_subsections(e))

        self._platform_defined_sections = list(set(platform_defined_sections))
        return

    @property
    def user_defined_sections(self) -> list[str]:
        return list(
            set(
                [
                    s
                    for s in self.rm.dict().keys()
                    if s not in self.platform_defined_sections
                ]
            )
        )


class ReadmeImprover(
    ChecksMixin,
    FixesMixin,
    EnrichmentsMixin,
    RendersMixin,
    ReadmeImproverInspectorMixin,
):
    def __init__(
        self,
        readme_fp: str | Path | None = None,
        readme: Readme | None = None,
        platform_defined_sections=(
            "Title",
            "Inputs",
            "Outputs",
            "Pipeline overview",
            "Pipeline steps",
        ),
        verbose: bool = True,
    ):
        if readme_fp is not None:
            self.readme = Readme(readme_fp)
        elif readme is not None:
            self.readme = readme
        else:
            raise ValueError("Need a readme filepath or readme.")

        self.fp = self.rm.fp
        self.platform_defined_sections = platform_defined_sections
        self.verbose = verbose

        self.fixes = dict()
        self.checks = dict()
        self.enrichments = dict()
        self.renders = dict()
        return

    def do_improvements(
        self, input_objects: list[object], key: str | None = None
    ) -> list[object]:
        output_objects = [None] * len(input_objects)
        for idx, input_object in enumerate(input_objects):
            intermediate_object = input_object

            self.do_checks(intermediate_object, key=key)
            intermediate_object = self.do_fixes(intermediate_object, key=key)
            intermediate_object = self.do_enrichments(intermediate_object, key=key)

            output_objects[idx] = intermediate_object
        return output_objects

    def improve_lines(
        self,
        sources: list[str],
        targets: list[str] | None = None,
        key: str = "user_defined_sections",
        overwrite: bool = True,
    ):
        if targets is None:
            targets = sources

        for idx, src in enumerate(sources):
            tgt = targets[idx]

            # here is one of the few places we differ from the ManifestImprover
            old_val_src = self.rm.dict().get(src, [])  # list of lines
            old_val_tgt = self.rm.dict().get(tgt, [])  # list of lines

            new_val_src = self.do_improvements(old_val_src, key=key)

            change = old_val_src != new_val_src
            if overwrite:
                self.rm.dict()[tgt] = new_val_src
            elif change and len(old_val_tgt) == 0:
                # if there is a change and the target is empty
                self.rm.dict()[tgt] = new_val_src
            else:
                pass
        return

    def generate_section(
        self,
        target: str = "Input",
        key: str | None = None,
        erase_subsections: bool = True,
        requires_empty_target: bool = False,
    ):
        if key is None:
            key = target

        preconditions = [target in self.renders]

        if requires_empty_target:
            target_content = self.collect_content(target)
            preconditions.append(len(target_content) == 0)

        if all(preconditions):
            if erase_subsections:
                # First erase existing content before creating novel content.
                subsections = self.collect_subsections(
                    target, include_section_itself=False
                )
                for subsection in subsections:
                    self.rm.dict().pop(subsection, None)
            else:
                pass

            generated_content = self.do_renders(key=key)
            self.rm.dict()[target] = generated_content

            if self.verbose:
                msg = """
                Generated section: {s}
                """.format(
                    s=target
                )
                print(msg)

        return

    def improve_user_defined_sections(self):
        return self.improve_lines(
            sources=self.user_defined_sections, key="user_defined_sections"
        )

    def improve_platform_defined_sections(self):
        for section in self.platform_defined_sections:
            self.improve_lines(sources=[section], key=section)
        return

    def generate_platform_defined_sections(self):
        for section in self.platform_defined_sections:
            self.generate_section(target=section, erase_subsections=True)

        return

    def draft_user_defined_sections(self):
        for section in self.user_defined_sections:
            if self.verbose:
                print("Generating content for {}".format(section))
            self.generate_section(
                target=section, erase_subsections=True, requires_empty_target=True
            )

        return

    # properties
    @property
    def rm(self):
        # alias
        return self.readme

    @rm.setter
    def rm(self, value):
        # alias
        self.readme = value
        return

    @property
    def readme(self):
        return getattr(self, "_readme", None)

    @readme.setter
    def readme(self, value):
        if isinstance(value, Readme):
            self._readme = value
        else:
            raise TypeError("readme attribute only accepts Readme object.")
