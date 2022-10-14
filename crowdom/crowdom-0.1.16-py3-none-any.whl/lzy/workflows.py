from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict

from lzy.api.v1 import op
from lzy.api.v1.whiteboard import whiteboard, view
import toloka.client as toloka

from .. import base, client, classification, classification_loop, mapping, pool as pool_config


@dataclass
class Results:
    raw_results: List[Tuple[Optional[classification.TaskLabelsProbas], List[classification.WorkerLabel]]]
    worker_weights: Optional[Dict[str, float]]


@whiteboard(tags=['classification'], namespace='default')
@dataclass
class Whiteboard:
    task_spec: base.TaskSpec
    params: client.params.Params
    project: toloka.Project
    lang: str
    input_objects: List[mapping.Objects]
    control_objects: List[mapping.TaskSingleSolution]

    pool: toloka.Pool = None  # TODO: need to refresh it after end of process, to get actual values for stopped_at
    results: Results = None

    @view
    def to_results(self) -> Results:
        return self.results


@op
def create_pool(
    loop: classification_loop.ClassificationLoop,
    control_objects: List[mapping.TaskSingleSolution],
    pool_cfg: pool_config.ClassificationConfig,
) -> toloka.Pool:
    return loop.create_pool(control_objects, pool_cfg)


@op
def add_input_objects(
    loop: classification_loop.ClassificationLoop,
    input_objects: List[mapping.Objects],
    pool: toloka.Pool,
) -> None:
    loop.add_input_objects(pool.id, input_objects)


@op
def run_loop(
    loop: classification_loop.ClassificationLoop,
    pool: toloka.Pool,
) -> None:
    loop.loop(pool.id)


@op
def get_results(
    loop: classification_loop.ClassificationLoop,
    input_objects: List[mapping.Objects],
    pool: toloka.Pool,
) -> Results:
    result = loop.get_results(pool.id, input_objects)
    return Results(result[0], result[1])
