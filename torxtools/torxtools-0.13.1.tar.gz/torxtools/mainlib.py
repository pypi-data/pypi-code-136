import sys
import typing as t


def maincli(fn: t.Callable, *args, **kwargs) -> None:
    """
    TODO
    """
    try:
        return fn(*args, **kwargs)
    except KeyboardInterrupt:
        # exit code could be success or error, it all depends on if it's the
        # normal way of quitting the app.
        pass
    except SystemExit as err:
        if isinstance(err.code, int):
            return err.code
        print(err, file=sys.stderr)
        return 1
    except Exception as err:
        print(f"error: {err}", file=sys.stderr)
    return 1
