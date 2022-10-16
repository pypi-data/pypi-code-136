"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-10-15
- Purpose: Main file that is invoked via `python -m exploration`.
    Accepts arguments or prompts the user for which command to execute
    and what file(s) to apply it to. Run `python -m exploration -h` for
    more information. See the `main` module for a Python-based API for
    the same functionality.
"""

from . import main

if __name__ == "__main__":
    options = main.parser.parse_args()
    if options.run == "show":
        main.show(
            options.source,
            formatOverride=options.format,
            step=options.step
        )
    elif options.run == "analyze":
        main.analyze(
            options.source,
            formatOverride=options.format
        )
    elif options.run == "convert":
        main.convert(
            options.source,
            options.destination,
            inputFormatOverride=options.format,
            outputFormatOverride=options.output_format,
            step=options.step
        )
    else:
        raise RuntimeError(
            f"Invalid 'run' default value: '{options.run}'."
        )
