"""Functions for turning a grader definition into a grader object, and evaluating it."""

from grading_tools import graders  # noQA F401,F403
from grading_tools.graders import *  # noQA F401,F403
from grading_tools.loaders import *  # noQA F401,F403
from grading_tools.utils import nested_get, nested_set


def check_submission(defaults, submission):
    """Load grader definition defaults, submission, answer, and executes grading."""
    # This flag helps with not reloading fixture files
    if "fixtures_loaded" not in defaults:
        defaults["fixtures_loaded"] = False

    # Check for grader key
    if "grader" not in defaults:
        raise AttributeError(
            "The definition for this task is missing the `'grader'` key."
        )

    # Check that grader has required keys and values
    for key in ["type", "answer", "method"]:
        if key not in defaults["grader"]:
            raise AttributeError(
                f"defaults['grader'] is missing a '{key}' key."
            )

    # Check that grader specified exists
    if not hasattr(graders, defaults["grader"]["type"]):
        raise NameError(f"There is no {defaults['grader']['type']} grader.")

    # Load any files that will be used (if they haven't been loaded already)
    if ("loaders" in defaults) and defaults["fixtures_loaded"] is False:
        loaders = defaults["loaders"]
        if not isinstance(loaders, list):
            raise TypeError(
                "The value assigned to defaults['loaders'] must be a list, "
                f"not {type(loaders)}."
            )

        for loader in loaders:
            # Make sure the key-vals are there
            for key in ["file_key", "method"]:
                if key not in loader:
                    raise AttributeError(f"Loaders is missing a '{key}' key.")

            # Get filename
            fn_keys = loader["file_key"].split("__")
            fn = nested_get(defaults, fn_keys)

            # Load object
            load_method = loader["method"]
            kwargs = loader.get("kwargs", {})
            loaded_obj = eval(f"{load_method}('{fn}', **{kwargs})")

            # Assign object to `defaults` dict
            nested_set(defaults, fn_keys, loaded_obj)

        defaults["fixtures_loaded"] = True

    # Set up args for grader
    grader_dict = {
        "submission": submission,
        "answer": defaults["grader"]["answer"],
    }
    if "points" in defaults["grader"]:
        grader_dict["points"] = defaults["grader"].get("points", 1)

    # Create grader
    g_type = defaults["grader"]["type"]
    g = eval(f"{g_type}(**grader_dict)")

    # Execute grading
    params_dict = defaults["grader"].get("kwargs", {})
    grade_method = defaults["grader"].get("method")
    if defaults["fixtures_loaded"]:
        command = f"g.{grade_method}(**params_dict)"
    else:
        command = f"g.{grade_method}(**{params_dict})"
    eval(command)

    return g.return_feedback(html=defaults.get("feedback_html", True))
