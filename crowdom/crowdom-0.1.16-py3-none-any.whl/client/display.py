from dataclasses import dataclass
from enum import Enum
import math
import json
from typing import List, Optional, Type, Tuple, ClassVar, Dict, Union

import numpy as np
import pandas as pd

from .. import (
    base,
    classification,
    classification_loop,
    contrib,
    evaluation,
    feedback_loop,
    mapping,
    objects,
    pricing,
    project,
)

from .task import PreparedTaskSpec, AnnotationTaskSpec, PreviewTaskSpec, AnnotationPreviewTaskSpec
from ..base import TaskSpec
from ..worker import NoWorker
from ..utils import DecimalEncoder


def get_pool_price(
    input_objects_count: int,
    config: pricing.PoolPricingConfig,
    overlap: classification_loop.Overlap,
    display_formula: bool = False,
) -> str:
    formula = PoolPriceFormula(input_objects_count, config, overlap)
    if display_formula:
        from IPython.display import display, Math

        print('clear formula, which does not account edge cases like min commission and incomplete assignments')
        display(Math(formula.clear_formula()))  # noqa
        print('\nmore precise formula, which accounts more edge cases')
        display(Math(formula.precise_formula()))  # noqa
    return formula.total_price_precise_raw_str


def get_annotation_price(
    input_objects_count: int,
    markup_config: pricing.PoolPricingConfig,
    check_config: pricing.PoolPricingConfig,
    markup_overlap: classification_loop.DynamicOverlap,
    check_overlap: classification_loop.Overlap,
    assignment_check_sample: Optional[evaluation.AssignmentCheckSample],
    display_formula: bool = False,
) -> str:
    formula = AnnotationPriceFormula(
        input_objects_count=input_objects_count,
        markup_config=markup_config,
        check_config=check_config,
        markup_overlap=markup_overlap,
        check_overlap=check_overlap,
        assignment_check_sample=assignment_check_sample,
    )
    if display_formula:
        from IPython.display import display, Math

        print('some edge cases may be not fully accounted')
        display(*(Math(f) for f in formula.clear_formula()))
    return formula.total_price_simple_raw_str


def get_spec_cls(task_function: base.TaskFunction, for_preview: bool = False) -> Type[PreparedTaskSpec]:
    if type(task_function) in [base.ClassificationFunction, base.SbSFunction]:
        return PreviewTaskSpec if for_preview else PreparedTaskSpec
    elif isinstance(task_function, base.AnnotationFunction):
        return AnnotationPreviewTaskSpec if for_preview else AnnotationTaskSpec
    else:
        raise ValueError(f'Unknown task function: {task_function}')


def get_spec_cls_by_task_spec(task_spec: PreparedTaskSpec) -> Type[PreparedTaskSpec]:
    if isinstance(task_spec, AnnotationTaskSpec):
        return AnnotationPreviewTaskSpec
    return PreviewTaskSpec


