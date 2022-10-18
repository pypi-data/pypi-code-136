import re
from pandas.core.frame import DataFrame
from friendly_traceback import utils as ft_utils
from friendly_traceback.message_parser import get_parser
from friendly_traceback.info_variables import get_object_from_name

parser = get_parser(KeyError)
# The decorator parser.add will ensure that the function loc_does_not_exist
# is going to be used in an attempt to find the cause of the error before
# any similar functions from friendly_traceback would be used to do the same.
@parser.add
def loc_does_not_exist(message, traceback_data):
    # The message for a key error is not useful as it contains only
    # the unknown key.
    # Did we try to use loc?
    match = re.search(r"(.*)\.loc", traceback_data.bad_line)
    if match is None:
        # let the other registered handlers attempt to find an explanation
        return {}

    df = match[1]
    frame = traceback_data.exception_frame
    target = get_object_from_name(df, frame)
    if target is None:  # This is very unlikely to happen
        return {}

    if isinstance(target, DataFrame):
        # In the error message, the key shown is a string representation of
        # the actual key. This is the way to get the actual key.
        key = traceback_data.value.args[0]
        columns = list(target)
        if key in columns:
            # Note the use of backticks below to surround code: this is markdown notation that
            # friendly can use to add syntax coloring.
            hint = f'To retrieve a column, just use square brackets: `{df}["{key}"]`.\n'
            return {
                "cause": "You tried to use loc to retrieve a column, but it takes a row or a row selector.\n" + hint,
                "suggest": hint
            }
        else:
            rows = list(target.index.values)
            similar = ft_utils.get_similar_words(key, rows)
            if len(similar) == 1:
                hint = ("Did you mean `{name}`?\n").format(name=similar[0])
                cause = (
                    "`{name}` is a key of `{dict_}` which is similar to `{key}`.\n"
                ).format(name=similar[0], dict_=df, key=repr(key))
                return {"cause": cause, "suggest": hint}
            elif len(similar) > 1:
                hint = f"Did you mean `{similar[0]}`?\n"
                names = ", ".join(similar)
                cause = f"`{df}` has some keys similar to `{key!r}` including:\n`{names}`.\n"
                return {"cause": cause, "suggest": hint}

            rows = ft_utils.list_to_string(rows) # Remove the brackets surrounding list items
            return {
                "cause": (
                    f"You tried to retrieve an unknown row. The valid values are:\n`{rows}`.\n"
                )
            }
    return {}
