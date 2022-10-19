from copy import deepcopy
from functools import reduce
from hestia_earth.schema import CompletenessJSONLD
from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name

from . import run as run_node, _import_model
from hestia_earth.orchestrator.utils import _new_practice, _filter_by_keys, find_term_match


def _full_completeness():
    completeness = CompletenessJSONLD().to_dict()
    keys = list(completeness.keys())
    keys.remove('@type')
    return {
        '@type': completeness['@type'],
        **reduce(lambda prev, curr: {**prev, curr: True}, keys, {})
    }


def _include_practice(practice: dict):
    term = practice.get('term', {})
    term_type = term.get('termType')
    term_id = term.get('@id')
    lookup = download_lookup(f"{term_type}.csv")
    value = get_table_value(lookup, 'termid', term_id, column_name('includeForTransformation'))
    return False if value is None or value == '' or not value else True


def _convert_transformation(cycle: dict, transformation: dict):
    data = deepcopy(transformation)
    # copy data from previous transformation
    data['dataCompleteness'] = _full_completeness()
    data['functionalUnit'] = cycle.get('functionalUnit')
    data['site'] = cycle.get('site')
    data['cycleDuration'] = transformation.get('transformationDuration', cycle.get('cycleDuration'))
    data['startDate'] = transformation.get('startDate', cycle.get('startDate'))
    data['endDate'] = transformation.get('endDate', cycle.get('endDate'))
    data['practices'] = [
        _new_practice(transformation.get('term'))  # add `term` as a Practice
    ] + transformation.get('practices', []) + [
        p for p in cycle.get('practices', []) if _include_practice(p)  # some practices need to be copied over
    ]
    return data


def _run_models(cycle: dict, transformation: dict, models: list):
    data = _convert_transformation(cycle, transformation)
    result = run_node(data, models)
    return _filter_by_keys(result, ['term', 'inputs', 'products', 'emissions'])


def _previous_transformation(cycle: dict, transformations: list, transformation: dict):
    term_id = transformation.get('previousTransformationTerm', {}).get('@id')
    return next(
        (v for v in transformations if v.get('term', {}).get('@id') == term_id),
        cycle
    )


def _apply_transformation_share(previous: dict, current: dict):
    share = current.get('previousTransformationShare', 100)
    products = previous.get('products', [])

    def replace_value(input: dict):
        product_value = find_term_match(products, input.get('term', {}).get('@id')).get('value', [])
        should_replace = len(product_value) > 0 and len(input.get('value', [])) == 0
        return {
            **input,
            **({'value': [v * share / 100 for v in product_value]} if should_replace else {})
        }

    return {**current, 'inputs': list(map(replace_value, current.get('inputs', [])))}


def _add_excreta_inputs(previous: dict, current: dict):
    run = _import_model('transformation.input.excreta').get('run')
    cycle = {
        **previous,
        '@type': 'Cycle',
        'transformations': [current]
    }
    # model will add the inputs directly in the transformation
    run(cycle)
    return current


def _run_transformation(cycle: dict, models: list):
    def run(transformations: list, transformation: dict):
        previous = _previous_transformation(cycle, transformations, transformation)
        transformation = _apply_transformation_share(previous, transformation)
        # add missing excreta Input when relevant
        transformation = _add_excreta_inputs(previous, transformation)
        transformation = _run_models(cycle, transformation, models)
        return transformations + [transformation]
    return run


def run(models: list, cycle: dict):
    transformations = cycle.get('transformations', [])
    return reduce(_run_transformation(cycle, models), transformations, [])
