"""
Pipeline module
"""
import logging
import pathlib
import sys

import yaml

from tcd_pipeline.rules import push as push_rule

logger = logging.getLogger()


def str_presenter(dumper, data):
    """String presenter

    This presenter will generate multiline string with |

    Examples:
    short: hello
    scripts: |
      line 1
      line 2

    """
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar(
          'tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)


def generate_workflows(pipeline_path: str, event: dict, output: str = None) -> None:
    """Generate workflows from pipeline files

    Parameters
    ----------
    pipeline_path : str
        Absolute path of pipeline file (*-pipeline.yaml)
        or directory contain pipeline files(*-pipeline.yaml)
    event : dict
        Git push event data

        {
          'refType': 'branch',
          'refName': 'main',
          'changes': [
            'Dockerfile,
            'src/main/java/**.java'
          ]
        }
    output : str
        Output generated worfklows file.
        Default is stdout.
    """

    # Checking path is exist
    path = pathlib.Path(pipeline_path)
    if not path.exists():
        raise ValueError(f"Path {path} does not exist.")

    # Collect list of pipeline files
    pipeline_files: list[str] = []
    if path.is_file():
        pipeline_files.append(path)
    elif path.is_dir():
        for file in list(path.glob("*-pipeline.yaml")):
            if file.is_file():
                pipeline_files.append(file)

    # Transform TCD pipeline to Argo workflows
    workflows: list[dict] = []
    for pipeline_file in pipeline_files:
        with open(pipeline_file, 'r', encoding="UTF-8") as stream:
            pipeline: dict = yaml.safe_load(stream)

            # Evaluate when push rules
            if evaluate_rules(pipeline=pipeline, event=event):
                workflows.append(
                  transform(pipeline)
                )

    # Generate workflow manifests
    if output is None:
        yaml.dump_all(workflows, sys.stdout)
    else:
        with open(output, "w", encoding="UTF-8") as outfile:
            yaml.dump_all(workflows, outfile)
            print("Workflow generated.", output)


def evaluate_rules(pipeline: dict, event: dict) -> bool:
    """Evaluate git event data with pipeline rule

    Rules to be evaluated
    - exact matching
    - semver matching
    - regex matching
    - glob matching

    Parameters
    ----------
    pipeline : dict
        Pipeline document
    event : dict
        Git event fact

        {
          'refType', 'branch',
          'refName', 'release/dev',
          'changes', [
            'Dockerfile',
            'src/main/java/Main.java'
          ]
        }

    Returns
    bool:
        Matched rule evaluation
    """

    rules = pipeline.get("when")

    # Return True if no rules specific
    if not rules:
        return True

    return push_rule.is_git_ref_match_exact(rules=rules, fact=event) \
        or push_rule.is_git_ref_match_glob(rules=rules, fact=event) \
        or push_rule.is_git_ref_match_semver(rules=rules, fact=event) \
        or push_rule.is_git_ref_match_regex(rules=rules, fact=event)


def transform(pipeline: dict) -> dict:
    """Transform TCD pipeline to Argo workflow

    Parameters
    ----------
    pipeline : dict
        Pipeline document

    Returns
    -------
    dict
        Argo workflow

    """
    builder = WorkflowBuilder(
      name=pipeline.get("name"),
      tasks=pipeline.get("tasks")
    )
    builder.add_templates(pipeline.get("templates"))
    return builder.build()


class WorkflowBuilder:
    """Building Argo workflow file

    Attributes
    ----------
    name : str
        Workflow name. {.metadata.generateName}
    labels : dict
        Workflow labels. {.metadata.labels}

    Methods
    -------
    add_label(key, value)
        Add label to workflow object.
    add_templates(templates)
        Add list of workflow template
    build()
        Build Argo workflow
    """
    workflow: dict
    labels: dict = {"tcd/workflow-type": "pipeline"}
    templates: list[dict]

    def __init__(self, name: str, tasks: list[dict]) -> None:
        """Initial workflow and entrypoint template

        Parameters
        ----------
        name : str
            Workflow name. {.metadata.generateName}
        tasks : list[dict]
            Main pipeline tasks. (Argo DAGTask)
            https://argoproj.github.io/argo-workflows/fields/#dagtask

        """
        self.templates = []
        self.workflow = yaml.safe_load(f"""
          apiVersion: argoproj.io/v1alpha1
          kind: Workflow
          metadata:
            generateName: {name}-
          spec:
            entrypoint: main-pipeline
            templates: []
          """)
        self.templates.append(
          {
            "name": "main-pipeline",
            "dag": {
              "tasks": tasks
            }
          }
        )

    def add_label(self, key: str, value: str) -> None:
        """Add workflow label

        Parameters
        ----------
        key : str
            Label key
        value : str
            Label value
        """
        self.labels[key] = value

    def add_templates(self, templates: list[dict]) -> None:
        """Add templates to workflow

        https://argoproj.github.io/argo-workflows/fields/#template

        Parameters
        ----------
        template : list[dict]
            Array of templates
        """
        self.templates.extend(templates)

    def build(self) -> dict:
        """Build workflow

        Returns
        -------
        dict
            Argo workflow
        """
        self.workflow['metadata']['labels'] = self.labels
        self.workflow['spec']['templates'] = self.templates

        return self.workflow
