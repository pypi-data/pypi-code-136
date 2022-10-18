import os


def is_worker_process() -> bool:
    """
    Returns True if the current process is a part of a distributed cluster
    and is not the master process - it means it should not write files or metrics
    """
    if os.environ.get("LOCAL_RANK", "0") != "0":  # pytorch DistributedDataParallel
        return True
    return False