# current formula is not 100% precise:
# - it does not know about custom toloka commission
# - it rounds total price by cents, but is seems that Toloka using ceil() for it
# also, we have two variants of formulas
# - clear one, which does not account case than assignment price is such that commission is greater than default
#   because of min commission, and also incomplete last assignment
# - precise but complex one, which accounts min commission
@dataclass
class PoolPriceFormula:
    input_objects_count: int
    config: pricing.PoolPricingConfig
    overlap: classification_loop.Overlap

    def __post_init__(self):
        min_overlap = self.overlap.min_overlap
        self.has_price_range = isinstance(self.overlap, classification_loop.DynamicOverlap)
        max_overlap = self.overlap.max_overlap if self.has_price_range else min_overlap

        self.task_price = self.config.assignment_price / self.config.real_tasks_count

        base_price_clear = self.input_objects_count * self.task_price * (1 + pricing.toloka_commission)

        self.min_total_price_clear = base_price_clear * min_overlap
        self.max_total_price_clear = base_price_clear * max_overlap

        self.assignments_count = math.ceil(self.input_objects_count / self.config.real_tasks_count)
        self.assignments_price = self.config.assignment_price + max(
            self.config.assignment_price * pricing.toloka_commission, pricing.min_toloka_commission
        )

        base_price_precise = self.assignments_count * self.assignments_price
        self.min_total_price_precise = base_price_precise * min_overlap
        self.max_total_price_precise = base_price_precise * max_overlap

        self.overlap_str = f'{self.overlap.min_overlap}'
        self.overlap_explanation_str = 'Overlap'
        self.total_price_simple_str = fr'{self.min_total_price_clear:.2f}\$'
        self.total_price_precise_str = fr'{self.min_total_price_precise:.2f}\$'
        self.total_price_precise_raw_str = f'{self.min_total_price_precise:.2f}$'

        if self.has_price_range:
            self.overlap_str = fr'[{self.overlap_str} \dots {self.overlap.max_overlap}]'
            self.overlap_explanation_str = r'[MinOverlap \dots MaxOverlap]'
            self.total_price_simple_str = fr'{self.total_price_simple_str} \dots {self.max_total_price_clear:.2f}\$'
            self.total_price_precise_str = fr'{self.total_price_precise_str} \dots {self.max_total_price_precise:.2f}\$'
            self.total_price_precise_raw_str = (
                f'{self.total_price_precise_raw_str} ... {self.max_total_price_precise:.2f}$'
            )

    def clear_formula(self) -> str:
        return (
            r'TotalPrice_{clear} = TaskCount * PricePerTask_\$ * '
            fr'{self.overlap_explanation_str} * (1 + TolokaCommission) = '
            fr'{self.input_objects_count} * {self.task_price:.4f}\$ * {self.overlap_str} * '
            fr'{1 + pricing.toloka_commission} = {self.total_price_simple_str}.'
        )

    def precise_formula(self) -> str:
        return (
            r'TotalPrice_{precise} = AssignmentCount * PricePerAssignment_\$ * '
            fr'{self.overlap_explanation_str} = \left \lceil \frac {{TaskCount}} {{TasksOnAssignment}} \right \rceil * '
            r'(PricePerAssignment_\$ + max(PricePerAssignment_\$ * TolokaCommission, MinTolokaCommission_\$) '
            fr'* {self.overlap_explanation_str} = \lceil {self.input_objects_count} / '
            fr'{self.config.real_tasks_count} \rceil * '
            fr'({self.config.assignment_price}\$ + max({self.config.assignment_price}\$ * '
            fr'{pricing.toloka_commission}, {pricing.min_toloka_commission}\$) * {self.overlap_str} = '
            fr'{self.assignments_count} * {self.assignments_price:.3f} * {self.overlap_str} = '
            fr'{self.total_price_precise_str}.'
        )


