from pathlib import Path

import jinja2
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..functiondict_mixin import FunctionDictMixin

ROOT = Path(__file__).absolute().parent.parent
TEMPLATE_DP = ROOT / "templates"


class Templates:
    # properties
    @property
    def available_templates(self):
        return {t.stem: t.name for t in self.template_dp.glob("*.jinja")}

    @property
    def active_template(self):
        return getattr(self, "_active_template", None)

    @active_template.setter
    def active_template(self, value: str | None):
        if value is None:
            if self.is_pipeline:
                value = "pipeline-inputs.jinja"
            else:
                value = "tool-inputs.jinja"
        elif value in self.available_templates:
            value = self.available_templates.get(value)
        else:
            msg = """
            Did not find template: {v}
            Available templates:   {ts}

            Template directory:    {td}
            Does it exist?         {exists}
            Contents of template directory: {tc}


            Root directory:        {rd}
            Contents of root directory: {c}
            """.format(
                v=value,
                ts=self.available_templates,
                td=TEMPLATE_DP,
                exists=TEMPLATE_DP.exists(),
                tc=list(TEMPLATE_DP.iterdir()),
                rd=ROOT,
                c=list(ROOT.iterdir()),
            )
            raise ValueError(msg)

        self._active_template = self.jinja_environment.get_template(value)
        return

    @property
    def jinja_environment(self):
        if getattr(self, "_jinja_environment", None) is None:
            self._jinja_environment = Environment(
                loader=FileSystemLoader(self.template_dp),
                autoescape=select_autoescape(),
                trim_blocks=True,
                lstrip_blocks=True,
            )
        return self._jinja_environment


class Renders(Templates):
    template_dp = TEMPLATE_DP

    @property
    def available_renders(self):
        return dict(
            title=self.title,
            context=self.context,
            examples=self.examples,
            links=self.links,
            tool_versions=self.tool_versions,
            tool_inputs=self.tool_inputs,
            tool_outputs=self.tool_outputs,
            pipeline_inputs=self.pipeline_inputs,
            pipeline_outputs=self.pipeline_outputs,
            pipeline_overview=self.pipeline_overview,
            pipeline_steps=self.pipeline_steps,
        )

    # drafts
    def init_readme(self, is_pipeline: bool = False):
        if is_pipeline:
            return self._render(template="init-readme-pipeline", d=dict())
        else:
            return self._render(template="init-readme-tool", d=dict())

    def context(self):
        return self._render(template="context", d=dict())

    def examples(self):
        return self._render(template="examples", d=dict())

    # Draft & Manifest-defined
    def links(self, manifest_dict: dict = dict()):
        return self._render(template="links", d=manifest_dict)

    def tool_versions(self, manifest_dict: dict = dict()):
        return self._render(template="tool-versions", d=manifest_dict)

    # Manifest-defined
    def title(self, manifest_dict: dict = dict()):
        return self._render(template="title", d=manifest_dict)

    def tool_inputs(self, manifest_dict: dict = dict()):
        return self._render(template="tool-inputs", d=manifest_dict)

    def tool_outputs(self, manifest_dict: dict = dict()):
        return self._render(template="tool-outputs", d=manifest_dict)

    def pipeline_inputs(self, manifest_dict: dict = dict()):
        return self._render(template="pipeline-inputs", d=manifest_dict)

    def pipeline_outputs(self, manifest_dict: dict = dict()):
        return self._render(template="pipeline-outputs", d=manifest_dict)

    def pipeline_overview(self, steps_dict: dict = dict()):
        return self._render(template="pipeline-overview", d=steps_dict)

    def pipeline_steps(self, steps_dict: dict = dict()):
        return self._render(template="pipeline-steps", d=steps_dict)

    # underlying worker
    def _render(self, template: str, d: dict, as_lines: bool = True):
        self.active_template = template
        rendered_content = self.active_template.render(**d)
        if as_lines:
            rendered_content = rendered_content.split("\n")
            rendered_content = ["{c}\n".format(c=c) for c in rendered_content]
            return rendered_content
        else:
            return rendered_content


class RendersMixin(Renders, FunctionDictMixin):
    def do_renders(
        self, manifest_dict: dict | None = None, key: str | None = None
    ) -> None:
        return self.do_functions(manifest_dict, key=key, kind="renders")

    def add_render(
        self,
        render: str,
        key: str | None = None,
        **kwargs,
    ):
        return self.add_function(function=render, key=key, kind="renders", **kwargs)

    def add_renders(
        self,
        renders: list[str],
        key: str | None = None,
        **kwargs,
    ):
        for render in renders:
            self.add_render(render, key=key, **kwargs)
        return
