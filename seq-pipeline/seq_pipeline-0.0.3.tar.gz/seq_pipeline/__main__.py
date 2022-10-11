from os.path import basename, splitext
from sys import argv, stderr, exc_info
from traceback import extract_tb

if __package__:
    from .process.main import main
else:
    from process.main import main


def process_exc_trace(exc_trace):
    stack = extract_tb(exc_trace)
    location = " > ".join(
        f"{splitext(basename(part[0]))[0]}.{part[2]}:{part[1]}"
        for part in stack[1:])
    return stack, location


def write_error(exc_type, exc_value, exc_trace):
    stack, location = process_exc_trace(exc_trace)
    message = "ERROR\n" \
        f" -> Location: {location}\n" \
        f" -> Line: {stack[-1][3]}\n" \
        f" -> {exc_type.__name__}: {exc_value}"
    stderr.write(f"{message}\n")


def write_interrupt(exc_type, exc_value, exc_trace):
    stack, location = process_exc_trace(exc_trace)
    message = " INTERRUPTED\n" \
        f" -> Location: {location}\n" \
        f" -> Line: {stack[-1][3]}"
    stderr.write(f"{message}\n")


if __name__ == "__main__":
    try:
        main(argv[1:])
    except KeyboardInterrupt:
        write_interrupt(*exc_info())
        raise SystemExit(1)
    except Exception:
        write_error(*exc_info())
        raise SystemExit(1)
