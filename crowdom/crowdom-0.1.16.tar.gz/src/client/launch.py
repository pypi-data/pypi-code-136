from datetime import timedelta
import logging
import threading
from typing import List, Optional, Tuple, Dict, Union, Type

# from lzy.api.v1 import LzyRemoteEnv
import toloka.client as toloka

from .. import (
    base,
    classification,
    classification_loop,
    datasource,
    experts,
    feedback_loop,
    mapping,
    mos,
    metrics,
    pool as pool_config,
    project,
    worker,
)
from ..utils import LaunchInterrupter
from .display import get_pool_price, get_annotation_price

# from ..lzy import Whiteboard, add_input_objects, create_pool, run_loop, get_results

from .params import ExpertParams, Params, AnnotationParams
from .task import PreparedTaskSpec, AnnotationTaskSpec, check_project
from .training import find_training_requirement
from .utils import ask, validate_objects_volume
from .relaunch import get_classification_pool, get_annotation_pools

logger = logging.getLogger(__name__)


def create_toloka_client(
    token: str,
    environment: toloka.TolokaClient.Environment = toloka.TolokaClient.Environment.PRODUCTION,
) -> toloka.TolokaClient:
    return toloka.TolokaClient(token=token, environment=environment, retries=20, timeout=(60.0, 240.0))


def launch(
    task_spec: PreparedTaskSpec,
    params: Params,
    input_objects: List[mapping.Objects],
    control_objects: List[mapping.TaskSingleSolution],  # assisted by us
    client: toloka.TolokaClient,
    interactive: bool = False,
    interrupted: Optional[threading.Event] = None,
    name: Optional[str] = None,
) -> Tuple[
    List[Tuple[Optional[classification.TaskLabelsProbas], List[classification.WorkerLabel]]],
    Optional[Dict[str, float]],
]:
    result = _launch(
        task_spec,
        params,
        input_objects,
        control_objects,
        client,
        interactive,
        interrupted,
        name=name,
    )
    if result is None:
        return [], None

    loop, pool_id = result
    return loop.get_results(pool_id, input_objects)


def launch_mos(
    task_spec: PreparedTaskSpec,
    params: Params,
    input_objects: List[mapping.Objects],
    client: toloka.TolokaClient,
    interactive: bool = False,
    interrupted: Optional[threading.Event] = None,
    inputs_to_metadata: Optional[Dict[mapping.Objects, mos.ObjectsMetadata]] = None,
    name: Optional[str] = None,
) -> Tuple[
    List[Tuple[Optional[classification.TaskLabelsProbas], List[classification.WorkerLabel]]],
    Optional[Dict[str, float]],
    Dict,
]:
    result = _launch(
        task_spec,
        params,
        input_objects,
        [],
        client,
        interactive,
        interrupted,
        name=name,
        loop_cls=classification_loop.MOSLoop,
        inputs_to_metadata=inputs_to_metadata,
    )

    if result is None:
        return [], None, {}

    loop, pool_id = result

    return loop.get_results(pool_id, input_objects) + (
        loop.assignment_evaluation_strategy.final_assignment_set.get_algorithm_ci(),
    )


def _launch(
    task_spec: PreparedTaskSpec,
    params: Params,
    input_objects: List[mapping.Objects],
    control_objects: List[mapping.TaskSingleSolution],
    client: toloka.TolokaClient,
    interactive: bool = False,
    interrupted: Optional[threading.Event] = None,
    name: Optional[str] = None,
    loop_cls: Type[classification_loop.ClassificationLoop] = classification_loop.ClassificationLoop,
    **kwargs,
) -> Optional[Tuple[classification_loop.ClassificationLoop, str]]:
    assert task_spec.scenario == project.Scenario.DEFAULT, 'You should use this function for crowd markup only'
    assert isinstance(params.task_duration_hint, timedelta)
    assert mapping.validation_enabled
    datasource.assert_tasks_are_unique(input_objects)
    datasource.assert_tasks_are_unique(control_objects)

    prj = check_project(task_spec, client)

    if not validate_objects_volume(
        input_objects,
        control_objects,
        params.task_duration_hint,
        params.pricing_config,
        interactive,
    ):
        return None

    if type(task_spec.function) not in (base.ClassificationFunction, base.SbSFunction):
        raise ValueError(f'unsupported task function: {task_spec.function}')

    # todo: check this some other way - assert isinstance(params, ClassificationLaunchParams)

    interrupter = LaunchInterrupter(client, interrupted or threading.Event())

    if interactive:
        pool_price = get_pool_price(len(input_objects), params.pricing_config, params.overlap, display_formula=True)
        if not ask(f'run classification of {len(input_objects)} objects for {pool_price}?'):
            return None
    loop = loop_cls(
        client,
        task_spec.task_mapping,
        params.classification_loop_params,
        task_spec.lang,
        interrupter,
        with_control_tasks=params.pricing_config.control_tasks_count > 0,
        **kwargs,
    )
    real_tasks_count = params.real_tasks_count
    control_tasks_count = params.control_tasks_count
    training_requirement = find_training_requirement(prj.id, task_spec, client, params)
    pool_cfg = pool_config.ClassificationConfig(
        project_id=prj.id,
        private_name=name or 'pool',
        reward_per_assignment=params.assignment_price,
        task_duration_hint=params.task_duration_hint,
        real_tasks_count=real_tasks_count,
        control_tasks_count=control_tasks_count,
        overlap=params.overlap.min_overlap,
        control_params=params.control,
        worker_filter=params.worker_filter,
        training_requirement=training_requirement,
    )

    pool = get_classification_pool(client, name, loop, pool_cfg, control_objects)
    interrupter.add_pool_id(pool.id)

    plotter = None
    if interactive:
        plotter = metrics.ClassificationMetricsPlotter(
            toloka_client=client,
            stop_event=interrupter.interrupted,
            task_mapping=task_spec.task_mapping,
            pool_id=pool.id,
            task_duration_hint=params.task_duration_hint,
            params=params.classification_loop_params,
            assignment_evaluation_strategy=loop.assignment_evaluation_strategy,
        )

    try:
        loop.add_input_objects(pool.id, input_objects)
        logger.info('classification has started')
        loop.loop(pool.id)
    except KeyboardInterrupt:
        interrupter.shutdown()
        return None
    finally:
        interrupter.interrupted.set()
        if plotter:
            plotter.join()

    return loop, pool.id

    # wb = Whiteboard(
    #     task_spec=task_spec.task_spec,
    #     params=params,
    #     project=prj,
    #     lang=task_spec.lang,
    #     input_objects=input_objects,
    #     control_objects=control_objects)
    #
    # env = LzyRemoteEnv()
    # with env.workflow('classification', whiteboard=wb):
    #     wb.pool = create_pool(loop, control_objects, pool_cfg)
    #     add_input_objects(loop, input_objects, wb.pool)
    #     run_loop(loop, wb.pool)
    #     wb.results = get_results(loop, input_objects, wb.pool)
    #     wb_id = wb.__id__
    #
    # return wb_id


