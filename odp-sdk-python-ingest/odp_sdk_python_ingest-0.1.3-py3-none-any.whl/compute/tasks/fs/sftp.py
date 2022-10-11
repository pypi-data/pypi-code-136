from typing import Optional, List, Callable, Union, Any, BinaryIO, Tuple
from urllib.parse import urlparse
import tempfile
from os import path
from functools import partial

from paramiko import SFTPAttributes
from prefect import Task
from prefect.utilities.tasks import defaults_from_attrs
import pysftp

import logging

__all__ = ["SftpList", "SftpGet"]

from odp.compute.metrics import Metrics, get_prefect_labels, get_prefect_label_names

LOG = logging.getLogger(__name__)


class SftpList(Task):
    def __init__(self, dir: Optional[str] = None, **kwargs):
        self.dir = dir
        super().__init__(**kwargs, nout=True)

    @defaults_from_attrs("dir")
    def run(
        self,
        connection_string: str,
        dir: str = None,
    ) -> List[Tuple[str, SFTPAttributes]]:
        parsed = urlparse(connection_string)
        username = parsed.username
        password = parsed.password
        host = parsed.hostname
        base_dir = parsed.path
        port = parsed.port or 22

        dir = path.join(base_dir, dir)

        LOG.info(f"LIST '{dir}': host={host}, port={port}, username={username}")

        with pysftp.Connection(
            host, username=username, password=password, port=port
        ) as sftp:
            files = sftp.listdir(dir)
            return [(x, sftp.stat(x)) for x in files]


class SftpGet(Task):
    def __init__(
        self,
        file_path: Optional[str] = None,
        decode_cb: Optional[Callable[[BinaryIO, str, str], Any]] = None,
        **kwargs,
    ):
        self.file_path = file_path
        self.decode_cb = decode_cb
        self.bytes_downloaded = 0

        self.bytes_downloaded_counter = Metrics.counter(
            name="bytes_downloaded",
            namespace=__name__.replace(".", "_"),
            labels=get_prefect_label_names("fname"),
        )

        super().__init__(**kwargs)

    @defaults_from_attrs("file_path", "decode_cb")
    def run(
        self,
        connection_string: str,
        file_path: str = None,
        decode_cb: Optional[Callable[[BinaryIO, str, str], Any]] = None,
    ) -> Any:
        parsed = urlparse(connection_string)
        username = parsed.username
        password = parsed.password
        host = parsed.hostname
        base_dir = parsed.path
        port = parsed.port or 22

        file_path = path.join(base_dir, file_path)

        LOG.info(f"GET '{file_path}': host={host}, port={port}, username={username}")

        with pysftp.Connection(
            host, username=username, password=password, port=port
        ) as sftp:

            fname = file_path.split("/")[-1]

            with tempfile.TemporaryDirectory() as tmpdir:
                local_path = path.join(tmpdir, fname)

                sftp.get(
                    remotepath=file_path,
                    localpath=local_path,
                    callback=partial(self._download_cb, file_path),
                    preserve_mtime=True,
                )

                Metrics.push()

                with open(local_path, "rb") as fd:
                    if decode_cb:
                        return decode_cb(fd, file_path, local_path)
                    else:
                        return fd.read()

    def _download_cb(
        self, fname: str, bytes_transferred: int, bytes_total: int
    ) -> None:

        LOG.debug(
            f"[{fname}] Bytes transferred: {bytes_transferred} / {bytes_total} ({100. * bytes_transferred / bytes_total:.3f} %"
        )

        self.bytes_downloaded_counter.inc(
            bytes_transferred - self.bytes_downloaded, labels=get_prefect_labels(fname)
        )
        self.bytes_downloaded = bytes_transferred

        Metrics.push()
