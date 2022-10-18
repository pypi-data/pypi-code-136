import atexit
import shutil
from functools import cache
from tempfile import mkdtemp

from datapac.package.artefact import Artefact
from datapac.package.package import match_files
from datapac.package.path import format
from datapac.rcave.sources.s3 import client
from datapac.rcave.utils.graph import S3Node
from datapac.utils import templating
from datapac.utils.environment import Environment


def get_output_path() -> str:
    return "artefacts/s3/{bucket}/{key:/}"


class S3Artefact(Artefact):
    source = "s3"

    bucket: str
    key: str
    tmp_path: str

    def __str__(self):
        return f"s3({self.bucket}, {self.key})"

    @property
    def output_path(self):
        return format(get_output_path(), bucket=self.bucket, key=self.key)

    def write(self, path: str):
        shutil.copyfile(self.tmp_path, path)

    def map(self, variables):
        return S3Artefact(
            bucket=templating.render(self.bucket, variables),
            key=templating.render(self.key, variables),
            tmp_path=self.tmp_path,
        )


def load_artefacts(path: str):
    files = match_files(path, get_output_path())
    return [S3Artefact(tmp_path=path, **kwargs) for path, kwargs in files]


@cache
def initialize_tmp_dir():
    tmp_dir = mkdtemp()
    atexit.register(shutil.rmtree, tmp_dir)
    return tmp_dir


def pull_node(env: Environment, node: S3Node, variables: dict):
    tmp_dir = initialize_tmp_dir()

    partial_bucket = templating.partial_render(
        node.bucket,
        {"parent": variables["parent"]},
    )
    partial_key = templating.partial_render(
        node.key,
        {"parent": variables["parent"]},
    )

    abs_path = f"{tmp_dir}/{partial_bucket}/{partial_key}"

    bucket = templating.render(node.bucket, variables)
    key = templating.render(node.key, variables)

    artefact = S3Artefact(
        bucket=partial_bucket,
        key=partial_key,
        tmp_path=abs_path,
    )

    print(f"[source:s3] pulling {artefact} artefact from s3://{bucket}/{key}")

    with client.connect(
        env.s3_endpoint_url,
        env.s3_access_key_id,
        env.s3_secret_access_key,
    ) as conn:
        client.download(conn, bucket, key, abs_path)

    return artefact


def push_artefacts(env: Environment, artefacts: list[S3Artefact]):
    with client.connect(
        env.s3_endpoint_url,
        env.s3_access_key_id,
        env.s3_secret_access_key,
    ) as conn:
        for artefact in artefacts:
            print(f"[source:s3] pushing {artefact} artefact")
            client.upload(conn, artefact.bucket, artefact.key, artefact.tmp_path)
