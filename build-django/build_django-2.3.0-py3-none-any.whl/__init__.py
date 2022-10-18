from argparse import ArgumentParser

__author__ = 'Kapustlo'

__version__ = '2.3.0'

parser: ArgumentParser = ArgumentParser(description='Build Django project')

parser.add_argument('name', metavar='name', help='Django project name')

parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')

parser.add_argument('--dir', dest='dir', type=str, default='./', required=False, help='Django project directory')

parser.add_argument('--debug', dest='debug', action='store_true', required=False, help='Should create env with DEBUG=True')

parser.add_argument('--hosts', dest='hosts', required=False, default='', help='List of comma separated ALLOWED_HOSTS values')

parser.add_argument('--python', dest='python', required=False, default=None, help='Python command. If not set, the Python used to run the program will be used')

parser.add_argument('--migrate', dest='migrate', required=False, action='store_true', help='Apply default migrations after creation')

parser.add_argument('--git', dest='git', required=False, action='store_true', help='Initialize git repo')

parser.add_argument('--commit', dest='commit', required=False, action='store_true', help='Make initial git commit')

parser.add_argument('--commit-message', dest='commit_message', required=False, default='Initial commit', help='Initial commit name')

parser.add_argument('--packages', dest='packages', nargs='+', help='Additional pip packages', required=False, default=[])

parser.add_argument('--no-compile', dest='no_compile', action='store_true', required=False, help='pip: Do not compile Python source files to bytecode')
