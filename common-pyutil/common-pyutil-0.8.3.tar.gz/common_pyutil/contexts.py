from contextlib import ExitStack


def call_with_contexts(func, contexts, *args, **kwargs):
    with ExitStack() as stack:
        for con in contexts:
            stack.enter_context(con)
        func(*args, **kwargs)
