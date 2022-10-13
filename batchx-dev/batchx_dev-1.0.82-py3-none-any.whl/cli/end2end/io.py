from datetime import datetime

from batchx_dev.toolbox import Manifest, ManifestImprover, ReadmeImprover

from ..monkeypatch import Path


def make_initial_readme(readme_fp: Path, is_pipeline: bool = False):

    with open(readme_fp, "w") as f:
        f.write("")

    rmi = ReadmeImprover(readme_fp=readme_fp)

    with open(readme_fp, "w") as f:
        f.writelines(rmi.init_readme(is_pipeline=is_pipeline))
    return


def make_backup_copy(
    fp: Path, dp: Path = None, add_timestamp: bool = True, suffix: str = "backup"
):
    fp = Path(fp)

    if dp is None:
        dp = fp.parent / "backups"
    dp = Path(dp)
    dp.mkdir(exist_ok=True, parents=True)

    if add_timestamp:
        ts = datetime.now().isoformat().replace(":", "-").split(".")[0]
        suffix = "{s}-{t}".format(s=suffix, t=ts)

    bu_fp = fp.copy(dp / (fp.stem + "-" + suffix + fp.suffix))
    return bu_fp
