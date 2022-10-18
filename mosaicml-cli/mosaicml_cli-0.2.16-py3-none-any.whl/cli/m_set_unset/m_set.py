""" mcli set Entrypoint """
import argparse

from mcli.cli.m_set_unset.api_key import configure_api_key_argparser, modify_api_key
from mcli.cli.m_set_unset.feature import modify_feature_flag


def set_entrypoint(**kwargs):
    del kwargs
    mock_parser = configure_argparser(parser=argparse.ArgumentParser())
    mock_parser.print_help()
    return 0


def configure_argparser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=set_entrypoint)

    feature_parser = subparsers.add_parser('feature', help='Activate a feature flag')
    feature_parser.add_argument('feature', nargs='?', help='The name of the feature flag')
    feature_parser.set_defaults(func=modify_feature_flag, activate=True)

    api_key_parser = subparsers.add_parser(
        'api-key',
        help='Set a MosaicML Cloud API key that will be used in all of your subsequent workloads',
        description='Set a MosaicML Cloud API key that will be used in all of your subsequent workloads',
    )
    configure_api_key_argparser(api_key_parser)
    api_key_parser.set_defaults(func=modify_api_key)

    return parser


def add_set_argparser(subparser: argparse._SubParsersAction,) -> argparse.ArgumentParser:
    """Adds the set parser to a subparser

    Args:
        subparser: the Subparser to add the Use parser to
    """
    set_parser: argparse.ArgumentParser = subparser.add_parser(
        'set',
        help='Set local configuration variables',
    )
    set_parser = configure_argparser(parser=set_parser)
    return set_parser
