import argparse
from jinja_docker_compose import jinja_docker_compose as jinja


def filehandle_if_exists_else_none(fname):
    try:
        return open(fname, 'r')
    except FileNotFoundError:
        return None


def open_compose_file(fname):
    if not fname:
        return filehandle_if_exists_else_none('docker-compose.yaml.j2') \
            or filehandle_if_exists_else_none('docker-compose.yml.j2')
    else:
        return filehandle_if_exists_else_none(fname)


def open_dictionary_file(fname):
    if not fname:
        return filehandle_if_exists_else_none('docker-compose.dic')
    else:
        return filehandle_if_exists_else_none(fname)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', metavar='INPUT_FILE',
                        type=open_compose_file,
                        default='',
                        help='Specify the yaml file to be transformed,'
                        ' default is docker-compose.yaml.j2'
                        ' and if that does not exist'
                        ' docker-compose.yml.j2')
    parser.add_argument('-D', '--dictionary', metavar='DICTIONARY_FILE',
                        type=open_dictionary_file,
                        default='',
                        help='Specify the dictionary file to use, default is'
                        ' docker-compose.dic.')
    parser.add_argument('-o', '--output', metavar='OUTPUT_FILE',
                        type=argparse.FileType('w'),
                        default='docker-compose.yml',
                        help='Specify an alternate output compose file'
                        ' (default: docker-compose.yml)')
    parser.add_argument('-G', '--generate', action='store_true',
                        help='Generate output compose file and exit,'
                        ' do not run docker-compose')
    parser.add_argument('-s', '--safeloader', action='store_true',
                        help='Uses the SafeLoader when loading the YAML,'
                        ' this removes the possible exploit that the default'
                        ' FullLoader enables')

    (args, extras) = parser.parse_known_args()

    jinja.transform(args)

    #
    # Do not run docker-compose if disabled
    #
    if not args.generate:
        jinja.execute_docker_compose(args.output.name, extras)
