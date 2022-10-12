"""Generic wrapper for ModelVariants in the OctoML Platform."""
from __future__ import annotations

import abc
import enum
import re
import typing
import warnings
from dataclasses import dataclass

from octomizer import client, model, model_inputs, workflow
from octomizer.logging_ import LOG
from octoml.octomizer.v1 import (
    autotune_pb2,
    benchmark_pb2,
    engine_pb2,
    hardware_pb2,
    model_inputs_pb2,
    models_pb2,
    octomizer_service_pb2,
    package_pb2,
    workflows_pb2,
)

ONNXRuntimeExecutionProvider = typing.Union[
    engine_pb2.ONNXRuntimeCPUSpec,
    engine_pb2.ONNXRuntimeOpenVINOSpec,
    engine_pb2.ONNXRuntimeTensorRTSpec,
    engine_pb2.ONNXRuntimeCUDASpec,
]


class ModelVariantFormat(enum.Enum):
    """An enum representing the formats a ModelVariant can be in."""

    ONNX = "onnx"
    RELAY = "relay"
    TENSORFLOW = "tensorflow"
    TFLITE = "tflite"
    TORCHSCRIPT = "torchscript"


class PackageOptions(abc.ABC):
    @staticmethod
    def _default() -> PackageOptions:
        return TVMPackageOptions()

    @staticmethod
    def _from_engine_spec(
        engine_spec: typing.Optional[engine_pb2.EngineSpec],
    ) -> typing.Optional[PackageOptions]:
        if not engine_spec:
            return None
        engine = getattr(engine_spec, engine_spec.WhichOneof("engine_spec"))
        if isinstance(engine, engine_pb2.ONNXRuntimeEngineSpec):
            return OnnxPackageOptions(engine_spec=engine_spec)
        elif isinstance(engine, engine_pb2.TVMEngineSpec):
            return TVMPackageOptions(engine_spec=engine_spec)
        elif isinstance(engine, engine_pb2.TensorFlowEngineSpec):
            return TensorFlowPackageOptions()
        elif isinstance(engine, engine_pb2.TorchscriptEngineSpec):
            return TorchscriptPackageOptions()
        else:  # No other engine specs have package support yet
            return None

    @staticmethod
    def _from_format(
        model_format: ModelVariantFormat,
    ) -> typing.Optional[PackageOptions]:
        if model_format == ModelVariantFormat.ONNX:
            return OnnxPackageOptions()
        elif model_format == ModelVariantFormat.RELAY:
            return TVMPackageOptions()
        elif model_format == ModelVariantFormat.TENSORFLOW:
            return TensorFlowPackageOptions()
        elif model_format == ModelVariantFormat.TORCHSCRIPT:
            return TorchscriptPackageOptions()
        else:  # No other model variants have package support yet
            return None

    @abc.abstractmethod
    def _apply_to_spec(self, package_spec: package_pb2.PackageStageSpec):
        """Get the engine spec prepresenting the PackageOptions"""


@dataclass
class TVMPackageOptions(PackageOptions):
    """Specifies packaging options for TVM runtime"""

    engine_spec: typing.Optional[engine_pb2.EngineSpec] = None
    """The Relay optimization level to use."""

    def _apply_to_spec(self, package_spec: package_pb2.PackageStageSpec):
        engine_spec = engine_pb2.EngineSpec()

        tvm_engine_spec = engine_pb2.TVMEngineSpec()
        if self.engine_spec:
            engine_spec.CopyFrom(self.engine_spec)
        else:
            tvm_engine_spec.relay_opt_lvl = 3
            tvm_engine_spec.enable_profiler = False
            tvm_engine_spec.tvm_num_threads = 0
            engine_spec.tvm_engine_spec.CopyFrom(tvm_engine_spec)

        package_spec.engine.CopyFrom(engine_spec)


