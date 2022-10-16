import os
import subprocess


def is_dbfs_fuse_available():
    with open(os.devnull, "w") as devnull_stderr, open(
        os.devnull, "w"
    ) as devnull_stdout:
        try:
            return (
                subprocess.call(
                    ["mountpoint", "/dbfs"],
                    stderr=devnull_stderr,
                    stdout=devnull_stdout,
                )
                == 0
            )
        except Exception:
            return False