@dataclass
class AnnotationPriceFormula:
    input_objects_count: int
    markup_config: pricing.PoolPricingConfig
    check_config: pricing.PoolPricingConfig

    markup_overlap: classification_loop.DynamicOverlap
    check_overlap: classification_loop.Overlap

    assignment_check_sample: Optional[evaluation.AssignmentCheckSample]

    def __post_init__(self):
        min_markup_overlap = self.markup_overlap.min_overlap
        max_markup_overlap = self.markup_overlap.max_overlap

        min_check_overlap = self.check_overlap.min_overlap
        self.has_check_price_range = isinstance(self.check_overlap, classification_loop.DynamicOverlap)
        max_check_overlap = self.check_overlap.max_overlap if self.has_check_price_range else min_check_overlap

        self.markup_task_price = self.markup_config.assignment_price / self.markup_config.real_tasks_count
        self.check_task_price = self.check_config.assignment_price / self.check_config.real_tasks_count

        self.check_overlap_str = f'{self.check_overlap.min_overlap}'
        self.markup_overlap_str = fr'[{self.markup_overlap.min_overlap} \dots {self.markup_overlap.max_overlap}]'
        self.markup_overlap_explanation_str = r'[MinMarkupOverlap \dots MaxMarkupOverlap]'
        self.check_overlap_explanation_str = 'CheckOverlap'

        self.check_tasks_count_str = (
            fr'[{self.input_objects_count * min_markup_overlap} \dots {self.input_objects_count * max_markup_overlap}]'
        )
        self.check_tasks_count_explanation_str = (
            f'MarkupTaskCount * {self.markup_overlap_explanation_str} = '
            f'{self.input_objects_count} * {self.markup_overlap_str}'
        )

        sample_frac = 1.0
        if self.assignment_check_sample is not None:
            assert self.assignment_check_sample.max_tasks_to_check is not None
            sample_frac = self.assignment_check_sample.max_tasks_to_check / self.markup_config.real_tasks_count

            self.check_tasks_count_str = (
                fr'[{math.ceil(self.input_objects_count * min_markup_overlap * sample_frac)} \dots '
                f'{math.ceil(self.input_objects_count * max_markup_overlap * sample_frac)}]'
            )
            self.check_tasks_count_explanation_str = (
                r'MarkupTaskCount * \frac {CheckSampleTaskCount} {MarkupTasksPerAssignment} * '
                fr'{self.markup_overlap_explanation_str} = {self.input_objects_count} * \frac '
                f'{{{self.assignment_check_sample.max_tasks_to_check}}} {{{self.markup_config.real_tasks_count}}} * '
                f'{self.markup_overlap_str}'
            )

        self.check_comission = pricing.toloka_commission

        if self.check_config.assignment_price * pricing.toloka_commission < pricing.min_toloka_commission:
            self.check_comission = pricing.min_toloka_commission / self.check_config.assignment_price

        self.markup_comission = pricing.toloka_commission

        if self.markup_config.assignment_price * pricing.toloka_commission < pricing.min_toloka_commission:
            self.markup_comission = pricing.min_toloka_commission / self.markup_config.assignment_price

        self.check_comission_explanation_str = (
            r'max \left( TolokaCommission, \frac {MinTolokaCommission} {PricePerCheckAssignment} \right) = '
            fr'max \left( {pricing.toloka_commission}, \frac {{{pricing.min_toloka_commission}}}'
            fr'{{{self.check_config.assignment_price}}} \right)'
        )
        self.markup_comission_explanation_str = (
            r'max \left( TolokaCommission, \frac {MinTolokaCommission} {PricePerMarkupAssignment} \right) = '
            fr'max \left( {pricing.toloka_commission}, \frac {{{pricing.min_toloka_commission}}}'
            fr'{{{self.markup_config.assignment_price}}} \right)'
        )

        base_markup_price_clear = self.input_objects_count * self.markup_task_price * (1 + self.markup_comission)
        # todo: sample происходит из целого assignment'а, могут быть краевые эффекты - не абсолютно точная формула
        base_check_price_clear = (
            math.ceil(self.input_objects_count * sample_frac) * self.check_task_price * (1 + self.check_comission)
        )
        self.min_markup_price = base_markup_price_clear * min_markup_overlap
        self.max_markup_price = base_markup_price_clear * max_markup_overlap
        self.min_check_price = base_check_price_clear * min_check_overlap * min_markup_overlap
        self.max_check_price = base_check_price_clear * max_check_overlap * max_markup_overlap
        self.min_total_price_clear = self.min_markup_price + self.min_check_price
        self.max_total_price_clear = self.max_markup_price + self.max_check_price

        self.check_price_str = fr'{self.min_check_price:.2f}\$ \dots {self.max_check_price:.2f}\$'
        self.markup_price_str = fr'{self.min_markup_price:.2f}\$ \dots {self.max_markup_price:.2f}\$'
        self.total_price_simple_str = fr'{self.min_total_price_clear:.2f}\$ \dots {self.max_total_price_clear:.2f}\$'
        self.total_price_simple_raw_str = f'{self.min_total_price_clear:.2f}$ ... {self.max_total_price_clear:.2f}$'
        if self.has_check_price_range:
            self.check_overlap_str = fr'[{self.check_overlap_str} \dots {self.check_overlap.max_overlap}]'
            self.check_overlap_explanation_str = r'[MinCheckOverlap \dots MaxCheckOverlap]'

    def clear_formula(self) -> Tuple[str, ...]:
        return (
            f'MarkupTolokaComission = {self.markup_comission_explanation_str} = {self.markup_comission};',
            fr'MarkupPrice = MarkupTaskCount * PricePerMarkupTask_\$ * '
            fr'{self.markup_overlap_explanation_str} * (1 + MarkupTolokaComission) = '
            fr'{self.input_objects_count} * {self.markup_task_price:.4f}\$ * {self.markup_overlap_str} * '
            fr'{1 + self.markup_comission} = {self.markup_price_str};',
            f'CheckTaskCount = {self.check_tasks_count_explanation_str} = {self.check_tasks_count_str};',
            f'CheckTolokaComission = {self.check_comission_explanation_str} = {self.check_comission};',
            r'CheckPrice = CheckTaskCount * PricePerCheckTask_\$ * '
            fr'{self.check_overlap_explanation_str} * (1 + CheckTolokaComission) = '
            fr'{self.check_tasks_count_str} * {self.check_task_price:.4f}\$ * {self.check_overlap_str} * '
            fr'{1 + self.check_comission} = {self.check_price_str};',
            r'TotalPrice = MarkupPrice + CheckPrice = '
            fr'{self.markup_price_str} + {self.check_price_str} = {self.total_price_simple_str}.',
        )


