import sys
import json
import yaml
from jinja2 import Template


def transform(args):
    #
    # Read the dictionary from file
    #
    with open(args.dictionary.name) as f:
        dic_data = f.read()
    dic = json.loads(dic_data)

    #
    # Use the more secure SafeLoader if requested, see
    # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
    #
    if args.safeloader:
        loader = yaml.SafeLoader
    else:
        loader = yaml.FullLoader

    #
    # Transform the input file acording to the dictionary
    #
    content = Template(args.file.read()).render(dic)
    config = yaml.load(content, Loader=loader)

    if config is None:
        raise RuntimeError('Compose file is empty')

    yaml.safe_dump(config, args.output, default_flow_style=False)


def execute_docker_compose(filename, extras):
    from compose.cli.main import main as compose_main
    sys.argv[:] = ['docker-compose', '-f', filename] + extras
    compose_main()
