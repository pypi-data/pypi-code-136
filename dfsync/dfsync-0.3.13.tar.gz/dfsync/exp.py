import sys
from decorator import decorator
from contextlib import contextmanager, ExitStack
from contextvars import ContextVar


class Rollback(Exception):
    pass


class RollbackOverridden(Exception):
    pass


class InvalidActionException(Exception):
    pass


META_NO_ROLLBACK = "no_rollback"
META_RETRY_COUNT = "retry"


class TransactionContext:
    def __init__(self, **kwargs):
        self._stack = None
        self._local_pragma = {}
        self._global_pragma = {**kwargs}

    def set_stack(self, stack):
        self._stack = stack

    def pragma(self, **kwargs):
        self._local_pragma.update(kwargs)

    def consume_pragma(self):
        result = {**self._global_pragma, **self._local_pragma}
        self._local_pragma = {}
        return result

    def enter_context(self, manager):
        return self._stack.enter_context(manager)


ROOT_CONTEXT = TransactionContext()
CURRENT_CONTEXT = ContextVar("Current transaction context", default=ROOT_CONTEXT)


class ReversibleAction:
    def __init__(self, func, args: list, kwargs: dict):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self._pragma = {}

    def set_metadata(self, metadata):
        self._metadata = metadata

    def begin(self):
        ctx = CURRENT_CONTEXT.get()
        self._pragma = ctx.consume_pragma()

        @contextmanager
        def manager():
            return self.func(*self.args, **self.kwargs)

        return ctx.enter_context(manager())


@decorator
def transaction_operation(func, *args, **kwargs):
    action = ReversibleAction(func, args, kwargs)
    return action.begin()


@contextmanager
def transaction():
    ctx = TransactionContext()
    previous_ctx_token = CURRENT_CONTEXT.set(ctx)
    try:
        with ExitStack() as stack:
            ctx.set_stack(stack)
            yield ctx
    finally:
        CURRENT_CONTEXT.reset(previous_ctx_token)


RESOURCES = {}


@transaction_operation
def allocate_resource(arg: str):
    print(f"allocate {arg}")
    resource = f"STEP: allocate {arg}"
    RESOURCES[arg] = resource

    try:
        yield resource
        print(f"commit({arg})")

    except Exception as e:
        print(f"rollback({arg})")
        del RESOURCES[arg]
        raise


@transaction_operation
def basic_resource_alloc():
    yield "Allocated"


@transaction_operation
def broken_resource_alloc():
    yield "Broken"
    yield "Broken2"


import os


@transaction_operation
def get_output_file(file_name):
    # Allocate the resource
    fd = open(file_name, "w")

    try:
        yield fd

        # Commit the changes
        fd.close()

    except:
        # Rollback changes
        fd.close()
        os.remove(file_name)
        raise  # Very important!


def main():
    with transaction() as ctx:
        res = None

        ctx.pragma(retry_on=Exception, retry_count=3)
        res = allocate_resource("vm_snapshot")
        print(res)

        res = allocate_resource("volume snapshot")
        print(res)

        fd = get_output_file("mihai.txt")
        print("Partial data", file=fd)

        raise ValueError()
        print("Partial data", file=fd)


if __name__ == "__main__":
    try:
        main()
    finally:
        print(RESOURCES)
