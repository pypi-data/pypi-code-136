import sys
import json
from contextlib import contextmanager
from datetime import datetime

import click

from freedomrobotics_api import FreedomClient
from freedomrobotics_api.credentials import ENVIRONMENTS
from freedomrobotics_api.api_handler import MissingArgumentsError
from freedomrobotics_api.helpers import is_short_relative_date

common_options = [
    click.option('-u', '--user', help='User email'),
    click.option('--password', hide_input=True),
    click.option('--token'),
    click.option('--secret'),
    click.option('--env', '--environment', default='release', type=click.Choice(ENVIRONMENTS)),
    click.option('-a', '--account-id'),
]

listing_options = [
    click.option('--attributes', help="List of attributes to retrieve separated by comma"),
]

api_options = [
    click.option('--params', help="Key value with API query params. The format must be key=value separated by comma")
]


def add_options(options):
    """Decorator to allow sharing options between commands
    taken from https://stackoverflow.com/a/40195800/2349395
    """
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


@contextmanager
def error_message_catch(message, show_info_msg=True, do_exit=True):
    try:
        yield
        if show_info_msg:
            click.echo(click.style(f"{message} OK", fg='green'))
    except Exception as e:
        click.echo(click.style(f"{message} FAILED: {e}", fg='red'))
        if do_exit:
            sys.exit(1)


def get_freedom_client(token=None, secret=None, user=None, password=None, url=None, env=None, **_):
    try:
        return FreedomClient(
            token=token,
            secret=secret,
            username=user,
            password=password,
            url=url,
            env=env,
        )
    except MissingArgumentsError as e:
        raise click.UsageError(str(e))


def echo_json(data):
    click.echo(json.dumps(data, indent=2))


def parse_list_option(attr_name, kwargs):
    if kwargs.get(attr_name) is None:
        return None
    return kwargs[attr_name].split(',')


def parse_dict_option(attr_name, kwargs):
    values = parse_list_option(attr_name, kwargs)
    if values is None:
        return None
    result = {}
    for value in values:
        if ':' not in value:
            raise click.UsageError(
                f"Invalid value `{value}` for {attr_name}. "
                f"Must be in a key=value format separated by comma"
            )
        key, value = values.lsplit('=', 1)
        result[key] = value
    return result


class FreedomUTCRangeType(click.ParamType):
    name = 'freedom_utc_range'

    def convert(self, value, param, ctx):
        """Possible data types:
        - Epoch timestamp
        - Short relatives texts such as "1m", "10m", "3h", "1d"
        - Datetimes in the following formats:
           - 2022-04-18_13:25:15
           - 2022-04-18_13:25
           - 2022-04-18_13
        """
        converted = None
        # Test for short relatives
        if is_short_relative_date(value):
            return value

        # Test for datetime formats
        for fmt in ('%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M', '%Y-%m-%dT%H'):
            try:
                converted = datetime.strptime(value, fmt)
                # To epoch
                converted = (converted - datetime.utcfromtimestamp(0)).total_seconds()
                return converted
            except ValueError:
                pass

        try:
            converted = int(value)
            return converted
        except ValueError:
            self.fail(
                f'Invalid value `{value}`. Must be either a relative time short text (25s, 15m, 3h, 1d), '
                f'a date time with formats Y-m-sTH:M:S (minute and seconds are optional), '
                f'or a valid Epoch number'
            )


FREEDOM_UTC_RANGE = FreedomUTCRangeType()
