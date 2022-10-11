import logging
import argparse
import importlib.util
import sys

from .config import Config
from .app import App

def run():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)-14s[L:%(lineno)-4d]# %(levelname)-8s[%(asctime)s] (%(funcName)s) %(message)s"
    )
    parser = argparse.ArgumentParser(usage="python run.py -c config.py")
    parser.add_argument("-c", help="config", metavar='./config.py', type=str, required=True)
    args = parser.parse_args()
    if args.c:
        try:
            spec = importlib.util.spec_from_file_location("run_config", args.c)
            runConfig = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(runConfig)
            config = Config(chats=runConfig.CHATS, tasks=runConfig.TASKS)
            selfName = runConfig.SELF_NAME
            logging.getLogger("cmb").info(f"start with config {args.c}")
        except Exception as e:
            logging.getLogger("cmb").critical(f"{e}, parse config error", exc_info=True)
            sys.exit(1)
        app = App(selfName=selfName, config=config, tz=getattr(runConfig, "TZ", None))
        app.run()

if __name__ == "__main__":
    run()
