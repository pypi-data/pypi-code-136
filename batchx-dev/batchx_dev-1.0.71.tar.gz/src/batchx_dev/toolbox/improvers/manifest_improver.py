from pathlib import Path

from ..parsers import Manifest
from ..parsers.api import BxImage
from .guidelines import ChecksMixin, EnrichmentsMixin, FixesMixin


class ManifestImproverInspectorMixin:
    def replace_suffix(self, jsonpath: str, suffix: str):
        parts = jsonpath.split(".")
        parts[-1] = suffix  # replace suffix
        return ".".join(parts)

    def find_all(
        self,
        suffix: list[str] | str = "title",
        prefix: list[str] | str = "",
        contains: list[str] | str = "",
    ):
        if isinstance(contains, str):
            contains = [contains]
        if isinstance(suffix, str):
            suffix = [suffix]
        if isinstance(prefix, str):
            prefix = [prefix]

        return [
            jp
            for jp in self.mf.collect_jsonpaths()
            if any((jp.startswith(s) for s in prefix))
            if any((jp.endswith(s) for s in suffix))
            if any((c in jp for c in contains))
        ]

    def find_manifest_entries_associated_with_steps(
        self,
        steps: list[str] | dict | None = None,
        contains_prefix="tools.properties",
        suffix=["description", "title"],
    ):
        if steps is None:
            steps = self.steps

        contains = [".".join([contains_prefix, s]) for s in steps]
        return self.find_all(
            contains=contains,
            suffix=suffix,
        )

    def collect_flat_dict(self, jsonpath: str, field="default"):
        def format_key(k, jp):
            k = k.split(jp)[1]
            parts = k.split(".")
            parts = [p for p in parts if p not in {"properties", field, ""}]
            return ".".join(parts)

        all_jps = self.find_all(suffix=field)
        relevant_jps = [d for d in all_jps if d.startswith(jsonpath)]
        lowest_level_relevant_jps = []
        for d in relevant_jps:
            if (
                len(
                    [
                        e
                        for e in relevant_jps
                        if e.startswith(d.split(".{f}".format(f=field))[0])
                    ]
                )
                == 1
            ):
                lowest_level_relevant_jps.append(d)

        flat_dict = {
            format_key(jp, jsonpath): self.mf[jp] for jp in lowest_level_relevant_jps
        }
        flat_dict = {k: v for k, v in flat_dict.items() if k != ""}
        return flat_dict

    def collect_defaults(self, jsonpath: str):
        return self.collect_flat_dict(jsonpath=jsonpath, field="default")

    def collect_titles(self, jsonpath: str):
        return self.collect_flat_dict(jsonpath=jsonpath, field="title")

    def collect_descendants(
        self,
        jsonpath: str,
        key_reference_field: str = "title",
        value_reference_field: str = "default",
        dummy_value=None,
    ):
        keys = self.collect_flat_dict(jsonpath=jsonpath, field=key_reference_field)
        values = self.collect_flat_dict(jsonpath=jsonpath, field=value_reference_field)
        return {k: values.get(k, dummy_value) for k in keys}

    @property
    def titles(self):
        return self.find_all(suffix="title")

    @property
    def descriptions(self):
        return self.find_all(suffix="description")

    @property
    def required(self):
        return self.find_all(suffix="required")

    @property
    def defaults(self):
        return self.find_all(suffix="default")

    @property
    def steps(self):
        if self.mf.is_pipeline:
            if getattr(self, "_steps", None) is None:
                steps = dict()
                for step in self.mf.pipeline.steps:
                    img = BxImage(step)

                    steps[img.canonical_name] = dict(
                        step=step,
                        name=img.name,
                        title=img.title,
                        env=img.environment,
                        version=img.version,
                        urls=img.urls,
                    )
                self._steps = steps
            else:
                pass

            return self._steps
        else:
            return None


