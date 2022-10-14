import json
from random import choice
from typing import Optional, Tuple, List, Union

from .. import classification_loop, experts, feedback_loop, mapping, pool as pool_config

import toloka.client as toloka


def get_pool_id(name: Optional[str]) -> Optional[str]:
    if name is None:
        return None
    try:
        with open(f'{name}.json', 'r') as file:
            return json.load(file)['pool_id']
    except (TypeError, FileNotFoundError, KeyError, ValueError):
        return None


def get_classification_pool(
    client: toloka.TolokaClient,
    name: Optional[str],
    loop: Union[experts.ExpertPipeline, classification_loop.ClassificationLoop],
    pool_cfg: Union[pool_config.ExpertConfig, pool_config.ClassificationConfig],
    control_objects: Optional[List[mapping.TaskSingleSolution]] = None,
) -> toloka.Pool:
    pool_id = get_pool_id(name)
    if pool_id is not None:
        return client.get_pool(pool_id)

    if isinstance(loop, experts.ExpertPipeline):
        assert control_objects is None
        pool = loop.create_pool(pool_cfg)
    else:
        pool = loop.create_pool(control_objects, pool_cfg)

    if name is not None:
        with open(f'{name}.json', 'w') as file:
            json.dump({'pool_id': pool.id}, file)

    return pool


def get_annotation_pools(
    client: toloka.TolokaClient,
    name: Optional[str],
    fb_loop: feedback_loop.FeedbackLoop,
    check_pool_cfg: pool_config.ClassificationConfig,
    markup_pool_cfg: pool_config.MarkupConfig,
    control_objects: List[mapping.TaskSingleSolution],
) -> Tuple[toloka.Pool, toloka.Pool]:
    pool_ids = get_pool_ids(name)

    if pool_ids is None:
        markup_pool, check_pool = fb_loop.create_pools(control_objects, markup_pool_cfg, check_pool_cfg)
    else:
        check_pool_id, markup_pool_id = pool_ids
        check_pool = client.get_pool(check_pool_id)
        markup_pool = client.get_pool(markup_pool_id)

    if name is not None:
        with open(f'{name}.json', 'w') as file:
            json.dump({'check_pool_id': check_pool.id, 'markup_pool_id': markup_pool.id}, file)

    return markup_pool, check_pool


def get_pool_ids(name: Optional[str]) -> Optional[Tuple[str, str]]:
    if name is None:
        return None
    try:
        with open(f'{name}.json', 'r') as file:
            data = json.load(file)
            return data['check_pool_id'], data['check_pool_id']
    except (TypeError, FileNotFoundError, KeyError, ValueError):
        return None


def get_swaps(name: Optional[str], input_objects: List[mapping.Objects]) -> List[bool]:
    if name is not None:
        try:
            with open(f'{name}-swaps.json', 'r') as file:
                return json.load(file)
        except (TypeError, FileNotFoundError, KeyError, ValueError):
            pass
    swaps = [choice((True, False)) for _ in input_objects]

    if name is not None:
        with open(f'{name}-swaps.json', 'w') as file:
            json.dump(swaps, file)

    return swaps
