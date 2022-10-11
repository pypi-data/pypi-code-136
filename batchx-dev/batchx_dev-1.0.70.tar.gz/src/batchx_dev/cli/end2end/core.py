from .extract import bx_coords_and_version, get_steps_urls_dict
from .report import print_attribute


def basic_configuration_mfi(mfi, steps_dict: dict | None = None, verbose: bool = True):
    # fixes
    mfi.add_all_fixes(key="title")
    mfi.add_all_fixes(key="description")

    # checks
    mfi.add_checks(["formal_style", "avoid_the_word_image"], key="title")
    mfi.add_checks(["formal_style", "avoid_the_word_image"], key="description")

    # enrichments
    mfi.add_enrichment("document_urls", key="description")
    mfi.add_enrichment("document_urls", key="description_from_title")

    # pipeline-specific enrichments
    if mfi.mf.is_pipeline:
        if verbose:
            print("\nAdding pipeline-specific enrichments.")
        mfi.add_enrichment(
            "fill_in_fixed_description", key="fixed_description_from_name"
        )

        mfi.add_enrichment(
            "fetch_external_title", key="external_titles_from_name", steps=steps_dict
        )
    # inspect enrichments
    if verbose:
        print_attribute(mfi, "enrichments")
    return mfi


def basic_configuration_rmi(
    rmi,
    mfi,
    steps_dict: dict | None = None,
    bx_env: str = "batchx",
    include_drafts: bool = True,
    flatten=("default", "available"),
    verbose: bool = True,
):
    tool_name, tool_version = bx_coords_and_version(mfi.mf, bx_environment=bx_env)

    manifest_dict = mfi.mf.serialize(flatten=flatten).copy()
    steps_urls_dict = get_steps_urls_dict(steps_dict)

    # fixes
    rmi.add_all_fixes(key="user_defined_sections")

    # add checks
    rmi.add_checks(
        ["formal_style", "avoid_the_word_image"], key="user_defined_sections"
    )

    # consistency check needs external input
    rmi.add_check(
        "consistent_tool_reference",
        key="user_defined_sections",
        tool_name=tool_name,
        tool_version=tool_version,
    )

    # add enrichments
    rmi.add_enrichment(
        "document_urls", key="user_defined_sections"
    )  # library-defined urls (BAM, FASTA etc.)

    # manually-defined urls

    """
    extra_urls_dict = dict()
    extra_urls_dict[
        "usage tab"
    ] = "https://platform.batchx.io/test/tools/{}/usage".format(
        manifest_dict.get("name").replace("/", "%2F")
    )
    rmi.add_enrichment(
        "document_urls",
        key="user_defined_sections",
        urls_to_document=extra_urls_dict,
    )
    """

    if mfi.mf.is_pipeline:
        if verbose:
            print("\nAdding pipeline-specific enrichments to readme.")

        # pipeline-steps defined urls
        rmi.add_enrichment(
            "document_urls",
            key="user_defined_sections",
            urls_to_document=steps_urls_dict.get("docs"),
        )
        rmi.add_enrichment(
            "document_urls",
            key="Inputs",
            urls_to_document=steps_urls_dict.get("input"),
        )
        rmi.add_enrichment(
            "document_urls",
            key="Outputs",
            urls_to_document=steps_urls_dict.get("output"),
        )

    rmi.add_render("title", key="Title", manifest_dict=manifest_dict)

    if include_drafts:
        rmi.add_render("context", key="Context")
        rmi.add_render("examples", key="Examples")

    # manifest-defined sections
    if mfi.mf.is_pipeline:
        if verbose:
            print("\nAdding pipeline-specific renders to readme.")
        rmi.add_render("pipeline_inputs", key="Inputs", manifest_dict=manifest_dict)
        rmi.add_render("pipeline_outputs", key="Outputs", manifest_dict=manifest_dict)
        rmi.add_render(
            "pipeline_overview",
            key="Pipeline overview",
            steps_dict=dict(steps=steps_dict),
        )
    else:
        if verbose:
            print("\nAdding tool-specific renders to readme.")
        rmi.add_render("tool_inputs", key="Inputs", manifest_dict=manifest_dict)
        rmi.add_render("tool_outputs", key="Outputs", manifest_dict=manifest_dict)

    return rmi
