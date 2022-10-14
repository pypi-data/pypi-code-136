# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Graz University of Technology.
#
# invenio-imoox is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Click command-line interface for `invenio-imoox` module."""

import time

import click
import requests
from flask.cli import with_appcontext
from invenio_records_lom import current_records_lom

from .converter import MoocToLOM
from .utils import get_identity_from_user_by_email


def get_records_from_imoox(endpoint: str) -> dict:
    """Get the response from imoox."""
    response = requests.get(endpoint, timeout=10)
    response.raise_for_status()
    return response.json()


def convert(imoox_records: list) -> dict:
    """Convert the imoox representation to lom."""
    converter = MoocToLOM()
    lom_records = []

    for imoox_record in imoox_records["data"]:
        lom_records.append(converter.convert(imoox_record))

    return lom_records


def create_then_publish(lom_record: dict, identity):
    """Create and publish function."""
    service = current_records_lom.records_service

    data = {
        "access": {"record": "public", "files": "public"},
        "files": {"enabled": False},
        "metadata": lom_record,
        "resource_type": "link",
    }

    draft = service.create(data=data, identity=identity)

    # to prevent the race condition bug.
    # see https://github.com/inveniosoftware/invenio-rdm-records/issues/809
    time.sleep(0.5)

    return service.publish(id_=draft.id, identity=identity)


@click.group()
def imoox():
    """CLI-group for `invenio-imoox` commands."""


@imoox.command("import")
@with_appcontext
@click.option("--endpoint", required=True)
@click.option("--user-email", type=click.STRING, default="imoox@tugraz.at")
def import_from_imoox(endpoint, user_email):
    """Import metadata from endpoint into the repository."""
    identity = get_identity_from_user_by_email(email=user_email)
    imoox_records = get_records_from_imoox(endpoint)
    lom_records = convert(imoox_records)

    for lom_record in lom_records:
        record = create_then_publish(lom_record, identity)
        print(record.id)

    return lom_records
