import yaml
import logging
import requests
from io import StringIO
from collections import defaultdict
from argo.workflows.client import (ApiClient,
                                   WorkflowServiceApi,
                                   Configuration,
                                   V1alpha1WorkflowCreateRequest)
import plynx.base.resource
import plynx.base.executor
import plynx.db.node
import plynx.db.validation_error

from plynx.constants import NodeRunningStatus, ParameterTypes, ValidationTargetType, ValidationCode
from plynx.constants import NodeRunningStatus,  SpecialNodeId, Collections


class Connector(plynx.base.resource.BaseResource):
    pass


class Node(plynx.base.executor.BaseExecutor):
    IS_GRAPH = False

    def __init__(self, node=None):
        super(Node, self).__init__(node)

    def run(self):
        raise NotImplementedError()

    def status(self):
        raise NotImplementedError()

    def kill(self):
        raise NotImplementedError()

    @classmethod
    def get_default_node(cls, is_workflow):
        if is_workflow:
            raise Exception('This class cannot be a workflow')
        node = super().get_default_node(is_workflow)
        node.parameters.extend(
            [
                plynx.db.node.Parameter.from_dict({
                    'name': '_image',
                    'parameter_type': ParameterTypes.STR,
                    'value': 'alpine:3.7',
                    'mutable_type': False,
                    'publicable': True,
                    'removable': False
                }),
                plynx.db.node.Parameter.from_dict({
                    'name': '_command',
                    'parameter_type': ParameterTypes.STR,
                    'value': 'echo "hello world"',
                    'mutable_type': False,
                    'publicable': True,
                    'removable': False
                }),
            ]
        )
        """
        node.logs.extend(
            [
                Output.from_dict({
                    'name': 'stderr',
                    'file_type': FILE_KIND,
                }),
                Output({
                    'name': 'stdout',
                    'file_type': FILE_KIND,
                }),
                Output({
                    'name': 'worker',
                    'file_type': FILE_KIND,
                }),
            ]
        )
        """
        return node


class DAG(plynx.base.executor.BaseExecutor):
    """ Main graph scheduler.

    Args:
        node_dict (dict)

    """
    IS_GRAPH = True

    def __init__(self, node=None):
        super(DAG, self).__init__(node)

    def run(self):
        logging.info('-' * 100)
        config = Configuration(host="https://host.docker.internal:2746")
        config.verify_ssl = False
        #config.assert_hostname = False
        client = ApiClient(configuration=config)
        service = WorkflowServiceApi(api_client=client)
        """
        WORKFLOW = 'https://raw.githubusercontent.com/argoproj/argo/v2.11.8/examples/dag-diamond-steps.yaml'

        resp = requests.get(WORKFLOW)
        manifest: dict = yaml.safe_load(resp.text)

        service.create_workflow('argo', V1alpha1WorkflowCreateRequest(workflow=manifest))
        """
        manifest_yaml = self._create_yaml()
        logging.warning('\n' + manifest_yaml)
        service.create_workflow('argo', V1alpha1WorkflowCreateRequest(workflow=manifest_yaml))
        logging.info('done' * 100)
        raise 'Don`t validate'
        return NodeRunningStatus.SUCCESS

    def status(self):
        raise NotImplementedError()

    def kill(self):
        raise NotImplementedError()

    def validate(self):
        validation_error = super().validate()
        if validation_error:
            return validation_error

        logging.error('TODO: Remove run in validation')
        self.run()

        violations = []
        sub_nodes = self.node.get_parameter_by_name('_nodes').value.value

        if len(sub_nodes) == 0:
            violations.append(
                plynx.db.validation_error.ValidationError(
                    target=ValidationTargetType.GRAPH,
                    object_id=str(self.node._id),
                    validation_code=ValidationCode.EMPTY_GRAPH
                ))

        for node in sub_nodes:
            node_violation = plynx.utils.executor.materialize_executor(node.to_dict()).validate()
            if node_violation:
                violations.append(node_violation)

        if len(violations) == 0:
            return None

        return plynx.db.validation_error.ValidationError(
            target=ValidationTargetType.GRAPH,
            object_id=str(self.node._id),
            validation_code=ValidationCode.IN_DEPENDENTS,
            children=violations
        )

    @classmethod
    def get_default_node(cls, is_workflow):
        node = super().get_default_node(is_workflow)
        node.title = 'New DAG workflow'
        return node

    def _create_yaml(self):
        ENTRYPOINT = 'dag'
        templates = []
        body = {
            'apiVersion': 'argoproj.io/v1alpha1',
            'kind': 'Workflow',
            'metadata': {
                'generateName': 'dag-diamond-',
            },
            'spec': {
                'entrypoint': ENTRYPOINT,
                'templates': templates
            }
        }

        sub_nodes = self.node.get_parameter_by_name('_nodes').value.value


        # fill step templates
        for node in sub_nodes:
            # orig_node_id_to_nodes[node.original_node_id].append(node)
            params = []
            for parameter in node.parameters:
                if parameter.name in {'_image', '_command'}:
                    continue
                params.append({'name': parameter.name})
            item = {
                'name': str(node._id),
                'inputs': {
                    'parameters': params
                },
                'container': {
                    'image': node.get_parameter_by_name('_image').value,
                    'command': ['/bin/sh', '-c'],
                    'args': node.get_parameter_by_name('_command').value,
                }
            }
            templates.append(item)

        tasks = []
        dag_template = {
            'name': ENTRYPOINT,
            'tasks': tasks,
        }

        for node in sub_nodes:
            dependencies = []
            for input in node.inputs:
                for input_reference in input.input_references:
                    dependencies.append(input_reference.node_id)
            params = []
            for parameter in node.parameters:
                if parameter.name in {'_image', '_command'}:
                    continue
                params.append({'name': parameter.name, 'value': parameter.value})
            item = {
                'name': str(node._id),
                'template': str(node._id),
                'dependencies': dependencies,
                'parameters': params,
            }
            tasks.append(item)

        templates.append(dag_template)

        stream = StringIO()
        yaml.dump(body, stream)
        return stream.getvalue()


"""
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: dag-diamond-
spec:
  entrypoint: diamond
  templates:
  - name: echo
    inputs:
      parameters:
      - name: message
    container:
      image: alpine:3.7
      command: [echo, "{{inputs.parameters.message}}"]
  - name: diamond
    dag:
      tasks:
      - name: A
        template: echo
        arguments:
          parameters: [{name: message, value: A}]
      - name: B
        dependencies: [A]
        template: echo
        arguments:
          parameters: [{name: message, value: B}]
      - name: C
        dependencies: [A]
        template: echo
        arguments:
          parameters: [{name: message, value: C}]
      - name: D
        dependencies: [B, C]
        template: echo
        arguments:
          parameters: [{name: message, value: D}]
"""
