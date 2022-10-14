from dataclasses import dataclass, field
import difflib
import json
import logging
from typing import Tuple, Optional

from bs4 import BeautifulSoup
import toloka.client as toloka

from .. import base, experts, mapping, instruction, project

from .utils import ask
from ..base import TaskSpec

logger = logging.getLogger(__name__)


@dataclass
class PreparedTaskSpec:
    task_spec: TaskSpec
    lang: str
    scenario: project.Scenario = project.Scenario.DEFAULT

    view: toloka.project.view_spec.ViewSpec = field(init=False)
    task_mapping: mapping.TaskMapping = field(init=False)
    dumped_view: str = field(init=False)

    def __post_init__(self):
        if isinstance(self, AnnotationTaskSpec):
            builder = project.AnnotationBuilder
        else:
            builder = {
                base.ClassificationFunction: project.ClassificationBuilder,
                base.SbSFunction: project.SbSBuilder,
                base.AnnotationFunction: project.AnnotationCheckBuilder,
            }[type(self.function)]

        self.view, self.task_mapping = builder(task_function=self.function, lang=self.lang).get_scenario(
            self.scenario, self.for_preview()
        )
        self.dump_view()

    def dump_view(self):
        self.dumped_view = json.dumps(json.loads(self.view.unstructure()['config']), ensure_ascii=False)

    @property
    def id(self) -> str:
        return self.task_spec.id

    @property
    def function(self) -> base.TaskFunction:
        return self.task_spec.function

    @property
    def name(self) -> base.LocalizedString:
        if self.scenario == project.Scenario.DEFAULT:
            return self.task_spec.name
        return self.task_spec.name + ' (' + self.scenario.project_name_suffix + ')'

    @property
    def description(self) -> base.LocalizedString:
        return self.task_spec.description

    @property
    def instruction(self) -> base.LocalizedString:
        return self.task_spec.instruction

    def log_message(self) -> str:
        scenario = '' if self.scenario == project.Scenario.DEFAULT else f' to {self.scenario.name}'
        return f'task "{self.task_spec.id}" in {self.lang}{scenario}'

    def for_preview(self) -> bool:
        return False

    def overload_view(self, view: toloka.project.view_spec.ViewSpec):
        self.view = view
        self.dump_view()


@dataclass
class PreviewTaskSpec(PreparedTaskSpec):
    def for_preview(self) -> bool:
        return True


@dataclass
class AnnotationTaskSpec(PreparedTaskSpec):
    check: PreparedTaskSpec = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        check_spec = TaskSpec(
            id=f'{self.task_spec.id}_check',
            function=self.task_spec.function,
            name=self.task_spec.name + ' – ' + project.CHECK,
            description=self.description + ' – ' + project.CHECK,
            instruction=self.instruction,
        )
        self.check = PreparedTaskSpec(check_spec, self.lang, self.scenario)


@dataclass
class AnnotationPreviewTaskSpec(PreviewTaskSpec, AnnotationTaskSpec):
    def __post_init__(self):
        super().__post_init__()
        # we don't use it for previews directly, but we need transformed task mapping in check spec here
        self.check = PreviewTaskSpec(self.check.task_spec, self.lang, self.scenario)


# Toloka localized projects are not suitable for us, because:
# - in task view, only labels can be localized in normal way without if/else conditions, i.e. we can't change output
#   validation depends on language for example, see
#   https://toloka.ai/ru/docs/guide/concepts/project-languages.html#project-languages__interface-translate.
# - Worker can choose multiple languages, on which he can perform tasks, but Toloka chooses instruction language
#   depends on worker language in settings, not language in pool filters. For tasks with language-specific
#   instructions it can cause problems.
def get_task_id(task_spec: PreparedTaskSpec):
    if task_spec.scenario == project.Scenario.DEFAULT:
        id = task_spec.id
    else:
        id = f'{task_spec.id}_{task_spec.scenario.value}'
    return f'{id}_{task_spec.lang}'


def _log_found_project(project_id: str, task_spec: PreparedTaskSpec):
    logger.debug(f'suitable Toloka project {project_id} is found for {task_spec.log_message()}')


