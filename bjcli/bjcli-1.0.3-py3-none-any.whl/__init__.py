import os
from argparse import ArgumentParser

__author__: str = 'Kapustlo'

__version__: str = '1.0.3'

environ = os.environ

parser: ArgumentParser = ArgumentParser(description='Make this baby run on Bjoern')

parser.add_argument('positional', metavar='wsgi_app', nargs='+', help='Path to wsgi application')

parser.add_argument('--version', action='version', version=f'%(prog)s v{__version__}')

parser.add_argument("-w", dest='workers', required=False, type=int, default=int(environ.get('WORKERS', 1)))

parser.add_argument("-p", dest='port', default=environ.get('PORT'), type=int, required=False)

parser.add_argument("-i", dest='host', required=False, default=environ.get('HOST', '127.0.0.1'))
