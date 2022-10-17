import os
import pprint


def debug_print(
    identifier: str,
    value: object | None = None,
    verbose=True,
    flush=True,
    long: bool = True,
):
    if verbose:
        if value is None:
            msg = "{i}".format(i=identifier)
        else:
            if isinstance(value, dict):
                value = "\n{}".format(pprint.pformat(value, indent=2))

            if long:
                msg = "Variable name:  {i}\nVariable value: {v}".format(
                    i=identifier, v=value
                )
            else:
                msg = "{i}: {v}".format(i=identifier, v=value)

        print(msg, flush=flush)
    return


def filtered_environment(
    add_toolbox_version: bool = True,
    prefixes: tuple[str] | set[str] | list[str] = ("BX", "PYTHON", "PATH", "PWD"),
):
    # NB do not add BATCHX to prefixes, contains private info.
    d = {k: v for k, v in os.environ.items() if any([e in k for e in prefixes])}

    if add_toolbox_version:
        try:
            from batchx_dev import __version__ as BX_PYTHON_TOOLBOX_VERSION

            d["BX_PYTHON_TOOLBOX_VERSION"] = BX_PYTHON_TOOLBOX_VERSION
        except Exception as e:
            debug_print(
                "Fetch BX_PYTHON_TOOLBOX_VERSION | Unexpected Exception.",
                e,
                verbose=True,
            )
    return d
