# coding: utf-8
"""
Low-level update commands.
"""
import logging

import click
import yaml

from opthub_client_cli.util import AliasedGroup, DateTimeTz, StrLength, execute

_logger = logging.getLogger(__name__)


@click.group(cls=AliasedGroup, help="Update an object.")
def update():
    """Update an object."""


@update.command(help="Update a problem.")
@click.argument("id-to-update", type=StrLength(min=2))
@click.option("-i", "--id", type=StrLength(min=2), help="New ID.")
@click.option("-t", "--image", type=StrLength(min=1), help="New Docker image tag.")
@click.option("--public/--private", default=None, help="New visibility.")
@click.option(
    "-e", "--description_en", type=StrLength(min=1), help="New description in English."
)
@click.option(
    "-j", "--description_ja", type=StrLength(min=1), help="New description in Japanese."
)
@click.pass_context
def problem(ctx, **kwargs):
    """Update a problem.

    :param ctx: Click context
    :param kwargs: GraphQL variables
    """
    _logger.debug("update.problem(%s)", kwargs)
    execute(
        ctx,
        """
        mutation(
          $id_to_update: String!
          %s
          %s
          %s
          %s
          %s
        ) {
          update_problems_by_pk(
            pk_columns: { id: $id_to_update }
            _set: {
              %s
              %s
              %s
              %s
              %s
            }
          ) {
            id
            updated_at
          }
        }
        """
        % (
            "$id: String!" if kwargs.get("id") is not None else "",
            "$image: String!" if kwargs.get("image") is not None else "",
            "$public: Boolean!" if kwargs.get("public") is not None else "",
            "$description_en: String!"
            if kwargs.get("description_en") is not None
            else "",
            "$description_ja: String!"
            if kwargs.get("description_ja") is not None
            else "",
            "id: $id" if kwargs.get("id") is not None else "",
            "image: $image" if kwargs.get("image") is not None else "",
            "public: $public" if kwargs.get("public") is not None else "",
            "description_en: $description_en"
            if kwargs.get("description_en") is not None
            else "",
            "description_ja: $description_ja"
            if kwargs.get("description_ja") is not None
            else "",
        ),
        {k: v for k, v in kwargs.items() if v is not None},
    )


@update.command(help="Update an indicator.")
@click.argument("id-to-update", type=StrLength(min=2))
@click.option("-i", "--id", type=StrLength(min=2), help="New ID.")
@click.option("-t", "--image", type=StrLength(min=1), help="New Docker image tag.")
@click.option("--public/--private", default=None, help="New visibility.")
@click.option(
    "-e", "--description_en", type=StrLength(min=1), help="New description in English."
)
@click.option(
    "-j", "--description_ja", type=StrLength(min=1), help="New description in Japanese."
)
@click.pass_context
def indicator(ctx, **kwargs):
    """Update an indicator.

    :param ctx: Click context
    :param kwargs: GraphQL variables
    """
    _logger.debug("update.indicator(%s)", kwargs)
    execute(
        ctx,
        """
        mutation(
          %s
          %s
          %s
          %s
          %s
        ) {
          update_indicators_by_pk(
            pk_columns: { id: $id_to_update }
            _set: {
              %s
              %s
              %s
              %s
              %s
            }
          ) {
            id
            updated_at
          }
        }
        """
        % (
            "$id: String!" if kwargs.get("id") is not None else "",
            "$image: String!" if kwargs.get("image") is not None else "",
            "$public: Boolean!" if kwargs.get("public") is not None else "",
            "$description_en: String!"
            if kwargs.get("description_en") is not None
            else "",
            "$description_ja: String!"
            if kwargs.get("description_ja") is not None
            else "",
            "id: $id" if kwargs.get("id") is not None else "",
            "image: $image" if kwargs.get("image") is not None else "",
            "public: $public" if kwargs.get("public") is not None else "",
            "description_en: $description_en"
            if kwargs.get("description_en") is not None
            else "",
            "description_ja: $description_ja"
            if kwargs.get("description_ja") is not None
            else "",
        ),
        {k: v for k, v in kwargs.items() if v is not None},
    )


