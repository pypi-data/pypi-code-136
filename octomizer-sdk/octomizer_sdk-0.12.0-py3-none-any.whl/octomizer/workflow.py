"""Resource representing a Workflow."""
from __future__ import annotations

import os
import re
import subprocess
import tarfile
import tempfile
import time
import typing

import requests

import octomizer.model as model_
from octomizer import client
from octomizer.logging_ import LOG
from octomizer.package_type import PackageType
from octoml.octomizer.v1 import (
    benchmark_pb2,
    engine_pb2,
    octomizer_service_pb2,
    workflows_pb2,
)

DEFAULT_WORKFLOW_TIMEOUT_SECONDS = 300
"""The default number of seconds to wait for a Workflow to finish."""

DEFAULT_WORKFLOW_POLL_INTERVAL_SECONDS = 10
"""The default number of seconds to wait between polling for Workflow statuses."""


class WorkflowTimeoutError(Exception):
    """Indicates a Workflow timed out while being awaited."""


class Workflow:
    """Represents an OctoML Workflow."""

    _TERMINAL_WORKFLOW_STATES = {
        workflows_pb2.WorkflowStatus.WorkflowState.COMPLETED,
        workflows_pb2.WorkflowStatus.WorkflowState.FAILED,
        workflows_pb2.WorkflowStatus.WorkflowState.CANCELED,
    }

    def __init__(
        self,
        client: client.OctomizerClient,
        model: typing.Optional[model_.Model] = None,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[workflows_pb2.Workflow] = None,
    ):
        """Initializes a new Workflow.

        :param client: an instance of the OctoML client.
        :param model: deprecated, the Model this Workflow is associated with.
        :param uuid: the id of this Workflow in the OctoML Platform.
        :param proto: the underyling protobuf object wrapped by this Workflow.
        """
        self._client = client

        if proto:
            # Proto has been provided.
            self._proto = proto
        elif uuid:
            # Fetch Workflow by UUID.
            workflow = self._client.get_workflow(uuid)
            self._proto = workflow.proto
            pass
        else:
            # This is a new Workflow builder.
            self._proto = workflows_pb2.Workflow()

        if model:
            LOG.warning(
                "The `model` field will be deprecated and is no longer necessary to get/create Workflows."
            )

    def __str__(self) -> str:
        return str(self._proto)

    @property
    def uuid(self) -> str:
        """Return the UUID for this Workflow."""
        return self._proto.uuid

    @property
    def proto(self) -> workflows_pb2.Workflow:
        """Return the raw representation for this Workflow."""
        return self._proto

    @property
    def model(self) -> model_.Model:
        """Return the model associated with this Workflow."""
        model_uuid = self.proto.model_uuid
        return self._client.get_model(model_uuid)

    def status(self) -> workflows_pb2.WorkflowStatus:
        """Returns the current status of this Workflow."""
        self.refresh()
        return self._proto.status

    def state(self) -> workflows_pb2.WorkflowStatus.WorkflowState:
        """Returns the current state of this Workflow."""
        self.refresh()
        return self._proto.status.state

    def done(self) -> bool:
        """Returns True if this Workflow has finished."""
        self.refresh()
        return self.is_terminal()

    def is_terminal(self) -> bool:
        """Returns True if this Workflow is in a terminal state"""
        return self._proto.status.state in self._TERMINAL_WORKFLOW_STATES

    def completed(self) -> bool:
        """Returns True if this Workflow has completed successfully."""
        self.refresh()
        return (
            self._proto.status.state
            == workflows_pb2.WorkflowStatus.WorkflowState.COMPLETED
        )

    def progress(self) -> workflows_pb2.Progress:
        """Returns the progress of this Workflow."""
        self.refresh()
        return self._proto.status.workflow_progress

    def result(self) -> workflows_pb2.WorkflowResult:
        """Returns the result of this Workflow. The result is only valid if the Workflow
        has finished running."""
        self.refresh()
        return self._proto.status.result

    def refresh(self) -> Workflow:
        """Get the latest status of this Workflow from the OctoML Platform."""
        if not self.is_terminal():
            request = octomizer_service_pb2.GetWorkflowRequest(
                workflow_uuid=self._proto.uuid
            )
            self._proto = self._client.stub.GetWorkflow(request)
        return self

    def wait(  # type: ignore
        self,
        timeout: typing.Optional[int] = DEFAULT_WORKFLOW_TIMEOUT_SECONDS,
        poll_interval: int = DEFAULT_WORKFLOW_POLL_INTERVAL_SECONDS,
        poll_callback: typing.Optional[typing.Callable[[Workflow], None]] = None,
    ) -> workflows_pb2.WorkflowStatus.WorkflowState:
        """Waits until this Workflow has finished or the given timeout has elapsed.

        :param timeout: the number of seconds to wait for this Workflow.
        :param poll_interval: the number of seconds to wait between polling for the
            status of this workflow.
        :param poll_callback: Optional callback invoked with `self` as an argument each time
            the Workflow status is polled.
        :return: the terminal state of this workflow.
        :raise: WorkflowTimeoutError if timeout seconds elapse before the Workflow
            reaches a terminal state.
        """
        start_time = time.time()
        while not self.done():
            assert self._proto is not None
            if poll_callback is not None:
                poll_callback(self)
            if timeout is not None and time.time() - start_time > timeout:
                raise WorkflowTimeoutError(
                    f"Timeout occurred while waiting on {self._proto.uuid}, status is "
                    f"{workflows_pb2.WorkflowStatus.WorkflowState.Name(self._proto.status.state)}"
                )
            time.sleep(poll_interval)

        if poll_callback is not None:
            poll_callback(self)
        return self._proto.status.state

    def cancel(self) -> Workflow:
        """Cancel this Workflow if it hasn't already been canceled/completed/failed."""
        # Canceling a terminal workflow won't do anything
        if self.is_terminal():
            return self

        # Try to cancel the workflow
        try:
            request = octomizer_service_pb2.CancelWorkflowRequest(
                workflow_uuid=self._proto.uuid
            )
            self._proto = self._client.stub.CancelWorkflow(request)
        except Exception as e:
            # Maybe the Workflow has already been canceled/failed/completed
            self.refresh()
            if not self.is_terminal():
                raise e
        return self

    def metrics(self) -> benchmark_pb2.BenchmarkMetrics:
        """Return the BenchmarkMetrics for this Workflow.

        The result is only valid if the Workflow had a Benchmark stage, and the
        Workflow state is WorkflowState.COMPLETED.
        """
        assert (
            self.completed()
        ), "Workflow is not yet completed, check completion status with Workflow.completed()"
        assert (
            self.has_benchmark_stage()
        ), "Workflow does not have benchmark stage, check for benchmark stage with Workflow.has_benchmark_stage()"
        orig_metrics = self._proto.status.result.benchmark_result.metrics
        # Hide full_metrics_dataref_uuid and compile_ms.
        return benchmark_pb2.BenchmarkMetrics(
            latency_mean_ms=orig_metrics.latency_mean_ms,
            latency_std_ms=orig_metrics.latency_std_ms,
        )

    def has_benchmark_stage(self) -> bool:
        """Returns True when the workflow contains a benchmark stage, False
        otherwise.
        """
        return self._proto.HasField("benchmark_stage_spec")

    def package_url(
        self, package_type: typing.Optional[PackageType] = PackageType.PYTHON_PACKAGE
    ) -> str:
        """Return the URL of the package output for this Workflow.

        :param package_type: The package type we want to get the url for.
            Defaults to Python wheel.

        The result is only valid if the Workflow had a Package stage, the
        package type is available for the specified runtime engine, and the
        Workflow state is WorkflowState.COMPLETED.

        :raises ValueError when a package type isn't available or when there is
            no package DataRef UUID.
        """
        assert self.completed()

        results = self._proto.status.result.package_result

        package_uuid = _get_package_dataref_uuid(results, package_type)

        if not package_uuid:
            # Get Engine type for better error message
            engine_type = getattr(
                self._proto.package_stage_spec.engine,
                self._proto.package_stage_spec.engine.WhichOneof("engine_spec"),
            )
            hardware_target = self._proto.hardware.platform
            if isinstance(engine_type, engine_pb2.TVMEngineSpec):
                runtime_engine = "TVM"
            elif isinstance(engine_type, engine_pb2.ONNXRuntimeEngineSpec):
                runtime_engine = "ONNX-RT"
            elif isinstance(engine_type, engine_pb2.TensorFlowEngineSpec):
                runtime_engine = "TensorFlow"
            elif isinstance(engine_type, engine_pb2.TFLiteEngineSpec):
                runtime_engine = "TFLite"
            elif isinstance(engine_type, engine_pb2.TorchscriptEngineSpec):
                runtime_engine = "Torchscript"
            else:
                runtime_engine = "Unknown"
            raise ValueError(
                f"No package DataRef UUID in Workflow result: {self._proto.status.result}. "
                f"Please confirm that {package_type} is available for engine ({runtime_engine}) on "
                f"target ({hardware_target})."
            )
        package_dataref = self._client.get_dataref(package_uuid)
        return package_dataref.url

    def save_package(
        self,
        out_dir: str,
        package_type: typing.Optional[PackageType] = PackageType.PYTHON_PACKAGE,
    ) -> str:
        """Download the package result for this Workflow to the given directory,
        and returns the full path to the package.

        :out_dir: Where the package will be saved to.
        :param package_type: The package type we want to save. Defaults to
            Python wheel.

        The result is only valid if the Workflow had a Package stage, and the
        Workflow state is WorkflowState.COMPLETED.
        """
        assert self.completed()
        response = requests.get(self.package_url(package_type))
        response.raise_for_status()

        # NOTE: A Content-Disposition filename should exist on all package datarefs,
        # but is optional on other datarefs.
        disposition = response.headers.get("Content-Disposition", "")
        p = re.compile(r"attachment; filename=(.*)")
        matches = p.fullmatch(disposition)

        if matches is None:
            raise ValueError("Invalid Content-Disposition for a package dataref.")

        filename = matches.group(1)
        out_file = os.path.join(out_dir, filename)
        with open(out_file, "wb") as outfile:
            outfile.write(response.content)

        return out_file

    def docker_build_triton(self, tag):
        """Downloads the Triton Docker build package, extracts all of the files and builds a Docker image.

        :tag: The name and tag (name:tag) of the Docker image.
        """
        with tempfile.TemporaryDirectory() as out_dir:
            tar_file = self.save_package(out_dir, PackageType.DOCKER_BUILD_TRITON)
            with tarfile.open(tar_file) as tar:
                tar.extractall(path=out_dir)
            return subprocess.run(
                ["./build.sh", tag],
                cwd=out_dir,
            )


def _get_package_dataref_uuid(results, package_type):
    """Gets the package UUID from the package results according to package type."""
    package_uuid = None
    if package_type == PackageType.PYTHON_PACKAGE:
        package_uuid = results.python_package_result.package_dataref_uuid
    elif package_type == PackageType.LINUX_SHARED_OBJECT:
        package_uuid = results.linux_shared_object_result.package_dataref_uuid
    elif package_type == PackageType.DOCKER_BUILD_TRITON:
        package_uuid = results.docker_build_triton_result.package_dataref_uuid
    elif package_type == PackageType.ONNXRUNTIME_CUSTOM_OPERATOR_LINUX:
        package_uuid = (
            results.onnx_runtime_custom_operator_linux_result.package_dataref_uuid
        )
    else:
        raise ValueError(f"Package type {package_type} is not available.")
    return package_uuid
