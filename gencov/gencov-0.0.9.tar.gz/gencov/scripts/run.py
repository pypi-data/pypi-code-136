from importlib import import_module
from os.path import basename, splitext
from sys import argv, stderr, exc_info
from traceback import extract_tb


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


def dispatch(raw_args):

    info = '''
gencov values :::: get coverage values at loci
       profile ::: get coverage profile over loci
       quantify :: quantify coverage at loci
       normalize : normalize genome-wide coverage (bigwig)
       gene-expr : quantify gene expression (rna-seq)
'''

    if not raw_args:
        raise ValueError("no script selected")

    if raw_args[0] in ["-h", "--help"]:
        stderr.write(info.strip() + "\n")
        return

    try:
        name = raw_args[0].replace("-", "_")
        module = import_module(f".{name}", __package__)
    except ModuleNotFoundError:
        raise ValueError(f"invalid script: {raw_args[0]}")

    return module.main(raw_args[1:])


def main():
    try:
        dispatch(argv[1:])
    except KeyboardInterrupt:
        write_interrupt(*exc_info())
        raise SystemExit(1)
    except Exception:
        write_error(*exc_info())
        raise SystemExit(1)