# template builder saves config and input fields in encoded way to URL, but it doesn't save output fields and state of
# UI, so we can create preview just for task (without solution), and there will be unnecessary config block
class TaskPreview:
    def __init__(
        self,
        input_objects: mapping.Objects,
        *,
        task_spec: Optional[PreparedTaskSpec] = None,
        task_function: Optional[base.TaskFunction] = None,
        lang: Optional[str] = None,
        output_objects: Optional[mapping.Objects] = None,
    ):
        assert (
            task_spec is not None or task_function is not None and lang is not None
        ), 'Provide either task_spec or both task_function and language'
        for_preview = output_objects is not None
        if task_spec is None:
            task_spec = get_spec_cls(task_function, for_preview)(
                task_spec=TaskSpec(
                    id=None,
                    function=task_function,
                    name=base.EMPTY_STRING,
                    description=base.EMPTY_STRING,
                    instruction=None,
                ),
                lang=lang,
            )
        elif for_preview:
            task_spec = get_spec_cls_by_task_spec(task_spec)(
                task_spec=task_spec.task_spec,
                lang=task_spec.lang,
                scenario=task_spec.scenario,
            )
        self.url = self.get_url(input_objects, task_spec, output_objects)

    def get_link(self) -> str:
        return f'<a href="{self.url}" target="_blank" rel="noopener noreferrer">task preview</a>'

    def display_link(self):
        from IPython.display import HTML

        return HTML(self.get_link())

    def display(self):
        from IPython.display import HTML

        return HTML(
            f'<iframe src="{self.url}" onload="javascript:(function(o)'
            '{o.style.height=o.contentWindow.document.body.scrollHeight+"px";}(this));" '
            'style="height:800px;width:100%;border:none;overflow:hidden;"/>'
        )

    @classmethod
    def get_url(
        cls,
        input_objects: mapping.Objects,
        task_spec: PreparedTaskSpec,
        output_objects: Optional[mapping.Objects] = None,
    ) -> str:
        objects_count = len(input_objects)
        if output_objects is not None:
            # for results preview we display output types as inputs, due to tb limitations
            objects_count += len(output_objects)

        if isinstance(task_spec, AnnotationTaskSpec):
            if objects_count == len(task_spec.check.task_mapping.input_mapping):
                task_spec = task_spec.check
            else:
                assert objects_count == len(
                    task_spec.task_mapping.input_mapping
                ), 'incorrect number of input objects supplied'
        config, task_mapping = task_spec.dumped_view, task_spec.task_mapping
        preview_objects = input_objects
        if output_objects is not None:
            preview_objects = np.concatenate([input_objects, output_objects])
        input_values: dict = task_mapping.to_task(preview_objects).input_values

        dumped = json.dumps(
            {'config': config, 'input': json.dumps(input_values, ensure_ascii=False, cls=DecimalEncoder)},
            ensure_ascii=False,
        )
        compressed = contrib.LZString.compressToEncodedURIComponent(dumped)
        return f'https://tb.yandex.net/editor?config={compressed}'


class Results:
    row_input_objects: np.ndarray
    row_output_objects: np.ndarray

    task_spec: PreparedTaskSpec

    WORKER_FIELD: ClassVar[str] = 'worker'
    PREVIEW_FIELD: ClassVar[str] = 'preview'

    def _add_task_previews(self, df: pd.DataFrame) -> pd.DataFrame:
        urls = [
            TaskPreview(task_input_objects, output_objects=task_output_objects, task_spec=self.task_spec).get_link()
            for task_input_objects, task_output_objects in zip(
                self.row_input_objects[df.index], self.row_output_objects[df.index]
            )
        ]
        df_copy = df.copy()
        df_copy[self.PREVIEW_FIELD] = urls
        return df_copy

    def html_with_task_previews(self, df: pd.DataFrame):
        from IPython.display import HTML

        return HTML(self._add_task_previews(df).to_html(escape=False))

    @staticmethod
    def deduplicate(df: pd.DataFrame) -> pd.DataFrame:
        return df.loc[df.astype(str).drop_duplicates().index]