@update.command(help="Update an environment.")
@click.argument("id-to-update", type=int)
@click.option("-m", "--match", type=click.IntRange(min=1), help="New match ID.")
@click.option("-k", "--key", type=StrLength(min=1), help="New key.")
@click.option("-v", "--value", type=yaml.safe_load, help="New value.")
@click.option("--public/--private", default=None, help="New visibility.")
@click.pass_context
def environment(ctx, **kwargs):
    """Update an environment.

    :param ctx: Click context
    :param kwargs: GraphQL variables
    """
    _logger.debug("update.environment(%s)", kwargs)
    execute(
        ctx,
        """
        mutation(
          $id_to_update: Int!
          %s
          %s
          %s
          %s
        ) {
          update_environments_by_pk(
            pk_columns: { id: $id_to_update }
            _set: {
              %s
              %s
              %s
              %s
            }
          ) {
            id
            updated_at
          }
        }
        """
        % (
            "$match: Int!" if kwargs.get("match") is not None else "",
            "$public: Boolean!" if kwargs.get("public") is not None else "",
            "$key: String!" if kwargs.get("key") is not None else "",
            "$value: jsonb!" if kwargs.get("value") is not None else "",
            "match_id: $match" if kwargs.get("match") is not None else "",
            "public: $public" if kwargs.get("public") is not None else "",
            "key: $key" if kwargs.get("key") is not None else "",
            "value: $value" if kwargs.get("value") is not None else "",
        ),
        {k: v for k, v in kwargs.items() if v is not None},
    )


@update.command(help="Update a match.")
@click.argument("id-to-update", type=int)
@click.option("-n", "--name", type=StrLength(min=2), help="New name.")
@click.option("-c", "--competition", type=StrLength(min=2), help="New competition ID.")
@click.option("-p", "--problem", type=StrLength(min=2), help="New problem ID.")
@click.option("-i", "--indicator", type=StrLength(min=2), help="New indicator ID.")
@click.option("-b", "--budget", type=click.IntRange(min=1), help="New budget.")
@click.pass_context
def match(ctx, **kwargs):
    """Update a match.

    :param ctx: Click context
    :param kwargs: GraphQL variables
    """
    _logger.debug("update.match(%s)", kwargs)
    execute(
        ctx,
        """
        mutation(
          $id_to_update: Int!
          %s
          %s
          %s
          %s
          %s
        ) {
          update_matches_by_pk(
            pk_columns: { id: $id_to_update }
            _set: {
              %s
              %s
              %s
              %s
              %s
            }
          ) {
            id
            updated_at
          }
        }
        """
        % (
            "$name: String!" if kwargs.get("name") is not None else "",
            "$competition: String!" if kwargs.get("competition") is not None else "",
            "$problem: String!" if kwargs.get("problem") is not None else "",
            "$indicator: String!" if kwargs.get("indicator") is not None else "",
            "$budget: Int!" if kwargs.get("budget") is not None else "",
            "name: $name" if kwargs.get("name") is not None else "",
            "competition_id: $competition"
            if kwargs.get("competition") is not None
            else "",
            "problem_id: $problem" if kwargs.get("problem") is not None else "",
            "indicator_id: $indicator" if kwargs.get("indicator") is not None else "",
            "budget: $budget" if kwargs.get("budget") is not None else "",
        ),
        {k: v for k, v in kwargs.items() if v is not None},
    )


@update.command(help="Update a competition.")
@click.argument("id-to-update", type=StrLength(min=2))
@click.option("-i", "--id", type=StrLength(min=2), help="New ID.")
@click.option("--public/--private", default=None, help="New visibility.")
@click.option("-o", "--open-at", type=DateTimeTz(), help="New open date.")
@click.option("-c", "--close-at", type=DateTimeTz(), help="New close date.")
@click.option(
    "-e", "--description_en", type=StrLength(min=1), help="New description in English."
)
@click.option(
    "-j", "--description_ja", type=StrLength(min=1), help="New description in Japanese."
)
@click.pass_context
def competition(ctx, **kwargs):
    """Update a competition.

    :param ctx: Click context
    :param kwargs: GraphQL variables
    """
    _logger.debug("update.competition(%s)", kwargs)
    execute(
        ctx,
        """
        mutation(
          $id_to_update: String!
          %s
          %s
          %s
          %s
          %s
          %s
        ) {
          update_competitions_by_pk(
            pk_columns: { id: $id_to_update }
            _set: {
              %s
              %s
              %s
              %s
              %s
              %s
            }
          ) {
            id
            updated_at
          }
        }
        """
        % (
            "$id: String!" if kwargs.get("id") is not None else "",
            "$public: Boolean!" if kwargs.get("public") is not None else "",
            "$description_en: String!"
            if kwargs.get("description_en") is not None
            else "",
            "$description_ja: String!"
            if kwargs.get("description_ja") is not None
            else "",
            "$open_at: timestamptz!" if kwargs.get("open_at") is not None else "",
            "$close_at: timestamptz!" if kwargs.get("close_at") is not None else "",
            "id: $id" if kwargs.get("id") is not None else "",
            "public: $public" if kwargs.get("public") is not None else "",
            "description_en: $description_en"
            if kwargs.get("description_en") is not None
            else "",
            "description_ja: $description_ja"
            if kwargs.get("description_ja") is not None
            else "",
            "open_at: $open_at" if kwargs.get("open_at") is not None else "",
            "close_at: $close_at" if kwargs.get("close_at") is not None else "",
        ),
        {k: v for k, v in kwargs.items() if v is not None},
    )
