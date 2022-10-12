# std
from functools import wraps


def tag_implies_commit(func):
    @wraps(func)
    def tag_implies_commit_wrapper(*, commit: bool = False, tag: bool = False, **kwargs):
        if tag:
            commit = True
        return func(commit=commit, tag=tag, **kwargs)
    return tag_implies_commit_wrapper