class LabelingResults(Results):
    df: pd.DataFrame
    has_worker_weights: bool
    RESULT_FIELD: ClassVar[str] = 'result'
    CONFIDENCE_FIELD: ClassVar[str] = 'confidence'


class ClassificationResults(LabelingResults):
    WORKER_WEIGHT_FIELD: ClassVar[str] = 'worker_weight'
    LABEL_FIELD: ClassVar[str] = 'label'
    OVERLAP_FIELD: ClassVar[str] = 'overlap'

    def __init__(
        self,
        input_objects: List[mapping.Objects],
        results: List[Tuple[classification.TaskLabelsProbas, List[classification.WorkerLabel]]],
        task_spec: PreparedTaskSpec,
        worker_weights: Optional[Dict[str, float]] = None,
    ):
        self.task_spec = task_spec

        # we will index these input objects by dataframe row indexes
        row_input_objects, row_output_objects = [], []

        input_fields = []
        for obj_mapping in task_spec.task_mapping.input_mapping:
            for _, task_field in obj_mapping.obj_task_fields:
                input_fields.append(task_field)

        self.input_fields = input_fields

        cls_type: Type[base.Class] = task_spec.task_mapping.output_mapping[0].obj_meta.type
        cls_fields = [(cls, f'proba_{cls.value}') for cls in cls_type.possible_instances()]

        self.proba_fields = [cls_field for _, cls_field in cls_fields]
        self.has_worker_weights = worker_weights is not None
        rows = []
        for task_input_objects, result in zip(input_objects, results):
            task_row = task_spec.task_mapping.toloka_values(task_input_objects)
            del task_row[mapping.TASK_ID_FIELD]

            labels_probas, raw_labels = result
            overlap = len(raw_labels)

            most_probable_result = classification.get_most_probable_label(labels_probas)
            if most_probable_result is not None:
                result, proba = most_probable_result
            else:
                assert labels_probas is None
                assert not raw_labels

                # todo: maybe confidence should also be None
                result, proba, labels_probas = None, 0.0, {}
                raw_labels = [(None, NoWorker())]
                if self.has_worker_weights:
                    worker_weights[None] = 0.0

            task_row[self.RESULT_FIELD] = np.nan if result is None else result.value
            task_row[self.CONFIDENCE_FIELD] = proba
            task_row[self.OVERLAP_FIELD] = overlap
            for cls, cls_field in cls_fields:
                proba = labels_probas.get(cls, 0.0)
                task_row[cls_field] = proba

            for raw_label, worker in raw_labels:
                worker_row = dict(task_row)
                worker_row[self.LABEL_FIELD] = np.nan if raw_label is None else raw_label.value
                worker_row[self.WORKER_FIELD] = worker.id
                if self.has_worker_weights:
                    worker_row[self.WORKER_WEIGHT_FIELD] = worker_weights[worker.id]
                rows.append(worker_row)
                row_input_objects.append(task_input_objects)
                row_output_objects.append((raw_label,))

        self.df = pd.DataFrame.from_dict(rows)
        self.row_input_objects = np.array(row_input_objects)
        self.row_output_objects = np.array(row_output_objects)

    def predict(self) -> pd.DataFrame:
        return self.deduplicate(
            self.df[self.input_fields + [self.RESULT_FIELD, self.CONFIDENCE_FIELD, self.OVERLAP_FIELD]]
        )

    def predict_proba(self) -> pd.DataFrame:
        return self.deduplicate(self.df[self.input_fields + self.proba_fields + [self.OVERLAP_FIELD]])

    def worker_labels(self) -> pd.DataFrame:
        worker_labels = self.df[
            self.input_fields
            + [self.LABEL_FIELD, self.WORKER_FIELD]
            + ([self.WORKER_WEIGHT_FIELD] if self.has_worker_weights else [])
        ]
        return worker_labels[worker_labels[self.WORKER_FIELD].notnull()]