def define_task(task_spec: PreparedTaskSpec, client: toloka.TolokaClient, interactive: bool = True):
    if task_spec.scenario == project.Scenario.DEFAULT and isinstance(task_spec, AnnotationTaskSpec):
        define_task(task_spec.check, client, interactive)

    found_project = find_project(task_spec, client)
    if found_project is None:
        prj = toloka.Project(private_comment=get_task_id(task_spec))
    else:
        prj, diff = found_project
        if not diff:
            _log_found_project(prj.id, task_spec)
            logger.info('no changes in task')
            return
        if interactive and not ask(f'{diff}update Toloka project {prj.id} according to the changes shown above?'):
            logger.info('task update is canceled')
            return

    task_spec.task_mapping.validate()

    prj.public_name = task_spec.name[task_spec.lang]
    prj.public_description = task_spec.description[task_spec.lang]
    prj.public_instructions = get_instruction(task_spec)
    prj.task_spec = toloka.project.task_spec.TaskSpec(
        input_spec=task_spec.task_mapping.to_toloka_input_spec(),
        output_spec=task_spec.task_mapping.to_toloka_output_spec(),
        view_spec=task_spec.view,
    )

    if found_project is None:
        logger.debug(f'creating Toloka project for {task_spec.log_message()}')
        client.create_project(prj)
        logger.info('task is defined')
    else:
        logger.debug(f'updating Toloka project {prj.id} for {task_spec.log_message()}')
        client.update_project(prj.id, prj)
        logger.info('task is updated')
        if interactive:
            notify_workers_about_task_change(task_spec, prj, client)


def find_project(
    task_spec: PreparedTaskSpec,
    client: toloka.TolokaClient,
) -> Optional[Tuple[toloka.Project, str]]:
    exists_msg = f'Toloka project is exists for {task_spec.log_message()}'

    for prj in client.get_projects(status='ACTIVE'):
        if not prj.private_comment == get_task_id(task_spec):
            continue
        if not mapping.check_project_is_suitable(prj, task_spec.task_mapping):
            raise ValueError(
                f'{exists_msg}, but function of task is changed in incompatible way. Use different task ID'
            )
        diff = get_project_diff(prj, task_spec)
        diff_msg = f'{exists_msg} and differs from current task spec:\n\n{diff}' if diff else ''
        return prj, diff_msg
    return None


def get_project_diff(prj: toloka.Project, task_spec: PreparedTaskSpec) -> str:
    assert prj.private_comment == get_task_id(task_spec)
    diffs = []
    for current_value, existing_value, value_display, value_name in (
        (task_spec.name[task_spec.lang], prj.public_name, None, 'name'),
        (task_spec.description[task_spec.lang], prj.public_description, None, 'description'),
        (get_instruction(task_spec), prettify_html(prj.public_instructions), None, 'instruction'),
        (
            task_spec.view.config.to_json(pretty=True),
            prj.task_spec.view_spec.config.to_json(pretty=True),
            lambda config: config.to_json(pretty=True),
            'view',
        ),
    ):
        if current_value != existing_value:
            diffs.append(f'{value_name} changed:\n\n{string_diff(existing_value, current_value)}\n\n')
    return '\n'.join(diffs)


def check_project(task_spec: PreparedTaskSpec, client: toloka.TolokaClient) -> toloka.Project:
    found_project = find_project(task_spec, client)
    if found_project is None:
        raise RuntimeError(f'task "{task_spec.id}" is not defined')
    prj, diff = found_project
    if diff:
        raise RuntimeError(diff)
    _log_found_project(prj.id, task_spec)
    return prj


# Toloka supports not all HTML tags and also changes HTML while creating/updating project, using escaping and some
# strange formatting. So we try so compare prettified versions of current and Toloka project instructions. It may break
# if Toloka begins to preprocess HTML in way that our prettifier could not format instructions in the same way. In such
# situation, we will have to put current instruction or its hash to some field in Toloka project, i.e. to private
# comment or metadata, and do not compare with instruction directly.
def prettify_html(html: str) -> str:
    return BeautifulSoup(html, 'html.parser').prettify()


def string_diff(s1: str, s2: str) -> str:
    diff = difflib.unified_diff(s1.splitlines(), s2.splitlines(), lineterm='')
    return '\n'.join(diff_line.rstrip() for diff_line in diff)