class ManifestImprover(
    ChecksMixin, FixesMixin, EnrichmentsMixin, ManifestImproverInspectorMixin
):
    def __init__(
        self,
        manifest_fp: str | Path | None = None,
        manifest: Manifest | None = None,
        verbose: bool = True,
    ):
        if manifest_fp is not None:
            self.manifest = Manifest(manifest_fp, jsonpaths=True)
        elif manifest is not None:
            self.manifest = manifest
        else:
            raise ValueError("Need a manifest filepath or manifest.")

        self.fp = self.mf.fp
        self.verbose = verbose

        self.fixes = dict()
        self.checks = dict()
        self.enrichments = dict()
        return

    def do_improvements(self, line: str, key: str | None = None) -> str:
        self.do_checks(line, key=key)
        line = self.do_fixes(line, key=key)
        line = self.do_enrichments(line, key=key)
        return line

    def improve_lines(
        self,
        sources: list[str],
        targets: list[str] | None = None,
        source_values: list[str] | None = None,
        target_values: list[str] | None = None,
        key: str = "title",
        overwrite: bool = True,
    ):
        if targets is None:
            targets = sources

        if source_values is None:
            old_source_values = [getattr(self.manifest, src, None) for src in sources]
        else:
            old_source_values = source_values

        if target_values is None:
            old_target_values = [getattr(self.manifest, tgt, None) for tgt in targets]
        else:
            old_target_values = target_values

        for src, old_val_src, tgt, old_val_tgt in zip(
            sources, old_source_values, targets, old_target_values
        ):
            new_val_src = self.do_improvements(old_val_src, key=key)

            change = old_val_src != new_val_src
            if new_val_src is None:
                pass
            elif overwrite:
                setattr(self.manifest, tgt, new_val_src)
            elif change and old_val_tgt is None:
                setattr(self.manifest, tgt, new_val_src)
            else:
                pass
        return

    def improve_titles(self):
        return self.improve_lines(sources=self.titles, key="title")

    def improve_descriptions(self):
        return self.improve_lines(sources=self.descriptions, key="description")

    def improve_descriptions_from_title(self):
        sources = [t for t in self.titles if t != "title"]
        targets = [self.replace_suffix(t, suffix="description") for t in sources]
        return self.improve_lines(
            sources=sources,
            targets=targets,
            key="description_from_title",
            overwrite=False,
        )

    def improve_descriptions_from_name(self, keys: list[str] | None = None):
        sources = self.descriptions
        source_values = sources  # input is actual name

        if keys is None:
            keys = [
                k
                for k in self.enrichments
                if any(
                    [
                        s in k
                        for s in {
                            "description_from_name",
                            "descriptions_from_name",
                            "description_from_names",
                            "descriptions_from_names",
                        }
                    ]
                )
            ]

        for key in keys:
            self.improve_lines(
                sources=sources,
                source_values=source_values,
                key=key,
                overwrite=True,
            )
        return

    def improve_titles_from_name(self, keys: list[str] | None = None):
        sources = self.titles
        source_values = sources  # input is actual name

        if keys is None:
            keys = [
                k
                for k in self.enrichments
                if any(
                    [
                        s in k
                        for s in {
                            "title_from_name",
                            "titles_from_name",
                            "title_from_names",
                            "titles_from_names",
                        }
                    ]
                )
            ]

        for key in keys:
            self.improve_lines(
                sources=sources,
                source_values=source_values,
                key=key,
                overwrite=True,
            )
        return

    def improve_defaults_from_name(self, keys: list[str] | None = None):
        sources = self.defaults
        source_values = sources  # input is actual name

        if keys is None:
            keys = [
                k
                for k in self.enrichments
                if any(
                    [
                        s in k
                        for s in {
                            "default_from_name",
                            "defaults_from_name",
                            "default_from_names",
                            "defaults_from_names",
                        }
                    ]
                )
            ]

        for key in keys:
            self.improve_lines(
                sources=sources,
                source_values=source_values,
                key=key,
                overwrite=True,
            )
        return

    def improve_available_from_name(self, keys: list[str] | None = None):
        sources = [t for t in self.titles if t != "title"]
        targets = [self.replace_suffix(t, suffix="available") for t in sources]

        sources = [t.split(".title")[0] for t in self.titles if t != "title"]
        source_values = sources  # input is actual name

        if keys is None:
            keys = [
                k
                for k in self.enrichments
                if any(
                    [
                        s in k
                        for s in {
                            "available_from_name",
                            "availables_from_name",
                            "available_from_names",
                            "availables_from_names",
                        }
                    ]
                )
            ]

        for key in keys:
            self.improve_lines(
                sources=sources,
                source_values=source_values,
                targets=targets,
                key=key,
                overwrite=True,
            )
        return

    # properties
    @property
    def mf(self):
        # alias
        return self.manifest

    @mf.setter
    def mf(self, value):
        # alias
        self.manifest = value
        return

    @property
    def manifest(self):
        return getattr(self, "_manifest", None)

    @manifest.setter
    def manifest(self, value):
        if isinstance(value, Manifest):
            self._manifest = value
        else:
            raise TypeError("manifest attribute only accepts Manifest object.")
