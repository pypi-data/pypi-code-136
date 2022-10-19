from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name
from hestia_earth.utils.api import download_hestia

from hestia_earth.orchestrator.log import logShouldRun
from hestia_earth.orchestrator.utils import get_required_model_param, find_term_match

_ALLOW_ALL = 'all'


def _lookup_values(term: dict, column: str):
    term_id = term.get('@id')
    term_type = term.get('termType')
    lookup = download_lookup(f"{term_type}.csv")
    values = get_table_value(lookup, 'termid', term_id, column_name(column))
    return (values or _ALLOW_ALL).split(';')


def _is_type_allowed(data: dict, term_id: str):
    node_type = data.get('@type', data.get('type'))
    term = download_hestia(term_id)
    allowed_types = _lookup_values(term, 'typesAllowed') if term else [_ALLOW_ALL]
    return True if _ALLOW_ALL in allowed_types or not node_type else node_type in allowed_types


_RUN_FROM_ARGS = {
    'runNonReliable': lambda node, _data: node.get('reliability', 1) >= 3,
    'runNonAddedTerm': lambda node, _data: 'term' not in node.get('added', []),
    'runNonMeasured': lambda node, _data: node.get('methodTier') != 'measured'
}


def _run_args(node: dict, args: dict, data: dict):
    keys = list(filter(lambda key: key in _RUN_FROM_ARGS and args[key] is True, args.keys()))
    return len(keys) > 0 and all([_RUN_FROM_ARGS[key](node, data) for key in keys])


def _is_empty(node: dict, skip_empty_value: bool = False):
    return node is None or all([
        not skip_empty_value,
        node.get('value') is None or node.get('value') == []
    ])


def should_run(data: dict, model: dict):
    key = get_required_model_param(model, 'key')
    term_id = get_required_model_param(model, 'value')
    args = model.get('runArgs', {})
    node = find_term_match(data.get(key, []), args.get('termId', term_id), None)
    # run if: value is empty or force run from args
    run = (_is_empty(node, args.get('skipEmptyValue', False)) or _run_args(node, args, data)) and all([
        _is_type_allowed(data, term_id)
    ])

    logShouldRun(data, model.get('model'), term_id, run, key=key, value=term_id)

    return run
