import contextlib
from typing import Dict, Any

from contextvars import ContextVar


class ContextData(object):
    def __init__(self, props: Dict[str, Any] = None, **kwargs):
        if props:
            for name, value in props.items():
                super().__setattr__(name, self._wrap(value))
        super().__setattr__('data', kwargs)

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return value

    def __setattr__(self, key, value):
        super().__setattr__(key, self._wrap(value))


_ctx: ContextVar[ContextData] = ContextVar('_ctx')


def get_context():
    if ctx := _ctx.get(None):
        return ctx
    _ctx.set(ContextData())
    return _ctx.get()


@contextlib.contextmanager
def with_context():
    token = _ctx.set(ContextData())
    yield _ctx.get(None)
    _ctx.reset(token)