@dataclass
class OnnxPackageOptions(PackageOptions):
    """Specifies packaging to the ONNX runtime"""

    engine_spec: engine_pb2.EngineSpec = engine_pb2.EngineSpec(
        onnxruntime_engine_spec=engine_pb2.ONNXRuntimeEngineSpec()
    )
    """The engine spec to use for the ONNX package."""

    def _apply_to_spec(self, package_spec: package_pb2.PackageStageSpec):
        package_spec.engine.CopyFrom(self.engine_spec)


@dataclass
class TensorFlowPackageOptions(PackageOptions):
    """Specifies packaging to the Tensorflow runtime"""

    def _apply_to_spec(self, package_spec: package_pb2.PackageStageSpec):
        engine_spec = engine_pb2.EngineSpec()

        tensorflow_engine_spec = engine_pb2.TensorFlowEngineSpec()
        engine_spec.tensor_flow_engine_spec.CopyFrom(tensorflow_engine_spec)

        package_spec.engine.CopyFrom(engine_spec)


@dataclass
class TorchscriptPackageOptions(PackageOptions):
    """Specifies packaging to the Torchscript runtime"""

    def _apply_to_spec(self, package_spec: package_pb2.PackageStageSpec):
        engine_spec = engine_pb2.EngineSpec()

        torchscript_engine_spec = engine_pb2.TorchscriptEngineSpec()
        engine_spec.torchscript_engine_spec.CopyFrom(torchscript_engine_spec)

        package_spec.engine.CopyFrom(engine_spec)


@dataclass
class AutoTVMOptions:
    """Specifies options for autotuning using AutoTVM."""

    kernel_trials: int = 2000
    """Number of trials for each kernel during autotuning -- records are pulled from a cache if available,
    and the remaining trials are actively tuned.
    """

    exploration_trials: int = 0
    """[experimental, use at your own risk] Minimum number of trials to tune from scratch during
    autotuning. Note for each tuning job, max(kernel_trials - cached trials, exploration_trials)
    number of trials are actively tuned.
    """

    random_trials: int = 0
    """[experimental, use at your own risk] On top of any cached trials, this indicates the
    maximum additional random records from the cache to seed autotuning if available.
    """

    early_stopping_threshold: int = 500
    """Threshold to terminate autotuning if results have not improved in this many iterations."""

    def _apply_to_spec(self, autotune_stage_spec: autotune_pb2.AutotuneStageSpec):
        """Modifies an AutotuneStageSpec to use these tuning settings."""
        autotune_stage_spec.autotvm.CopyFrom(
            autotune_pb2.AutoTVMSpec(
                kernel_trials=self.kernel_trials,
                early_stopping_threshold=self.early_stopping_threshold,
                exploration_trials=self.exploration_trials,
                random_trials=self.random_trials,
            )
        )


@dataclass
class AutoschedulerOptions:
    """Specifies options for autotuning using Autoscheduler."""

    trials_per_kernel: int = 1000
    """Number of trials for each kernel during autotuning."""

    early_stopping_threshold: int = 250
    """Threshold to terminate autotuning if results have not improved in this many iterations."""

    top_trials_per_kernel: int = 10
    """Number of top trials to retrieve from the cache, if possible."""

    def _apply_to_spec(self, autotune_stage_spec: autotune_pb2.AutotuneStageSpec):
        """Modifies an AutotuneStageSpec to use these tuning settings."""
        autotune_stage_spec.autoscheduler.CopyFrom(
            autotune_pb2.AutoSchedulerSpec(
                exploration_trials_per_kernel=self.trials_per_kernel,
                early_stopping_threshold=self.early_stopping_threshold,
                top_trials_per_kernel=self.top_trials_per_kernel,
            )
        )


@dataclass
class MetascheduleOptions:
    """Specifies options for autotuning using Metaschedule."""

    exploration_trials_per_kernel: int = 1000
    """Number of trials to explore for each kernel during autotuning."""

    top_trials_per_kernel: int = 10
    """Number of trials to import from previous tuning runs."""

    def _apply_to_spec(self, autotune_stage_spec: autotune_pb2.AutotuneStageSpec):
        """Modifies an AutotuneStageSpec to use these tuning settings."""
        autotune_stage_spec.metascheduler.CopyFrom(
            autotune_pb2.MetaSchedulerSpec(
                exploration_trials_per_kernel=self.exploration_trials_per_kernel,
                top_trials_per_kernel=self.top_trials_per_kernel,
            )
        )