# tmp routine, while we didn't implement pipeline in lzy
def select_control_tasks(
    input_objects: List[mapping.Objects],
    results: Union[
        List[Tuple[classification.TaskLabelsProbas, List[classification.WorkerLabel]]], List[feedback_loop.TaskResult]
    ],
    min_confidence: float,
    min_overlap: int = 1,
) -> List[mapping.TaskSingleSolution]:
    control_tasks = []
    if not isinstance(results[0], feedback_loop.TaskResult):
        for task_input_objects, (labels_probas, raw_labels) in zip(input_objects, results):
            label, proba = classification.get_most_probable_label(labels_probas)
            if len(raw_labels) >= min_overlap and proba >= min_confidence:
                control_tasks.append((task_input_objects, (label,)))
        return control_tasks

    for result in results:
        if not result.solutions:
            continue
        task, best_solution = result.task, result.solutions[0]
        # if we have non-trivial check_sample, there can be good annotations without evaluation - unknown confidence
        # however, in case of min_confidence == 0 we may want to receive TaskSingleSolution for _each_ input object
        if not best_solution.evaluation:
            continue
        solution, proba = best_solution.solution, best_solution.evaluation.confidence
        raw_labels = best_solution.evaluation.worker_labels
        if len(raw_labels) >= min_overlap and proba >= min_confidence:
            control_tasks.append((task, solution))
    return control_tasks


# todo реальные пулы нельзя создавать с 0 стоимостью. мб можно все делать в сэндбоксе
# todo вообще нужно корректировать task_duration с учетом сценариев
def launch_experts(
    task_spec: PreparedTaskSpec,
    params: ExpertParams,
    input_objects: Union[List[mapping.Objects], List[mapping.TaskSingleSolution]],
    case: experts.ExpertCase,
    client: toloka.TolokaClient,
    name: Optional[str] = None,
    interactive: bool = False,
) -> List[Tuple[Union[mapping.TaskSingleSolution, mapping.Objects], mapping.TaskMultipleSolutions]]:
    assert task_spec.scenario != project.Scenario.DEFAULT, 'You should use this function for expert markup only'
    assert isinstance(params.task_duration_hint, timedelta)
    assert mapping.validation_enabled

    prj = check_project(task_spec, client)

    assignment_price = params.assignment_price
    pipeline = experts.ExpertPipeline(
        client, task_spec.function, task_spec.task_mapping, task_spec.lang, scenario=task_spec.scenario
    )

    skills = experts.get_skills(task_spec.id, task_spec.lang, client)
    assert skills, f'No suitable skills found for task spec {task_spec.id} and lang {task_spec.lang}'
    logger.debug(f'Using found skills: {skills}')

    if interactive:
        pool_price = get_pool_price(
            len(input_objects),
            params.pricing_config,
            classification_loop.StaticOverlap(overlap=1),
            display_formula=True,
        )
        if not ask(f'run expert labeling of {len(input_objects)} objects for {pool_price}?'):
            return []

    interrupter = LaunchInterrupter(client, threading.Event())

    pool_cfg = pool_config.ExpertConfig(
        project_id=prj.id,
        private_name=name or 'pool',
        public_description=case.label[task_spec.lang],
        reward_per_assignment=assignment_price,
        task_duration_hint=params.task_duration_hint,
        real_tasks_count=params.pricing_config.get_tasks_count(),
        worker_filter=worker.ExpertFilter([skill for (_, skill) in skills]),
    )

    pool = get_classification_pool(client, name, pipeline, pool_cfg)
    interrupter.add_pool_id(pool.id)

    # todo some extra functionality will be lost here without lzy graph rearrangements - e.q. pre-/post-swaps in sbs
    try:
        pipeline.add_input_objects(pool.id, input_objects)
        logger.info('expert labeling has started')
        pipeline.loop(pool.id)
    except KeyboardInterrupt:
        interrupter.shutdown(reraise=False)

    return pipeline.get_results(pool.id, input_objects)