class AnnotationResults(LabelingResults):
    EVAL_FIELD: ClassVar[str] = base.EVALUATION_TASK_FIELD
    ANNOTATION_WORKER_FIELD: ClassVar[str] = 'annotator'
    CHECK_WORKER_FIELD: ClassVar[str] = 'evaluator'
    WORKER_WEIGHT_FIELD: ClassVar[str] = 'evaluator_weight'
    CHECK_OVERLAP_FIELD: ClassVar[str] = 'evaluation_overlap'
    ANNOTATION_OVERLAP_FIELD: ClassVar[str] = 'annotation_overlap'

    def __init__(
        self,
        results: List[feedback_loop.TaskResult],
        task_spec: AnnotationTaskSpec,
        worker_weights: Optional[Dict[str, float]] = None,
    ):
        self.task_spec = task_spec

        row_input_objects, row_output_objects = [], []

        input_fields = []
        for obj_mapping in task_spec.task_mapping.input_mapping:
            for _, task_field in obj_mapping.obj_task_fields:
                input_fields.append(task_field)

        self.input_fields = input_fields

        output_fields = []
        for obj_mapping in task_spec.task_mapping.output_mapping:
            for _, task_field in obj_mapping.obj_task_fields:
                output_fields.append(task_field)

        self.output_fields = output_fields

        self.has_worker_weights = worker_weights is not None

        rows = []
        for task_result in results:
            inputs = task_spec.task_mapping.toloka_values(task_result.task)

            del inputs[mapping.TASK_ID_FIELD]

            for i, solution in enumerate(task_result.solutions):
                outputs = task_spec.task_mapping.toloka_values(solution.solution, output=True)

                task_row = {**inputs, **outputs}
                task_row[self.ANNOTATION_WORKER_FIELD] = solution.worker.id

                task_row[self.RESULT_FIELD] = i == 0
                task_row[self.ANNOTATION_OVERLAP_FIELD] = len(task_result.solutions)
                if solution.evaluation is None:
                    task_row[self.CHECK_OVERLAP_FIELD] = 0
                    rows.append(task_row)
                    row_input_objects.append(task_result.task)
                    row_output_objects.append(solution.solution)
                else:
                    assert solution.evaluation.worker_labels
                    task_row[self.CONFIDENCE_FIELD] = solution.evaluation.confidence
                    task_row[self.CHECK_OVERLAP_FIELD] = len(solution.evaluation.worker_labels)
                    for choice, worker in solution.evaluation.worker_labels:
                        worker_row = dict(task_row)
                        worker_row[self.EVAL_FIELD] = choice.ok
                        worker_row[self.CHECK_WORKER_FIELD] = worker.id
                        if self.has_worker_weights:
                            worker_row[self.WORKER_WEIGHT_FIELD] = worker_weights[worker.id]
                        rows.append(worker_row)
                        row_input_objects.append(task_result.task)
                        row_output_objects.append(solution.solution)

        self.df = pd.DataFrame.from_dict(rows)
        self.row_input_objects = np.array(row_input_objects)
        self.row_output_objects = np.array(row_output_objects)

    def predict(self) -> pd.DataFrame:
        df = self.deduplicate(self.df[self.input_fields + self.output_fields + [self.RESULT_FIELD]])
        return df[df[self.RESULT_FIELD]].drop([self.RESULT_FIELD], axis=1)

    def predict_proba(self) -> pd.DataFrame:
        return self.deduplicate(self.df[self.input_fields + self.output_fields + [self.CONFIDENCE_FIELD]])

    def worker_labels(self) -> pd.DataFrame:
        return self.df.drop([self.RESULT_FIELD], axis=1)


class ExpertLabelingApplication(Enum):
    TRAINING = 'training'
    CONTROL_TASKS = 'control_tasks'
    ANNOTATION_CHECK_TRAINING = 'check_training'


