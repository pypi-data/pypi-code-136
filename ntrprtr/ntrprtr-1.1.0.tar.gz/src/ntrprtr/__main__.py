import sys
import json

import argparse

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--obj", "-o", type=int, required=True, help="Create a config with the given number of objects")
    parser.add_argument("--name", "-n", type=str, default="config.json", help="Name of the config file")
    args = parser.parse_args()

    config = []

    for i in range(0, args.obj):
        o = { "name": "Name", "description": "desc", "start": 0, "end": 0, "action": { "type": "type" }}
        config.append(o)

    j = json.dumps(config, indent=4)

    with open(args.name, "w")as f:
        f.write(j)



if __name__ == "__main__":
    sys.exit(main())
