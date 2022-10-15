# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
decorator functions

"""
import argparse, os, sys
from functools import wraps
 

DESCRIPTION = 'Compile google docs into a manuscript'
CATEGORIES = ['Adult', 'YA', 'Middle-Grade', "Children's"]
HELP = {
    'folder': 'google drive folder or filename',
    'genre': 'eg. Crime, Fantasy, Literary Fiction',
    'pseudonym': "eg. Lee Child (if you don't use "
                 'a pseudonym put your real name here)',
    'title': 'novel title',
    'shortname': 'abbreviated title (needed if title is longer than 3 words)',
    'final': 'use this flag to inject the below contact info into the title page',
    'reply_to': " full name of the person they should reply to",
    'email': 'the email address they should reply to',
    'street': 'the street address they should reply to',
    'phone': 'the phone number they should reply to'
}
 
def run_with_shell_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        parser = argparse.ArgumentParser(prog=fn.__name__,
                                         description=DESCRIPTION)

        parser.add_argument('source', envvar='MSFY_SOURCE',
                            action=EnvDefault, nargs='+',
                            help=HELP['folder'])
        parser.add_argument('-c', '--category', envvar='MSFY_CATEGORY',
                            action=EnvDefault, choices=CATEGORIES)
        parser.add_argument('-g', '--genre', envvar='MSFY_GENRE',
                            action=EnvDefault, help=HELP['genre'])
        parser.add_argument('-p', '--pseudonym', envvar='MSFY_PSEUDONYM',
                            action=EnvDefault, help=HELP['pseudonym'])
        parser.add_argument('-t', '--title', envvar='MSFY_TITLE',
                            action=EnvDefault, help=HELP['title'])
        parser.add_argument('-s', '--shortname', envvar='MSFY_SHORTNAME',
                            required=False, action=EnvDefault,
                            help=HELP['shortname'])
        parser.add_argument('-f', '--final', action='store_true',
                            required=False, help=HELP['final'])

        parser.add_argument('-R', '--reply-to', envvar='MSFY_REPLY_TO',
                            required='--final' in sys.argv, action=EnvDefault,
                            help=HELP['reply_to'])
        parser.add_argument('-E', '--email', envvar='MSFY_EMAIL',
                            required='--final' in sys.argv, action=EnvDefault,
                            help=HELP['email'])
        parser.add_argument('-P', '--phone', envvar='MSFY_PHONE',
                            required='--final' in sys.argv, action=EnvDefault,
                            help=HELP['phone'])
        parser.add_argument('-S', '--street1', envvar='MSFY_STREET1',
                            required='--final' in sys.argv, action=EnvDefault,
                            help=HELP['street'])
        parser.add_argument('-T', '--street2', envvar='MSFY_STREET2',
                            required='--final' in sys.argv, action=EnvDefault,
                            help=HELP['street'])

        args = parser.parse_args()
        fn(**vars(args))
    return wrapper


class EnvDefault(argparse.Action):
    """properly handle env vars without breaking argparse"""

    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if envvar == 'MSFY_SHORTNAME':
            title = os.environ['MSFY_TITLE']
            required = len(title.split()) > 3
        if required and default:
            required = False
        super().__init__(default=default,
                         required=required, 
                         **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        vals = ' '.join(values) if type(values) is list else values
        setattr(namespace, self.dest, vals)
