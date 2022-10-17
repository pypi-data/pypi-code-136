import json
from datetime import datetime
from typing import Optional

import click
import pyld
import questionary

from renkubio import __version__
from renkubio.biosample import BioSample, BioSampleSchema
from renkubio.common_entities import EnrichableEntity
from renkubio.rdf import (
    extract_biosample_meta,
    get_sample_table,
    get_sample_uri,
    load_graph,
)
from renkubio.utils import (
    edit_annotations,
    find_sample_in_annot,
    get_project_url,
    get_renku_dataset,
    get_renku_project,
    load_annotations,
    prettify_csv,
    prettyprint_dict,
)


def prompt_enrich_object(obj: EnrichableEntity, msg: str, display_field: str):
    """Interactive prompt the user to select the API record matching object property."""
    # Send a request with object name to an API
    records = obj.query()
    # Interactive selection among matching records
    try:
        choices = [rec[display_field] for rec in records] + ["None"]
    except TypeError:
        return
    choice = questionary.select(
        msg,
        choices=choices,
    ).ask()

    if choice:
        # Recover full metadata for chosen record and enrich biosample with it
        chosen_record = list(filter(lambda r: r.get(display_field) == choice, records))[
            0
        ]
        obj.enrich(chosen_record)


def prompt_biosample(
    bs: BioSample,
    taxon: Optional[str] = None,
    collector: Optional[str] = None,
    location: Optional[str] = None,
):
    """Sequentially prompts the user to enrich each object property of the input biosample."""

    if taxon:
        prompt_enrich_object(
            bs.taxonomic_range,
            msg="What is the matching taxon record ?",
            display_field="scientificName",
        )

    if collector:
        prompt_enrich_object(
            bs.collector,
            msg="What is the organization responsible for sample collection ?",
            display_field="name",
        )

    if location:
        prompt_enrich_object(
            bs.location_created,
            msg="What is the correct location where the sample was collected ?",
            display_field="display_name",
        )


def get_iso_date(date: str) -> datetime:
    """Check that input string is in ISO-8601 format and
    keep only year, month and day informations"""
    try:
        return datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Deadline must be in ISO-8601 (YYYY-MM-DD) format.")


@click.group()
@click.version_option(version=__version__)
def bio():
    """
    renku-bio: Biological annotations in Renku metadata.
    """


@bio.command()
@click.argument("name")
@click.option("--description", "-d", help="Free text description of the sample.")
@click.option(
    "--url", "-u", help="If applicable, a link to a ressource describing the sample."
)
@click.option(
    "--taxon", "-t", help="The taxon of the sample (Scientific or common name)."
)
@click.option(
    "--age", "-a", type=int, help="The biological age of the sample, in years."
)
@click.option(
    "--collector",
    "-c",
    help="The organization responsible for sample collection.",
)
@click.option(
    "--control",
    "-C",
    is_flag=True,
    help="Whether this sample represents the control group.",
)
@click.option(
    "--gender",
    "-g",
    help="Can be 'male', 'female', or another value.",
)
@click.option(
    "--date", help="Date when the sample was collected, in YYYY-MM-DD format."
)
@click.option(
    "--location",
    "-l",
    help="Where the sample was collected. Ideally a geographical name.",
)
@click.option(
    "--dataset",
    help="Target dataset in which to add the sample. If not specified, sample"
    " is added to the project's metadata.",
)
@click.option(
    "--dry-run", is_flag=True, help="Only print biosample, do not modify metadata."
)
@click.option(
    "--no-prompt", is_flag=True, help="Do not prompt to enrich biosample properties."
)
def add_sample(
    name: str,
    description: str,
    url: Optional[str],
    taxon: Optional[str],
    age: Optional[int],
    gender: Optional[str],
    collector: Optional[str],
    control: Optional[bool],
    date: Optional[str],
    location: Optional[str],
    dry_run: bool = False,
    no_prompt: bool = False,
    dataset: Optional[str] = None,
):
    """Add a biological sample to the project's metadata.
    name is the identifier used to refer to the sample. If
    a dataset is specified, adds the sample to the dataset
    metadata instead."""

    if dataset:
        meta = get_renku_dataset(dataset)
    else:
        meta = get_renku_project()
    annotations = load_annotations(meta)

    if find_sample_in_annot(annotations, name) >= 0:
        raise ValueError(
            f"A sample with name {name} already exists in "
            "this project. Please use another name."
        )

    if date:
        date = get_iso_date(date)

    # Generate a unique ID for the biosample
    sample_id = get_project_url()
    if dataset:
        sample_id += f"/datasets/{dataset}"
    sample_id += f"/{name}"
    bs = BioSample(
        _id=sample_id,
        name=name,
        url=url,
        description=description,
        taxonomic_range=taxon,
        collector=collector,
        sampling_age=age,
        gender=gender,
        location_created=location,
        date_created=date,
        is_control=control,
    )

    if not no_prompt:
        prompt_biosample(bs, taxon, collector, location)

    bs_dict = BioSampleSchema().dump(bs)
    bs_json = pyld.jsonld.flatten({k: v for k, v in bs_dict.items() if v is not None})

    if dry_run:
        print(json.dumps(bs_json, indent=2))
    else:
        # Add sample to current annotations
        annotations[0]["body"] += bs_json

        edit_annotations(annotations, dataset)


@bio.command()
def ls_samples():
    """List available biosamples"""

    graph = load_graph()
    samples_csv = get_sample_table(graph)
    pretty_csv = prettify_csv(
        samples_csv,
        has_headers=True,
        tablefmt="fancy_grid",
    )
    print(pretty_csv)


@bio.command()
@click.argument("name")
def show_sample(name: str):
    """Display information on a specific biosample"""
    graph = load_graph()
    sample_id = get_sample_uri(name, graph)
    if sample_id:
        meta_dict = extract_biosample_meta(sample_id, graph)
        prettyprint_dict(meta_dict)
    else:
        print(f"No sample named '{name}'.")


@bio.command()
@click.argument("name")
@click.option(
    "--dataset",
    help="Target dataset in which to add the sample. If not specified, sample"
    " is added to the project's metadata.",
)
def rm_sample(name: str, dataset: Optional[str] = None):
    """Remove a biosample from the project's metadata.
    name refers to the biosample to remove."""

    if dataset:
        meta = get_renku_dataset(dataset)
    else:
        meta = get_renku_project()
    # find sample in current annotations dictionary
    annotations = load_annotations(meta)
    rm_idx = find_sample_in_annot(annotations, name)

    if rm_idx < 0:
        print(f"No sample named {name}.")
        return

    # rm sample from annotations dictionary
    annotations[0]["body"].pop(rm_idx)

    # Update project metadata with edited dictionary
    edit_annotations(annotations, dataset)