def launch_annotation(
    task_spec: AnnotationTaskSpec,
    params: AnnotationParams,
    check_params: Params,
    input_objects: List[mapping.Objects],
    control_objects: List[mapping.TaskSingleSolution],  # assisted by us
    client: toloka.TolokaClient,
    interactive: bool = False,
    interrupted: Optional[threading.Event] = None,
    name: Optional[str] = None,
    s3: Optional[datasource.S3] = None,
) -> Tuple[List[feedback_loop.TaskResult], Optional[Dict[str, float]]]:
    assert task_spec.scenario == project.Scenario.DEFAULT, 'You should use this function for crowd markup only'
    assert isinstance(params.task_duration_hint, timedelta)
    assert isinstance(check_params.task_duration_hint, timedelta)
    assert mapping.validation_enabled
    datasource.assert_tasks_are_unique(input_objects)
    datasource.assert_tasks_are_unique(control_objects)

    markup_prj = check_project(task_spec, client)
    check_prj = check_project(task_spec.check, client)
    # todo: validate_objects_volume

    for obj in task_spec.function.get_outputs():
        if obj.type.is_media():
            assert s3 is not None, 'S3 client is required for media-output tasks'

    interrupter = LaunchInterrupter(client, interrupted or threading.Event())

    if interactive:
        annotation_price = get_annotation_price(
            input_objects_count=len(input_objects),
            markup_config=params.pricing_config,
            check_config=check_params.pricing_config,
            markup_overlap=params.overlap,
            check_overlap=check_params.overlap,
            assignment_check_sample=params.assignment_check_sample,
            display_formula=True,
        )
        if not ask(f'run annotation of {len(input_objects)} objects for {annotation_price}?'):
            return [], None

    fb_loop = feedback_loop.FeedbackLoop(
        pool_input_objects=input_objects,
        markup_task_mapping=task_spec.task_mapping,
        check_task_mapping=task_spec.check.task_mapping,
        markup_params=params.feedback_loop_params,
        check_params=check_params.classification_loop_params,
        client=client,
        lang=task_spec.lang,
        interrupter=interrupter,
        s3=s3,
        model_markup=params.model,
        model_check=check_params.model,
    )

    check_training_requirement = find_training_requirement(check_prj.id, task_spec.check, client, check_params)
    markup_training_requirement = find_training_requirement(markup_prj.id, task_spec, client, params)

    check_pool_cfg = pool_config.ClassificationConfig(
        project_id=check_prj.id,
        private_name=name or 'check pool',
        reward_per_assignment=check_params.assignment_price,
        task_duration_hint=check_params.task_duration_hint,
        real_tasks_count=check_params.real_tasks_count,
        control_tasks_count=check_params.control_tasks_count,
        overlap=check_params.overlap.min_overlap,
        control_params=check_params.control,
        worker_filter=check_params.worker_filter,
        training_requirement=check_training_requirement,
    )

    markup_pool_cfg = pool_config.MarkupConfig(
        project_id=markup_prj.id,
        private_name=name or 'markup pool',
        reward_per_assignment=params.assignment_price,
        task_duration_hint=params.task_duration_hint,
        real_tasks_count=params.real_tasks_count,
        worker_filter=params.worker_filter,
        training_requirement=markup_training_requirement,
        control_params=params.control,
        first_attempt_by_model_worker=params.model is not None,
    )
    markup_pool, check_pool = get_annotation_pools(
        client, name, fb_loop, check_pool_cfg, markup_pool_cfg, control_objects
    )
    interrupter.add_pool_id(markup_pool.id)
    interrupter.add_pool_id(check_pool.id)

    plotter = None
    if interactive:
        plotter = metrics.AnnotationMetricsPlotter(
            toloka_client=client,
            stop_event=interrupter.interrupted,
            task_spec=task_spec,
            check_pool_id=check_pool.id,
            markup_pool_id=markup_pool.id,
            check_task_duration_hint=check_params.task_duration_hint,
            markup_task_duration_hint=params.task_duration_hint,
            evaluation=fb_loop.evaluation,
        )

    try:
        logger.info('annotation has started')
        fb_loop.loop(markup_pool.id, check_pool.id)
    except KeyboardInterrupt:
        interrupter.shutdown()
        return [], None
    finally:
        interrupter.interrupted.set()
        if plotter:
            plotter.join()

    return fb_loop.get_results(markup_pool.id, check_pool.id)
