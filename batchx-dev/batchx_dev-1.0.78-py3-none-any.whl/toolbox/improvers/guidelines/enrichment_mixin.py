from functools import partial

from ...parsers import DotDict
from ...utils import FIXED_DESCRIPTIONS, URLS
from ..functiondict_mixin import FunctionDictMixin


class Enrichments:
    @property
    def available_enrichments(self):
        return dict(
            document_urls=self.document_urls,
            fill_in_fixed_description=self.fill_in_fixed_description,
            fetch_external_title=self.fetch_external_title,
            fetch_defaults=self.fetch_defaults,
            fetch_available=self.fetch_available,
            fetch_flat_dict_for_field=self.fetch_flat_dict_for_field,
        )

    def document_urls(
        self,
        line: str,
        urls_to_document: None | dict = None,
        verbose: bool | None = None,
    ) -> str:
        if verbose is None:
            verbose = self.verbose

        def _update_urls_to_document(
            line: str, urls_to_document: dict | None, verbose: bool
        ):
            if urls_to_document is None:
                urls_to_document = URLS.copy()
            else:
                urls_to_document.copy()

            # count already documented urls
            counts = {k: line.count(v) for k, v in urls_to_document.items()}

            for k, c in counts.items():
                if c > 0:
                    # this url has been documented already
                    urls_to_document.pop(k)

                if c > 1:
                    # this url has been excessively documented

                    if verbose:
                        msg = """
                        In the following excerpt (first 100 chars shown): 
                        '''
                        {e}
                        '''

                        Term     {k}
                        with URL {u}
                        has been documentend {n} times 

                        Please verify whether this was a conscious decision, as the 
                        documentation guidelines specify documenting the same term just once.
                        """.format(
                            k=k,
                            u=urls_to_document.get(
                                k,
                                "<URL MISSING>: It did get popped from the dict as it should.",
                            ),
                            n=c,
                            e=line[: min(100, len(line))],
                        )
                        print(msg)
            return urls_to_document

        def _add_url_to_line(line: str, key: str, url) -> str:
            attempt_01 = line.replace(
                " {k}".format(k=k), " [{k}]({u})".format(k=k, u=u), 1
            )

            attempt_02 = line.replace(
                "{k} ".format(k=k), "[{k}]({u}) ".format(k=k, u=u), 1
            )

            if attempt_01 != line:
                new_line = attempt_01
                if verbose:
                    print("Documented an instance of {}".format(k))
            elif attempt_02 != line:
                new_line = attempt_02
                if verbose:
                    print("Documented an instance of {}".format(k))
            else:
                new_line = line
            return new_line

        urls_to_document = _update_urls_to_document(line, urls_to_document, verbose)

        new_line = line
        for k, u in urls_to_document.items():
            new_line = _add_url_to_line(new_line, k, u)

        return new_line

    def fill_in_fixed_description(
        self,
        name: str,
        fixed_descriptions: None | dict = None,
        warn: bool = False,
        verbose: bool | None = None,
    ) -> str | None:

        if verbose is None:
            verbose = self.verbose

        if fixed_descriptions is None:
            fixed_descriptions = FIXED_DESCRIPTIONS.copy()

        fixed_description = fixed_descriptions.get(name, None)

        if fixed_description is not None and verbose:
            msg = """
            [ENRICHMENT] Found a description for which the guidelines specify a fixed text.
                THIS PARAMETER: {p}
                HAS THIS FIXED TITLE:
                    {t}

                DID REPLACEMENT OR JUST WARNING: {a}

            """.format(
                p=name, t=fixed_description, a="warning" if warn else "replacement"
            )
            print(msg)

        if warn:
            return None
        else:
            return fixed_description

    def fetch_external_title(
        self,
        name: str,
        steps: None | dict = None,
        verbose: bool | None = None,
    ) -> str | None:
        def _name_from_title_jsonpath(jp):
            parts = jp.split(".")
            if len(parts) > 1:
                return parts[-2]
            else:
                return jp

        if verbose is None:
            verbose = self.verbose

        if steps is None:
            steps = self.steps

        if name is not None:
            name = _name_from_title_jsonpath(name)

        external_title = steps.get(name, dict()).get("title", None)

        if external_title is not None and verbose:
            msg = """
            [ENRICHMENT] Found a title for which an external title could be fetched.
                THIS PARAMETER: {p}
                HAS THIS EXTERNAL TITLE:
                    {t}

            """.format(
                p=name,
                t=external_title,
            )
            print(msg)

        return external_title

    def fetch_flat_dict_for_field(
        self,
        name: str,
        field: str = "default",
        steps: None | dict = None,
        conservative: bool = True,
        verbose: bool | None = None,
    ) -> dict:
        if verbose is None:
            verbose = self.verbose

        value = self.mf[name]
        if (
            conservative
            and isinstance(value, (DotDict, dict))
            and len(dict(value)) == 0
        ):
            jp = name.split(".{f}".format(f=field))[0]
            flat_dict = self.collect_flat_dict(jp, field=field)
        elif not conservative:
            jp = name.split(".{f}".format(f=field))[0]
            print(jp)
            flat_dict = self.collect_flat_dict(jp, field=field)
        else:
            flat_dict = None

        if flat_dict is not None and len(flat_dict) > 0 and verbose:
            msg = """
            [ENRICHMENT] Fetched nested fields.
                THIS PARAMETER: {p}
                HAS THESE VALUES FOR {f}:
                    {d}

            """.format(
                p=name, d=flat_dict, f=field.upper()
            )
            print(msg)

        return flat_dict

    def fetch_defaults(
        self,
        name: str,
        steps: None | dict = None,
        verbose: bool | None = None,
    ) -> dict:
        return self.fetch_flat_dict_for_field(
            name=name, field="default", steps=steps, verbose=verbose, conservative=True
        )

    def fetch_available(
        self,
        name: str,
        steps: None | dict = None,
        verbose: bool | None = None,
    ) -> dict:
        return self.collect_descendants(
            name,
            key_reference_field="title",
            value_reference_field="default",
            dummy_value=None,
        )


class EnrichmentsMixin(Enrichments, FunctionDictMixin):
    def do_enrichments(self, line: str, key: str | None = None) -> str:
        """Do all enrichments. This tries to enrich the given line."""
        return self.do_functions(line, key=key, kind="enrichments")

    def add_enrichment(
        self,
        enrichment: str,
        key: str | None = None,
        **kwargs,
    ):
        return self.add_function(
            function=enrichment, key=key, kind="enrichments", **kwargs
        )
