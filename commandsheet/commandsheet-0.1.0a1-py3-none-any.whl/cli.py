"""Code for the command-line interface."""

import argparse
import sys
from commandsheet.locale import _


class CustomArgumentParser(argparse.ArgumentParser):
    def print_usage(self, file=None):
        file = sys.stdout if file is None else sys.stderr
        output = self.format_usage().replace('usage: ', _('usage: '), 1)
        print(output, file=file, end='')

    def print_help(self, file=None):
        file = sys.stdout if file is None else sys.stderr
        output = self.format_help().replace('usage: ', _('usage: '), 1)
        print(output, file=file, end='')

    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            unrecognized = {'args': ' '.join(argv)}
            msg = _('unrecognized arguments: %(args)s' % unrecognized)
            self.error(msg)
        return args

    def exit(self, status=0, message=None, newline=False):
        if message is not None:
            end_char = '' if not newline else '\n'
            print(_(message), file=sys.stderr, end=end_char)
        sys.exit(status)

    def error(self, message):
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(
            status=2,
            newline=True,
            message=_('%(prog)s: error: %(message)s' % args)
        )


def options(parser):
    opts = parser.add_argument_group(_('options'))
    opts.add_argument(
        '-s',
        '--section-numbers',
        action='store_true',
        help=_("Print a section number in front of each section title")
    )
    opts.add_argument(
        '-f',
        '--fillchar',
        action='store',
        metavar=_('CHAR'),
        default='.',
        type=str,
        help=_(
            "Use %(metavar)s to fill the gap between "
            "the command and its explanation "
            "(default: `%(default)s`)"
        )
    )
    opts.add_argument(
        '-c',
        '--config-file',
        action='store',
        metavar=_('CONFIG'),
        help=_("Use %(metavar)s as the config file")
    )
    opts.add_argument(
        '-h',
        '--help',
        action='help',
        help=_("Show this message")
    )
    opts.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s 0.1.0a1',
        help=_("Show version")
    )


def argparser():
    return CustomArgumentParser(
        prog='commandsheet',
        description=_("Display catalog of commands user uses often."),
        add_help=False,
        allow_abbrev=False
    )