class ModelVariant:
    """Represents a ModelVariant on the OctoML Platform."""

    def __init__(
        self,
        client: client.OctomizerClient,
        model: model.Model,
        uuid: typing.Optional[str] = None,
        proto: typing.Optional[models_pb2.ModelVariant] = None,
    ):
        """Initializes a new ModelVariant.

        :param client: an instance of the OctoML client.
        :param model: the Model this ModelVariant is associated with.
        :param uuid: the id of this ModelVariant in the OctoML Platform.
        :param proto: the underyling protobuf object wrapped by this ModelVariant.
        """
        self._client = client
        self.model = model
        if proto:
            # Proto has been provided.
            self.proto = proto
        elif uuid:
            # Fetch ModelVariant by UUID.
            self.proto = self._get_model_variant_by_uuid(uuid)
        else:
            raise ValueError("Must provide either uuid or proto")

    def __str__(self) -> str:
        return str(self.proto)

    def __eq__(self, other) -> bool:
        return self.proto == other.proto

    @property
    def uuid(self) -> str:
        """Return the UUID for this Model."""
        return self.proto.uuid

    @property
    def format(self) -> ModelVariantFormat:  # type: ignore
        """Returns the ModelVariantFormat of this ModelVariant.

        :return: the ModelVariantFormat of this ModelVariant.
        """
        assert self.proto is not None
        if self.proto.model_format_config.relay_model_config.model_dataref_uuid:
            return ModelVariantFormat.RELAY
        if self.proto.model_format_config.onnx_model_config.model_dataref_uuid:
            return ModelVariantFormat.ONNX
        elif self.proto.model_format_config.tensor_flow_model_config.model_dataref_uuid:
            return ModelVariantFormat.TENSORFLOW
        elif self.proto.model_format_config.tflite_model_config.model_dataref_uuid:
            return ModelVariantFormat.TFLITE
        elif self.proto.model_format_config.torchscript_model_config.model_dataref_uuid:
            return ModelVariantFormat.TORCHSCRIPT
        else:
            raise ValueError(
                f"Unexpected value for model_format_config: {str(self.proto.model_format_config)}"
            )

    @property
    def inputs(
        self,
    ) -> typing.Tuple[typing.Dict[str, typing.List[int]], typing.Dict[str, str]]:
        """Return the input shapes and dtypes for this ModelVariant. Shapes are
        expected to be positive but -1 can be used as a sentinel when the
        dim is unknown and the user is expected to clarify.
        """
        inputs = self.proto.inputs.input_fields
        input_shapes = {i.input_name: list(i.input_shape) for i in inputs}
        input_dtypes = {i.input_name: i.input_dtype for i in inputs}
        return input_shapes, input_dtypes

    def _get_model_variant_by_uuid(self, uuid: str) -> models_pb2.ModelVariant:
        """Get the model variant proto for the given UUID from the OctoML Platform.

        :param uuid: the model UUID to retrieve.
        """
        request = octomizer_service_pb2.GetModelVariantRequest(model_variant_uuid=uuid)
        return self._client.stub.GetModelVariant(request)

    def create_workflow(
        self, workflow_spec: workflows_pb2.Workflow
    ) -> workflow.Workflow:
        """Creates a new Workflow for this ModelVariant.

        :param workflow_spec: the specification for the Workflow to be created.
        :return: the new Workflow.
        """
        assert self.model is not None
        request = octomizer_service_pb2.CreateWorkflowRequest(workflow=workflow_spec)
        response = self._client.stub.CreateWorkflow(request)
        LOG.warning(
            f"Started workflow: {response.uuid}. You'll be emailed when it finishes."
        )
        return workflow.Workflow(
            client=self._client,
            proto=response,
        )

    def benchmark(
        self,
        platform: str,
        num_benchmark_trials: int = 30,
        num_runs_per_trial: int = 1,
        max_time_seconds: int = 120,
        min_time_seconds: int = 10,
        relay_opt_lvl: int = 3,
        enable_profiler: bool = True,
        tvm_num_threads: int = 0,
        untuned_tvm: bool = False,
        input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        create_package: bool = False,
        package_name: typing.Optional[str] = None,
        use_onnx_engine: bool = False,
        intra_op_num_threads: int = 0,
        onnx_execution_provider: typing.Optional[ONNXRuntimeExecutionProvider] = None,
        benchmark_tvm_in_onnxruntime: bool = False,
    ) -> workflow.Workflow:
        """Benchmark this ModelVariant. This is a convenience function that creates a Workflow
        consisting of a single benchmarking stage.

        :param platform: The hardware platform to target. Available platforms can be queried
            via the `get_hardware_targets` method on an OctomizerClient. If you would like to
            benchmark on other hardware platforms, please submit a feature request
            `here <https://octoml.atlassian.net/servicedesk/customer/portal/6>`_.
        :param num_benchmark_trials: Number of benchmarking trials to execute.
        :param num_runs_per_trial: Number of benchmarks to run per trial.
        :param max_time_seconds: The maximum benchmark duration; zero implies no time limit.
            Note that the experiment may consist of fewer trials than specified.
        :param min_time_seconds: The minimum benchmark duration; zero implies no minimum time.
            Note that the experiment may consist of more trials than specified.
        :param relay_opt_lvl: The Relay optimization level to use, if the model format is Relay.
        :param enable_profiler: Whether to enable the RelayVM profiler when benchmarking,
            if the model format is Relay. Profiling is done as an additional step, so
            it does not affect the values of the standard metrics that are reported.
        :param tvm_num_threads: Number of threads that TVM runtime uses when running inference.
            By default, this is set to vcpu_count/2 for hyperthreading hardware targets and vcpu_count
            for non-hyperthreading hardware targets, to give you best performance.
            Setting to 0 enables TVM to automatically decide number of threads.
        :param untuned_tvm: Whether this is a baseline untuned TVM benchmark.
        :param create_package: Whether a package should be created or not. Defaults to False.
        :param package_name: The name of the package. If unset or empty, will default
            to the name of the model. Note: Non-alphanumeric characters in the name will
            be replaced with underscores ('_') and trailing/leading underscores will be
            stripped. Valid package names must only contain lower case letters, numbers,
            and single (non leading/trailing) underscores ('_').
        :param intra_op_num_threads: The number of threads to use for ONNXRuntimeCPUSpec
            benchmarks/packages (which uses ONNX-RT's CPUExecutionProvider).
            Default is 0, which is physical core count of the platform.
        :param onnx_execution_provider: The execution provider to use for ONNX benchmarks.
            Note that not every execution provider is valid for every platform.
        :param benchmark_tvm_in_onnxruntime: Whether we should run the benchmark as a TVM -> ONNX
            custom op model. (Only for Relay models.)

        :return A Workflow instance.
        """
        proto = workflows_pb2.Workflow(
            model_uuid=self.model.uuid,
            model_variant_uuid=self.uuid,
        )
        proto.hardware.CopyFrom(
            hardware_pb2.HardwareSpec(
                platform=platform,
            )
        )
        engine_spec = engine_pb2.EngineSpec()
        if untuned_tvm or self.format == ModelVariantFormat.RELAY:
            # separate cases with the same proto (at this time)
            tvm_engine_spec = engine_pb2.TVMEngineSpec()
            tvm_engine_spec.relay_opt_lvl = relay_opt_lvl
            tvm_engine_spec.enable_profiler = enable_profiler
            tvm_engine_spec.tvm_num_threads = tvm_num_threads
            tvm_engine_spec.onnxruntime_benchmark = benchmark_tvm_in_onnxruntime
            engine_spec.tvm_engine_spec.CopyFrom(tvm_engine_spec)
        elif self.format == ModelVariantFormat.ONNX or use_onnx_engine:
            onnx_spec = engine_pb2.ONNXRuntimeEngineSpec(
                intra_op_num_threads=intra_op_num_threads,
            )
            _set_onnx_ep(onnx_spec, onnx_execution_provider)
            engine_spec.onnxruntime_engine_spec.CopyFrom(onnx_spec)
        elif self.format == ModelVariantFormat.TENSORFLOW:
            engine_spec.tensor_flow_engine_spec.CopyFrom(
                engine_pb2.TensorFlowEngineSpec()
            )
        elif self.format == ModelVariantFormat.TFLITE:
            engine_spec.tflite_engine_spec.CopyFrom(engine_pb2.TFLiteEngineSpec())
        elif self.format == ModelVariantFormat.TORCHSCRIPT:
            engine_spec.torchscript_engine_spec.CopyFrom(
                engine_pb2.TorchscriptEngineSpec()
            )
        else:
            raise ValueError(f"Unknown model format: {self.format}")

        benchmark_spec = benchmark_pb2.BenchmarkStageSpec()
        benchmark_spec.engine.CopyFrom(engine_spec)
        benchmark_spec.num_trials = num_benchmark_trials
        benchmark_spec.runs_per_trial = num_runs_per_trial
        benchmark_spec.max_time_seconds = max_time_seconds
        benchmark_spec.min_time_seconds = min_time_seconds

        model_inputs_proto = self._get_model_inputs_proto(input_shapes, input_dtypes)
        if model_inputs_proto is not None:
            benchmark_spec.model_inputs.CopyFrom(model_inputs_proto)
        proto.benchmark_stage_spec.CopyFrom(benchmark_spec)

        if create_package:
            package_spec = self._package_spec_helper(
                None, engine_spec, model_inputs_proto, package_name
            )
            if package_spec:
                proto.package_stage_spec.CopyFrom(package_spec)
        return self.create_workflow(proto)

    def accelerate(  # noqa: C901
        self,
        platform: str,
        relay_opt_lvl: int = 3,
        enable_profiler: bool = True,
        tvm_num_threads: int = 0,
        kernel_trials: typing.Optional[int] = None,
        exploration_trials: typing.Optional[int] = None,
        random_trials: typing.Optional[int] = None,
        early_stopping_threshold: typing.Optional[int] = None,
        num_benchmark_trials: int = 30,
        num_runs_per_trial: int = 1,
        max_time_seconds: int = 120,
        min_time_seconds: int = 10,
        input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        tuning_options: typing.Optional[
            typing.Union[AutoTVMOptions, AutoschedulerOptions, MetascheduleOptions]
        ] = None,
        create_package: bool = True,
        package_name: typing.Optional[str] = None,
        benchmark_tvm_in_onnxruntime: bool = False,
    ) -> workflow.Workflow:
        """Accelerate this ModelVariant. This is a convenience function that creates a Workflow
        consisting of autotuning, benchmarking, and (optional) packaging stages.

        :param platform: The hardware platform to target. Available platforms can be queried
            via the `get_hardware_targets` method on an OctomizerClient. If you would like to
            benchmark on other hardware platforms, please submit a feature request
            `here <https://octoml.atlassian.net/servicedesk/customer/portal/6>`_.
        :param relay_opt_lvl: The Relay optimization level to use.
        :param enable_profiler: Whether to enable the RelayVM profiler when benchmarking.
            Profiling is done as an additional step, so it does not affect the values of
            the standard metrics that are reported.
        :param tvm_num_threads: Number of threads that TVM runtime uses when running inference.
            By default, this is set to vcpu_count/2 for hyperthreading hardware targets and
            vcpu_count for non-hyperthreading hardware targets, to give you best performance.
            Setting to 0 enables TVM to automatically decide number of threads.
        :param kernel_trials: deprecated, specify tuning_options instead.
        :param exploration_trials: deprecated, specify tuning_options instead.
        :param random_trials: deprecated, specify tuning_options instead.
        :param early_stopping_threshold: deprecated, specify tuning_options instead.
        :param num_benchmark_trials: Number of benchmarking trials to execute; if zero,
           then max_time_seconds value dictates benchmark duration.
        :param num_runs_per_trial: Number of benchmarks to run per trial.
        :param max_time_seconds: The maximum benchmark duration; zero implies no time limit.
            Note that the experiment may consist of fewer trials than specified.
        :param min_time_seconds: The minimum benchmark duration; zero implies no minimum time.
            Note that the experiment may consist of more trials than specified.
        :param input_shapes: dict mapping input name to shape. Must be provided if
            input_dtypes is provided.
        :param input_dtypes: dict mapping input name to dtype. Must be provied if
            input_shapes is provided.
        :param tuning_options: options to control the autotuning search. Provide either
            AutoTVMOptions or AutoschedulerOptions or MetascheduleOptions.
        :param create_package: Whether a package should be created or not. Defaults to True.
        :param package_name: The name of the package. If unset or empty, will default
            to the name of the model. Note: Non-alphanumeric characters in the name will
            be replaced with underscores ('_') and trailing/leading underscores will be
            stripped. Valid package names must only contain lower case letters, numbers,
            and single (non leading/trailing) underscores ('_').
        :param benchmark_tvm_in_onnxruntime: Whether we should run the benchmark as a TVM -> ONNX
            custom op model.

        :return A Workflow instance.

        :raises ValueError when the package name is not a valid package name.
        """
        proto = workflows_pb2.Workflow(
            model_uuid=self.model.uuid,
            model_variant_uuid=self.uuid,
        )
        proto.hardware.CopyFrom(
            hardware_pb2.HardwareSpec(
                platform=platform,
            )
        )
        model_inputs_proto = self._get_model_inputs_proto(input_shapes, input_dtypes)

        autotune_spec = autotune_pb2.AutotuneStageSpec()
        # We always target TVM when accelerating.
        tvm_engine_spec = engine_pb2.TVMEngineSpec()
        tvm_engine_spec.relay_opt_lvl = relay_opt_lvl
        tvm_engine_spec.enable_profiler = enable_profiler
        tvm_engine_spec.tvm_num_threads = tvm_num_threads
        tvm_engine_spec.onnxruntime_benchmark = benchmark_tvm_in_onnxruntime

        # For backwards compatibility, if any legacy (AutoTVM) options were specified,
        # use AutoTVM. Otherwise use Metascheduler defaults.
        if (
            kernel_trials is not None
            or exploration_trials is not None
            or random_trials is not None
            or early_stopping_threshold is not None
        ):
            autotvm_args = {}
            if kernel_trials is not None:
                autotvm_args["kernel_trials"] = kernel_trials
            if exploration_trials is not None:
                autotvm_args["exploration_trials"] = exploration_trials
            if random_trials is not None:
                autotvm_args["random_trials"] = random_trials
            if early_stopping_threshold is not None:
                autotvm_args["early_stopping_threshold"] = early_stopping_threshold
            tuning_options = AutoTVMOptions(**autotvm_args)
        elif tuning_options is None:
            tuning_options = MetascheduleOptions()

        if isinstance(tuning_options, AutoschedulerOptions) and self.proto.quantized:
            raise ValueError(
                "Auto-scheduler currently does not support quantized models. Quantized models can be accelerated via AutoTVM by passing AutoTVMOptions instead of AutoschedulerOptions."
            )

        tuning_options._apply_to_spec(autotune_spec)

        if model_inputs_proto is not None:
            autotune_spec.model_inputs.CopyFrom(model_inputs_proto)

        engine_spec = engine_pb2.EngineSpec(tvm_engine_spec=tvm_engine_spec)

        autotune_spec.engine.CopyFrom(engine_spec)
        proto.autotune_stage_spec.CopyFrom(autotune_spec)

        benchmark_spec = benchmark_pb2.BenchmarkStageSpec()
        benchmark_spec.engine.CopyFrom(engine_spec)
        benchmark_spec.num_trials = num_benchmark_trials
        benchmark_spec.runs_per_trial = num_runs_per_trial
        benchmark_spec.max_time_seconds = max_time_seconds
        benchmark_spec.min_time_seconds = min_time_seconds

        if model_inputs_proto is not None:
            benchmark_spec.model_inputs.CopyFrom(model_inputs_proto)
        proto.benchmark_stage_spec.CopyFrom(benchmark_spec)

        if create_package:
            package_spec = self._package_spec_helper(
                None, engine_spec, model_inputs_proto, package_name
            )
            if package_spec:
                proto.package_stage_spec.CopyFrom(package_spec)

        return self.create_workflow(proto)

    def package(
        self,
        platform: str,
        relay_opt_lvl: typing.Optional[int] = None,
        tvm_num_threads: typing.Optional[int] = None,
        input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
        package_name: typing.Optional[str] = None,
        package_options: typing.Optional[PackageOptions] = None,
    ) -> workflow.Workflow:
        """Package this ModelVariant. This is a convenience function that creates a Workflow
        consisting of a single packaging stage.

        :param platform: The hardware platform to target. Available platforms can be queried
            via the `get_hardware_targets` method on an OctomizerClient. If you would like to
            benchmark on other hardware platforms, please submit a feature request
            `here <https://octoml.atlassian.net/servicedesk/customer/portal/6>`_.
        :param relay_opt_lvl: Deprecated, specify relay optimization level with `package_options`
        :param tvm_num_threads: Deprecated, the number set here will not affect the package.
        :param input_shapes: dict mapping input name to shape. Must be provided if
            input_dtypes is provided.
        :param input_dtypes: dict mapping input name to dtype. Must be provied if
            input_shapes is provided.
        :param package_name: The name of the package. If unset or empty, will default
            to the name of the model. Note: Non-alphanumeric characters in the name will
            be replaced with underscores ('_') and trailing/leading underscores will be
            stripped. Valid package names must only contain lower case letters, numbers,
            and single (non leading/trailing) underscores ('_').

        :param package_options: Selects and configures runtime: TVMPackageOptions (TVM),
            or OnnxPackageOption (ONNX). All available package types for the specified
            runtime engine will be created.
        :return A Workflow instance.

        :raises ValueError when the package name is not a valid package name.
        """
        proto = workflows_pb2.Workflow(
            model_uuid=self.model.uuid,
            model_variant_uuid=self.uuid,
        )
        proto.hardware.CopyFrom(
            hardware_pb2.HardwareSpec(
                platform=platform,
            )
        )

        if tvm_num_threads is not None:
            warnings.warn(
                "Setting tvm_num_threads on packaging is deprecated and will not affect the package",
                DeprecationWarning,
                stacklevel=2,
            )

        if relay_opt_lvl is not None:
            warnings.warn(
                "The parameter relay_opt_lvl on package() is deprecated. In the future please use package_options to specify and configure runtime engine.",
                DeprecationWarning,
                stacklevel=2,
            )
            tvm_engine_spec = engine_pb2.TVMEngineSpec()
            tvm_engine_spec.relay_opt_lvl = relay_opt_lvl
            tvm_engine_spec.tvm_num_threads = tvm_num_threads or 3
            engine_spec = engine_pb2.EngineSpec(tvm_engine_spec=tvm_engine_spec)
            package_options = TVMPackageOptions(engine_spec=engine_spec)

        model_inputs_proto = self._get_model_inputs_proto(input_shapes, input_dtypes)
        package_spec = self._package_spec_helper(
            package_options, None, model_inputs_proto, package_name
        )

        assert package_spec
        proto.package_stage_spec.CopyFrom(package_spec)
        return self.create_workflow(proto)

    @staticmethod
    def _get_model_inputs_proto(
        input_shapes: typing.Optional[typing.Dict[str, typing.List[int]]] = None,
        input_dtypes: typing.Optional[typing.Dict[str, str]] = None,
    ) -> typing.Optional[model_inputs_pb2.ModelInputs]:
        """Converts model inputs to protos and relys on api to validate inputs."""

        if (input_shapes and input_dtypes is None) or (
            input_dtypes and input_shapes is None
        ):
            raise ValueError("Both input_shapes and input_dtypes must be set.")

        model_inputs_proto = None
        if input_shapes is not None and input_dtypes is not None:
            model_inputs_proto = model_inputs.inputs_to_input_proto(
                input_shapes, input_dtypes
            )
        return model_inputs_proto

    def _package_spec_helper(
        self,
        package_options: typing.Optional[PackageOptions] = None,
        engine_spec: typing.Optional[engine_pb2.EngineSpec] = None,
        model_inputs_proto: typing.Optional[model_inputs_pb2.ModelInputs] = None,
        package_name: typing.Optional[str] = None,
    ) -> typing.Optional[package_pb2.PackageStageSpec]:
        """Helper function to populate PackageStageSpec.

        :param package_options: Selects and configures runtime: TVMPackageOptions (TVM),
            or OnnxPackageOption (ONNX). All available package types for the specified
            runtime engine will be created.
        :param engine_spec: The engine spec that will be used. Helps determine the
            package option if package_options wasn't specified.
        :param model_inputs_proto: Shapes and dtypes of input to the model.
        :param package_name: Given name of the package, if any.

        :returns a PackageStageSpec with the given specifications.
        """
        package_spec = package_pb2.PackageStageSpec()

        # Takes package options from package_options if available
        # otherwise it determines the package options from the engine_spec if available (accelerate/benchmark)
        # otherwise it tries to get it from the format of the model if available (packaging)
        package_options = (
            package_options
            or PackageOptions._from_engine_spec(engine_spec)
            or PackageOptions._from_format(self.format)
        )

        # Failed to find a package option, so don't package.
        if not package_options:
            return None

        # Applies the EngineSpec.
        package_options._apply_to_spec(package_spec)

        if model_inputs_proto is not None:
            package_spec.model_inputs.CopyFrom(model_inputs_proto)

        if package_name:
            if not ModelVariant._validate_package_name(package_name):
                raise ValueError(
                    f"The package name, {package_name}, is not a valid package name."
                )
            package_spec.package_name = package_name
        return package_spec

    @staticmethod
    def _validate_package_name(package_name: str) -> bool:
        """Validates the package name only contains lower case letters, numbers,
        and single (non leading/trailing) underscores ('_').

        :param package_name: The package name to be validated

        :returns whether the package name is valid.
        """
        regex = r"^(?!.*[_]{2})([a-z0-9]|[a-z0-9][a-z0-9_]*[a-z0-9]+)$"
        pattern = re.compile(regex)
        return re.fullmatch(pattern, package_name) is not None


def _set_onnx_ep(
    onnx_spec: engine_pb2.ONNXRuntimeEngineSpec,
    onnx_execution_provider: typing.Optional[ONNXRuntimeExecutionProvider],
):
    """Sets the onnx execution spec based on which ONNX EP config was passed in.

    :param onnx_spec: The ONNXRuntimeEngineSpec proto.
    :param onnx_execution_provider: The onnx execution provider config
    """
    if isinstance(onnx_execution_provider, engine_pb2.ONNXRuntimeCPUSpec):
        onnx_spec.cpu.CopyFrom(onnx_execution_provider)
    elif isinstance(onnx_execution_provider, engine_pb2.ONNXRuntimeOpenVINOSpec):
        onnx_spec.openvino.CopyFrom(onnx_execution_provider)
    elif isinstance(onnx_execution_provider, engine_pb2.ONNXRuntimeTensorRTSpec):
        onnx_spec.tensorrt.CopyFrom(onnx_execution_provider)
    elif isinstance(onnx_execution_provider, engine_pb2.ONNXRuntimeCUDASpec):
        onnx_spec.cuda.CopyFrom(onnx_execution_provider)
