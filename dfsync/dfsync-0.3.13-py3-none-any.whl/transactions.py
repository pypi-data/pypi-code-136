from decorator import decorator
from contextlib import contextmanager, ExitStack
from contextvars import ContextVar


class TransactionContext:
    def __init__(self, **kwargs):
        self._stack = None
        self._local_pragma = {}
        self._global_pragma = {**kwargs}
        self._currently_running = None

    def set_stack(self, stack):
        self._stack = stack

    def pragma(self, **kwargs):
        self._local_pragma.update(kwargs)

    def consume_pragma(self):
        result = {**self._global_pragma, **self._local_pragma}
        self._local_pragma = {}
        return result

    def enter_context(self, manager):
        try:
            if self._stack:
                return self._stack.enter_context(manager)
        finally:
            self.set_currently_running(None)

    def set_currently_running(self, op):
        self._currently_running = op


class TransactionOperation:
    def __init__(self, func, *args, **kwargs):
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
            ctx.set_currently_running(self)
            return self.func(*self.args, **self.kwargs)

        return ctx.enter_context(manager())


@decorator
def transaction_operation(func, *args, **kwargs):
    action = TransactionOperation(func, *args, **kwargs)
    return action.begin()


@contextmanager
def transaction(**kwargs):
    """
    Groups a set of operations that allocate resource into a transaction context.
    Any exception raised inside the transaction block will trigger the exception
    handling code of all the individual operations in reversed order.

    ```
    import os

    @transaction_operation
    def get_output_file(file_name):
        # Allocate the resource
        fd = open(file_name, "w")

        try:
            yield fd

            # Commit changes on successfully exiting the transaction
            fd.close()

        except:
            # Rollback changes
            fd.close()
            os.remove(file_name)
            raise  # Very important!


    def unreliable_code():
        raise ValueError("Unreliable code raises exceptions")

    def main():
        with transaction():
            primary = get_output_file("data.txt")
            print("Partial data", file=primary)

            secondary = get_output_file("secondary_data.txt")
            print("Partial data", file=secondary)

            # When this raises exceptions, the output files are rolled-back
            unreliable_code()
            print("Complete data", file=primary)
    ```

    """
    ctx = TransactionContext(**kwargs)
    previous_ctx_token = CURRENT_CONTEXT.set(ctx)
    try:
        with ExitStack() as stack:
            ctx.set_stack(stack)
            yield ctx
    finally:
        CURRENT_CONTEXT.reset(previous_ctx_token)


def get_operation_pragma(key):
    ctx = CURRENT_CONTEXT.get()
    if ctx._currently_running is None:
        return None
    return ctx._currently_running._pragma.get(key)


ROOT_CONTEXT = TransactionContext()
CURRENT_CONTEXT = ContextVar("Current transaction context", default=ROOT_CONTEXT)