class ExpertLabelingResults(Results):
    df: pd.DataFrame

    OK_FIELD: ClassVar[str] = '_ok'

    # todo implement this in ClassificationResults
    DURATION_FIELD: ClassVar[str] = 'duration'

    input_length: int
    output_lenght: int
    ok_index: int
    evaluation_index: Optional[int] = None
    comment_index: int
    output_names: List[str]

    def __init__(
        self,
        results: List[Tuple[Union[mapping.TaskSingleSolution, mapping.Objects], mapping.TaskMultipleSolutions]],
        task_spec: PreparedTaskSpec,
        worker_id_to_name: Optional[Dict[str, str]] = None,
    ):
        self.task_spec = task_spec
        if worker_id_to_name is None:
            worker_id_to_name = {}
        # we will index these input objects by dataframe row indexes
        row_input_objects, row_output_object = [], []

        rows = []
        for _, (input_objects, solution) in results:
            if not solution:
                # expert labeling was interrupted, and this task doesn't have a solution
                continue
            [(output_objects, assignment)] = solution
            task_row = {
                **task_spec.task_mapping.toloka_values(input_objects, output=False),
                **task_spec.task_mapping.toloka_values(output_objects, output=True),
            }
            del task_row[mapping.TASK_ID_FIELD]
            task_row[self.WORKER_FIELD] = worker_id_to_name.get(assignment.user_id, assignment.user_id)
            task_row[self.DURATION_FIELD] = (assignment.submitted - assignment.created) / len(assignment.tasks)
            rows.append(task_row)
            row_input_objects.append(input_objects)
            row_output_object.append(output_objects)
        self.rows = rows
        self.df = pd.DataFrame.from_dict(rows)
        self.row_input_objects = np.array(row_input_objects)
        self.row_output_objects = np.array(row_output_object)
        function = task_spec.function

        default_spec = get_spec_cls(function)(task_spec=self.task_spec.task_spec, lang=self.task_spec.lang)

        self.input_length = len(default_spec.task_mapping.input_mapping)
        self.output_length = len(default_spec.task_mapping.output_mapping)
        ok_meta, comment_meta = project.Builder.EXPERT_LABELING_METAS

        self.output_names = [
            task_mapping.obj_task_fields[0][1] for task_mapping in self.task_spec.task_mapping.output_mapping
        ]
        self.ok_index = self.output_names.index(ok_meta.name)
        self.comment_index = self.output_names.index(comment_meta.name)
        if isinstance(function, base.AnnotationFunction):
            evaluation_name = function.get_evaluation_named_meta().name
            if evaluation_name in self.output_names:
                self.evaluation_index = self.output_names.index(evaluation_name)

    def get_results(self) -> pd.DataFrame:
        return self.df

    def get_accuracy(self):
        return self.df[self.OK_FIELD].mean()

    def get_solved_task_and_comment(
        self,
        task: mapping.Objects,
        solution: mapping.Objects,
        application: ExpertLabelingApplication,
    ) -> Tuple[mapping.TaskSingleSolution, objects.Text]:
        objs = task + solution
        if self.evaluation_index is None or application == ExpertLabelingApplication.TRAINING:
            inputs, outputs, comment = (
                objs[: self.input_length],
                objs[self.input_length : self.input_length + self.output_length],
                solution[self.comment_index],
            )
        else:
            inputs, outputs, comment = (
                objs[: self.input_length + self.output_length],
                (solution[self.evaluation_index],),
                solution[self.comment_index],
            )
        return (inputs, outputs), comment

    def suitable(self, solution: mapping.Objects, application: ExpertLabelingApplication) -> bool:
        if not solution[self.ok_index].ok:
            return False
        if application == ExpertLabelingApplication.CONTROL_TASKS:
            return True
        if solution[self.comment_index] is None or not solution[self.comment_index].text:
            return False
        if application == ExpertLabelingApplication.ANNOTATION_CHECK_TRAINING:
            return True
        if self.evaluation_index is not None:
            return solution[self.evaluation_index].ok
        return True

    def get_correct_objects(
        self,
        application: ExpertLabelingApplication = ExpertLabelingApplication.CONTROL_TASKS,
    ) -> Tuple[List[mapping.TaskSingleSolution], List[objects.Text]]:
        tasks_and_solutions = [
            (self.task_spec.task_mapping.from_task_values(row), self.task_spec.task_mapping.from_solution_values(row))
            for row in self.rows
        ]
        generated_objects = [
            self.get_solved_task_and_comment(task, solution, application)
            for task, solution in tasks_and_solutions
            if self.suitable(solution, application)
        ]
        solutions = [solution for solution, _ in generated_objects]
        texts = [text for _, text in generated_objects]
        return solutions, texts
