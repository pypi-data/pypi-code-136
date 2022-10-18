from datapac.package.package import Package
from datapac.package.package import open as pkg_open
from datapac.package.package import render
from datapac.rcave.sources.postgres import source as postgres
from datapac.rcave.sources.s3 import source as s3
from datapac.utils.environment import Environment

open = pkg_open


def push(env: Environment, pkg: Package, variables: dict):
    with render(pkg, variables) as rendered:
        postgres.push_artefacts(
            env, [a for a in rendered.artefacts if a.source == "postgres"]
        )

        s3.push_artefacts(env, [a for a in rendered.artefacts if a.source == "s3"])
