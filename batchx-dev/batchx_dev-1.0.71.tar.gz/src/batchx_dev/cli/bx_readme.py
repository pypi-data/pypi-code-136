# imports
import json
import os
from datetime import datetime

import click
from batchx_dev.toolbox import Manifest, ManifestImprover, ReadmeImprover

from .end2end import (
    basic_configuration_mfi,
    basic_configuration_rmi,
    make_backup_copy,
    make_initial_readme,
    print_available_improvements,
    print_report_header,
)
from .monkeypatch import Path


# actual function
def run_bx_readme(
    manifest_fp: Path,
    readme_fp: Path,
    backup_dp: Path | None = None,
    manifest_fp_out: Path | None = None,
    readme_fp_out: Path | None = None,
    offline: bool = False,
    bx_env: str = "batchx",
    include_drafts: bool = True,
    verbose: bool = True,
):
    online = not offline

    print_report_header("Initialization", level=1)

    # INIT MFI
    BU_MF_FP = make_backup_copy(manifest_fp, dp=backup_dp)

    if manifest_fp_out is None:
        MF_FP_OUT = manifest_fp

    mfi = ManifestImprover(manifest_fp=manifest_fp, verbose=verbose)

    # INIT RMI
    if not Path(readme_fp).exists():
        make_initial_readme(readme_fp, is_pipeline=mfi.mf.is_pipeline)
    else:
        pass
    BU_RM_FP = make_backup_copy(readme_fp, dp=backup_dp)

    if readme_fp_out is None:
        RM_FP_OUT = readme_fp

    rmi = ReadmeImprover(readme_fp=readme_fp, verbose=verbose)

    if verbose:
        print_report_header("Backups", level=2)
        for e in [BU_MF_FP, BU_RM_FP]:
            print("    - {}".format(e))

    if online and isinstance(getattr(mfi, "steps", None), dict):
        steps_dict = mfi.steps.copy()
    else:
        steps_dict = dict()

    if verbose:
        print_available_improvements(mfi, level=2)
        print_available_improvements(rmi, level=2)

    # MFI
    print_report_header("ManifestImprover", level=1)
    mfi = basic_configuration_mfi(mfi, steps_dict=steps_dict, verbose=verbose)

    # run mfi
    mfi.improve_descriptions_from_name()
    mfi.improve_titles()
    mfi.improve_descriptions()
    mfi.improve_descriptions_from_title()
    mfi.improve_titles_from_name()

    mfi.mf.save(fp=MF_FP_OUT)

    # RMI
    print_report_header("ReadmeImprover", level=1)

    mfi.add_enrichment("fetch_defaults", key="defaults_from_name")
    mfi.improve_defaults_from_name()  # These defaults should not end up on disk

    mfi.add_enrichment("fetch_available", key="available_from_name")
    mfi.improve_available_from_name()  # These defaults should not end up on disk

    rmi = basic_configuration_rmi(
        rmi,
        mfi,
        steps_dict=steps_dict,
        bx_env=bx_env,
        include_drafts=include_drafts,
        flatten=("default", "available"),
        verbose=verbose,
    )

    # run rmi
    rmi.improve_user_defined_sections()
    rmi.generate_platform_defined_sections()
    rmi.improve_platform_defined_sections()
    rmi.draft_user_defined_sections()

    rmi.rm.save(fp=RM_FP_OUT)

    return


# CLI-method
@click.command()
@click.option(
    "--manifest_fp",
    default="manifest.json",
    help="Manifest filepath.",
    type=click.Path(exists=True),
)
@click.option(
    "--readme_fp",
    default="readme.md",
    help="Readme filepath.",
)
@click.option(
    "--backup_dp",
    default=None,
    help="Backup directory path.",
)
@click.option(
    "--manifest_fp_out",
    default=None,
    help="Manifest output filepath.",
)
@click.option(
    "--readme_fp_out",
    default=None,
    help="Readme output filepath.",
)
@click.option(
    "--bx_env",
    default="batchx",
    help="BatchX environment to assume for consistency checks in example section.",
)
@click.option(
    "--offline",
    is_flag=True,
    default=False,
    help="Flag that indicates whether the ReadmeImprover should try and fetch information online.",
)
@click.option(
    "--include_drafts",
    is_flag=True,
    default=True,
    help="Flag that indicates whether the ReadmeImprover should generate drafts for empty sections.",
)
def main(
    manifest_fp: Path,
    readme_fp: Path,
    backup_dp: Path | None = None,
    manifest_fp_out: Path | None = None,
    readme_fp_out: Path | None = None,
    offline: bool = False,
    bx_env: str = "batchx",
    include_drafts: bool = True,
    verbose: bool = True,
):
    return run_bx_readme(
        manifest_fp=manifest_fp,
        readme_fp=readme_fp,
        backup_dp=backup_dp,
        manifest_fp_out=manifest_fp_out,
        readme_fp_out=readme_fp_out,
        offline=offline,
        bx_env=bx_env,
        include_drafts=include_drafts,
        verbose=verbose,
    )


# main clause
if __name__ == "__main__":
    main()
