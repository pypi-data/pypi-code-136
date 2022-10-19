"""
Test case for PITag.
.. since: 0.2
"""

# -*- coding: utf-8 -*-
# Copyright (c) 2022 Endeavour Mining
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to read
# the Software only. Permissions is hereby NOT GRANTED to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sqlalchemy  # type: ignore
from hamcrest import assert_that, equal_to, raises, calling
from edv_dwh_connector.exceptions import ValueNotFoundError, \
    ValueAlreadyExistsError
from edv_dwh_connector.pi.db.pg_pi_tag import PgPITags
from tests.adapted_postgresql import AdaptedPostreSQL, PgDwhForTests


def test_save_new_tag() -> None:
    """
    Tests that it saves new tag.
    """

    with AdaptedPostreSQL() as postgres:
        tags = PgPITags(
            PgDwhForTests(
                sqlalchemy.create_engine(postgres.get_connection_url())
            )
        )
        tag = tags.add(
            "AI160014A_SCLD",
            "CIL Free Cyanide Analyser pH Indicator Tank 1 Scaled Value",
            "pH"
        )
        assert_that(
            tag.code(), equal_to("AI160014A_SCLD"),
            "PI Tag code should match"
        )
        assert_that(
            tag.name(),
            equal_to(
                "CIL Free Cyanide Analyser pH Indicator Tank 1 Scaled Value"
            ),
            "PI Tag name should match"
        )
        assert_that(
            tag.uom(), equal_to("pH"),
            "PI Tag unit should match"
        )


def test_get_tag_by_code() -> None:
    """
    Tests that it gets tag by code
    """

    with AdaptedPostreSQL() as postgres:
        tags = PgPITags(
            PgDwhForTests(
                sqlalchemy.create_engine(postgres.get_connection_url())
            )
        )
        code = "AI162003_SCLD"
        assert_that(
            tags.get(code).code(), equal_to(code),
            "PI Tag fetched should have code matching"
        )


def test_try_to_add_existent_tag() -> None:
    """
    Try to add existent tag.
    """

    with AdaptedPostreSQL() as postgres:
        tags = PgPITags(
            PgDwhForTests(
                sqlalchemy.create_engine(postgres.get_connection_url())
            )
        )
        tag = tags.add(
            "AI162002_SCLD",
            "AI162002 Carbon Scout Tank 1 DO Scaled Value",
            "ppm"
        )
        assert_that(
            calling(tags.add).with_args(tag.code(), "Foo", "unit foo"),
            raises(
                ValueAlreadyExistsError,
                "Tag with code AI162002_SCLD already exists"
            ),
            "PI Tag added should exist"
        )


def test_try_to_get_non_existent_tag() -> None:
    """
    Try to get non-existent tag.
    """

    with AdaptedPostreSQL() as postgres:
        tags = PgPITags(
            PgDwhForTests(
                sqlalchemy.create_engine(postgres.get_connection_url())
            )
        )
        assert_that(
            calling(tags.get).with_args("NOT-EXISTENT CODE"),
            raises(ValueNotFoundError, "Tag not found"),
            "PI Tag fetched should not exist"
        )