def get_instruction(task_spec: PreparedTaskSpec) -> str:
    lang = task_spec.lang
    worker = '<div>' + task_spec.instruction[lang] + '</div>'
    acceptance = instruction.acceptance[lang]

    if isinstance(task_spec.function, base.AnnotationFunction) and not isinstance(task_spec, AnnotationTaskSpec):
        worker = '<div>' + instruction.annotation_check_cut[lang] + worker + '</div>'

    if task_spec.scenario == project.Scenario.DEFAULT:
        return prettify_html(instruction.css + worker + acceptance)

    worker_header, expert_cut = instruction.worker_header[lang], instruction.expert_cut[lang]

    has_evaluation = False
    if isinstance(task_spec.function, base.AnnotationFunction):
        has_evaluation = task_spec.scenario == project.Scenario.EXPERT_LABELING_OF_TASKS

    expert = instruction.get_formatted_expert_instruction(task_spec.function, lang, has_evaluation)

    return prettify_html(instruction.css + worker_header + worker + '<div>' + expert_cut + expert + '</div>')


def notify_workers_about_task_change(task_spec: PreparedTaskSpec, prj: toloka.Project, client: toloka.TolokaClient):
    recipients_filter, recipients_msg = define_notification_recipients(task_spec, prj, client)
    if recipients_filter is None:
        return

    if not ask(f'notify workers of changes in the task? ({recipients_msg})'):
        return

    # If the name of the task has changed, the topic will contain a new name, which may confuse the workers.
    # In this case, we recommend writing in the message about the name change and specify the old name.
    topic = (
        base.LocalizedString(
            {
                'EN': 'Changes in task',
                'RU': 'Изменения в задании',
                'TR': 'Görevlerdeki değişiklikler',
                'KK': 'Тапсырмалардағы өзгерістер',
            }
        )
        + ' "'
        + task_spec.name
        + '"'
    )[task_spec.lang]

    message_lang = f'in {task_spec.lang}'
    if task_spec.lang != base.DEFAULT_LANG:
        message_lang += f' or {base.DEFAULT_LANG}'
    message = input(f'specify message for workers ({message_lang}): ')

    send_message_to_workers(topic, message, task_spec.lang, recipients_filter, client)

    logger.info('workers are notified')


def define_notification_recipients(
    task_spec: PreparedTaskSpec,
    prj: toloka.Project,
    client: toloka.TolokaClient,
) -> Tuple[Optional[toloka.filter.FilterCondition], str]:
    if task_spec.scenario != project.Scenario.DEFAULT:
        skills = experts.get_skills(task_spec.id, task_spec.lang, client)
        if len(skills) == 0:
            logger.info('no registered experts to receive notification')
            return None, ''
        worker_filters = [
            toloka.filter.Skill(key=skill.id, operator=toloka.primitives.operators.CompareOperator.GTE, value=0.0)
            for _, skill in skills
        ]
        recipients_msg = (
            f'all experts who registered for task "{task_spec.id}" in {task_spec.lang} language '
            f'will receive a notification'
        )
    else:
        worker_filters = [toloka.filter.Languages.in_(task_spec.lang)]
        training_requirement = experts.find_training(prj.id, client)
        recipients_msg = (
            f'all {task_spec.lang} workers who have ever performed tasks associated with your Toloka account '
            f'will receive a notification'
        )
        if training_requirement:
            skill_id = experts.get_skill_id_from_training(client.get_pool(training_requirement.id))
            # user skill for training is deleted after retry_training_after_days
            worker_filters.append(
                toloka.filter.Skill(key=skill_id, operator=toloka.primitives.operators.CompareOperator.GTE, value=0.0)
            )
            recipients_msg = (
                f'all workers who have performed the task "{task_spec.id}" in {task_spec.lang} language within '
                f'the last {training_requirement.retry_training_after_days} days will receive a notification'
            )
    return toloka.filter.FilterAnd(worker_filters), recipients_msg


def send_message_to_workers(
    topic: str, message: str, lang: str, recipients_filter: toloka.filter.FilterCondition, client: toloka.TolokaClient
):
    try:
        logger.debug(f'sending message\n\ttopic: {topic}\n\ttext: {message}\n\trecipients filter: {recipients_filter}')
        client.compose_message_thread(
            topic={lang: topic},
            text={lang: message},
            recipients_select_type=toloka.message_thread.RecipientsSelectType.FILTER,
            recipients_filter=recipients_filter,
            answerable=False,
        )
    except toloka.exceptions.IncorrectActionsApiError as e:
        if e.code == 'INCORRECT_RECIPIENTS':
            logger.warn('no recipients for the notification')
        else:
            raise
