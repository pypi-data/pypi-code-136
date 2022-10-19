import yaml


class AttackArguments:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            args = yaml.load(file, Loader=yaml.FullLoader)
        for k, v in args.items():
            setattr(self, k, v)
