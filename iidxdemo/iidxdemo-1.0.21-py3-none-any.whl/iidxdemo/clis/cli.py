import datetime
import pathlib


def main():
    print(datetime.datetime.now(), "main")
    cwd = pathlib.Path(__file__).parent
    dir_pkg = cwd.parent
    dir_cfg = cwd.parent / "cfg"
    cfg_version = dir_cfg / "version.txt"
    if cfg_version.exists():
        print(f"exists: {cfg_version}")
        with open(cfg_version, "r") as f:
            for line in f.readlines():
                print(line)
    else:
        print("not exists")


if __name__ == '__main__':
    main()
