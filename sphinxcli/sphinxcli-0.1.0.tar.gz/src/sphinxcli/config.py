from pathlib import Path


def get_sphinx_config(conf: Path) -> Path:
    if not conf.exists():
        raise ValueError(f"Sphinx configuration file '{conf}' not found")

    if conf.is_dir():
        conffile = conf / "conf.py"
        if not conffile.exists():
            raise ValueError(f"Sphinx configuration file 'conf.py' not found in {conf}")
    else:
        conffile = conf
        if not conffile.exists():
            raise ValueError(f"Sphinx configuration file '{conffile}' not found.")

    return conffile
