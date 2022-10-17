from typing import List, Dict, Any, Callable


def recurse_dict(obj: Dict[Any, Any],
                 pred: Callable[[Any, Any], bool],
                 repl: Callable[[Any, Any], Any],
                 repl_only: bool = False) -> Dict[Any, Any]:
    """Recurse over a :class:`dict` and perform replacement.

    This function replaces the values of the dictionary in place. The predicate
    is based upon a (key, value) pair and if any object is not a :class:`dict`
    or :class:`list` it's returned as is.

    Args:
        obj: A dictionary
        pred: Predicate to check when to perform replacement
        repl: Function which performs the replacement
        repl_only: If True then stop at first replacement

    Returns:
        A modified dictionary

    """
    if not (isinstance(obj, dict) or isinstance(obj, list)):
        return obj
    if isinstance(obj, dict):
        for k, v in obj.items():
            if pred(k, v):
                obj[k] = repl(k, v)
                if repl_only:
                    continue
            if isinstance(v, dict):
                obj[k] = recurse_dict(v, pred, repl, repl_only)
            if isinstance(v, list):
                for i, item in enumerate(v):
                    v[i] = recurse_dict(item, pred, repl, repl_only)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            obj[i] = recurse_dict(item, pred, repl, repl_only)
    return obj


def recurse_dict_pred_val(obj: Dict[Any, Any],
                          pred: Callable[[Any], bool],
                          repl: Callable[[Any], Any]) -> Dict[Any, Any]:
    """Recurse over a :class:`dict` and perform replacement.

    This function replaces the values of the dictionary in place. Used to
    fix the generated schema :class:`dict`.

    Args:
        obj: A dictionary
        pred: Predicate to check when to perform replacement
        repl: Function which performs the replacement

    Returns:
        A modified dictionary

    """
    if not (isinstance(obj, dict) or isinstance(obj, list)):
        return obj
    if isinstance(obj, dict):
        for k, v in obj.items():
            if pred(v):
                obj[k] = repl(v)
            if isinstance(v, dict):
                obj[k] = recurse_dict_pred_val(v, pred, repl)
            if isinstance(v, list):
                for i, item in enumerate(v):
                    v[i] = recurse_dict_pred_val(item, pred, repl)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            obj[i] = recurse_dict_pred_val(item, pred, repl)
    return obj
