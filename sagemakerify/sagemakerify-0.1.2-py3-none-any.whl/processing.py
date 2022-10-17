import os
import shutil
import json
import inspect
import sagemaker_utils
from time import gmtime, strftime
from sagemaker.network import NetworkConfig
from sagemaker.processing import Processor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep
from sagemakerify import utils, globals, handler


class ProcessingHandler:
    def __init__(self, function, **kwargs):

        self.default_args = utils.get_default_args(function)
        self.session = kwargs.pop("session", globals.DEFAULTS.get("session", None))

        self.default_prefix = globals.DEFAULTS.get("prefix", "sagemakerify")
        self.project = globals.DEFAULTS.get("project", self.default_prefix)
        self.default_bucket = globals.DEFAULTS.get(
            "bucket", self.session.default_bucket()
        )

        self.base_image = kwargs.pop(
            "base_image", globals.DEFAULTS.get("base_image", None)
        )
        self.secret = kwargs.pop("secret", globals.DEFAULTS.get("secret", None))
        self.codebuild_role = kwargs.pop(
            "codebuild_role", globals.DEFAULTS.get("codebuild_role", None)
        )
        self.instance_count = kwargs.pop(
            "instance_count", globals.DEFAULTS.get("instance_count", None)
        )
        self.instance_type = kwargs.pop(
            "instance_type", globals.DEFAULTS.get("instance_type", None)
        )
        self.role = kwargs.pop("role", globals.DEFAULTS.get("role", None))
        self.volume_size_in_gb = kwargs.pop(
            "volume_size_in_gb", globals.DEFAULTS.get("volume_size_in_gb", None)
        )
        self.max_runtime_in_seconds = kwargs.pop(
            "max_runtime_in_seconds",
            globals.DEFAULTS.get("max_runtime_in_seconds", None),
        )
        self.tags = kwargs.pop("tags", globals.DEFAULTS.get("tags", None))
        self.volume_kms_key = kwargs.pop(
            "volume_kms_key", globals.DEFAULTS.get("volume_kms_key", None)
        )
        self.output_kms_key = kwargs.pop(
            "output_kms_key", globals.DEFAULTS.get("output_kms_key", None)
        )
        self.enable_network_isolation = kwargs.pop(
            "enable_network_isolation",
            globals.DEFAULTS.get("enable_network_isolation", None),
        )
        self.security_group_ids = kwargs.pop(
            "security_group_ids", globals.DEFAULTS.get("security_group_ids", None)
        )
        self.subnets = kwargs.pop("subnets", globals.DEFAULTS.get("subnets", None))
        self.encrypt_inter_container_traffic = kwargs.pop(
            "encrypt_inter_container_traffic",
            globals.DEFAULTS.get("encrypt_inter_container_traffic", None),
        )
        self.base_job_name = kwargs.pop("base_job_name", f"{self.project}").lower()
        self.image_env = kwargs.pop("image_env", {})
        self.data_s3_prefix = kwargs.pop("data_s3_prefix", None)
        self.code_s3_prefix = kwargs.pop("code_s3_prefix", None)
        self.image_s3_prefix = kwargs.pop("image_s3_prefix", None)
        self.image_uri = kwargs.pop("image_uri", None)
        self.libraries = kwargs.pop("libraries", None)
        self.dependencies = kwargs.pop("dependencies", None)
        self.image_name = kwargs.pop("image_name", None)
        self.others = kwargs.pop("others", None)
        self.kwargs = kwargs
        self.experiment_config = None

        build_image = self.image_uri is None

        self.role = utils.get_execution_role(self.role)

        if self.instance_count is None or self.instance_count <= 0:
            raise Exception("instance_count is required and must be grather than 0")
        elif self.instance_type is None:
            raise Exception("instance_type is required")
        elif self.role is None:
            raise Exception("role is required")
        elif self.volume_size_in_gb is None or self.volume_size_in_gb < 5:
            raise Exception(
                "volume_size_in_gb is required and must be grather or equal to 5 GB"
            )
        elif self.max_runtime_in_seconds is None or self.max_runtime_in_seconds <= 0:
            raise Exception(
                "max_runtime_in_seconds is required and must be grather than 0"
            )

        if build_image:
            if self.base_image is None:
                raise Exception("base_image is required")
            elif self.codebuild_role is None:
                raise Exception("codebuild_role is required or set it globally")

            if self.image_s3_prefix is None or len(self.image_s3_prefix) == 0:
                self.image_s3_prefix = (
                    f"s3://{self.default_bucket}/{self.default_prefix}/docker_images"
                )

        if self.code_s3_prefix is None:
            self.code_s3_prefix = (
                f"s3://{self.default_bucket}/{self.default_prefix}/code"
            )

        if self.data_s3_prefix is None:
            self.data_s3_prefix = (
                f"s3://{self.default_bucket}/{self.default_prefix}/data"
            )

        # Create a file with the code received
        (
            self.function_name,
            self.function_file,
            self.num_inputs,
            self.num_outputs,
        ) = utils.create_function_file(function)

        # Create handler code
        handler_file = f"{globals.DEFAULTS.source_code_location}/handler.py"
        sagemaker_utils.make_dirs(handler_file)
        with open(handler_file, "w") as f:
            f.write(inspect.getsource(handler))

        self.prefix_job_name = (
            f"{self.base_job_name}-{self.function_name}".lower().replace("_", "-")
        )

        if build_image:
            # Create docker image
            self.parameters = {
                "image_name": self.image_name
                if self.image_name is not None
                else self.prefix_job_name,
                "base_image": self.base_image,
                "s3_path": self.image_s3_prefix,
                "role": self.codebuild_role,
                "wait": True,
            }

            if self.libraries is not None:
                self.parameters["libraries"] = self.libraries

            if self.secret is not None:
                self.parameters["secret"] = self.secret

            if self.dependencies is not None:
                self.parameters["dependencies"] = self.dependencies
            else:
                self.parameters["dependencies"] = []

            self.parameters["dependencies"].append(
                (handler_file, "/opt/ml/code/handler.py")
            )

            if self.others is not None:
                self.parameters["others"] = self.others
            else:
                self.parameters["others"] = []

            self.parameters["others"].append("RUN pip install pandas pyarrow")

            self.parameters["env"] = self.image_env
            self.parameters["env"]["SAGEMAKER_SUBMIT_DIRECTORY"] = "/opt/ml/code"
            self.parameters["env"]["SAGEMAKER_PROGRAM"] = "handler.py"

            hash = utils.dict_hash(self.parameters)
            if globals.CACHE.get_image(self.parameters["image_name"])["hash"] != hash:
                self.image_uri = sagemaker_utils.create_docker_image(**self.parameters)

                globals.CACHE.set_image(
                    self.parameters["image_name"], self.image_uri, hash
                )

            else:
                self.image_uri = globals.CACHE.get_image(self.parameters["image_name"])[
                    "uri"
                ]

        # Creates a SageMaker Processor
        self.processor_parameters = {
            "image_uri": self.image_uri,
            "role": self.role,
            "instance_count": self.instance_count,
            "instance_type": self.instance_type,
            "entrypoint": ["python3", f"/opt/ml/code/handler.py"],
            "env": {
                "SM_OUTPUT_DATA_DIR": "/opt/ml/processing/output",
                "SM_MODEL_DIR": "/opt/ml/processing/output",
                "SM_CHANNEL_CONFIG": "/opt/ml/processing/input/config",
                "SM_CHANNEL_CODE": "/opt/ml/processing/input/code",
            },
            "volume_size_in_gb": self.volume_size_in_gb,
            "max_runtime_in_seconds": self.max_runtime_in_seconds,
            "sagemaker_session": self.session,
        }

        if self.tags is not None:
            self.processor_parameters["tags"] = self.tags

        if self.volume_kms_key is not None:
            self.processor_parameters["volume_kms_key"] = self.volume_kms_key

        if self.output_kms_key is not None:
            self.processor_parameters["output_kms_key"] = self.output_kms_key

        network_config = {}

        if self.enable_network_isolation is not None:
            network_config["enable_network_isolation"] = self.enable_network_isolation

        if self.security_group_ids is not None:
            network_config["security_group_ids"] = self.security_group_ids

        if self.subnets is not None:
            network_config["subnets"] = self.subnets

        if self.encrypt_inter_container_traffic is not None:
            network_config[
                "encrypt_inter_container_traffic"
            ] = self.encrypt_inter_container_traffic

        if len(network_config.keys()) > 0:
            self.processor_parameters["network_config"] = NetworkConfig(
                **network_config
            )

        for i in range(self.num_inputs):
            self.processor_parameters["env"][
                f"SM_CHANNEL_INPUT_{i+1}"
            ] = f"/opt/ml/processing/input/input_{i+1}"

        self.processor_parameters = dict(self.kwargs, **self.processor_parameters)

        self.processor = Processor(**self.processor_parameters)

    def run(self, *args, **kwargs):

        job_name = (
            f'{self.prefix_job_name}-{strftime("%d-%m-%y-%H-%M-%S", gmtime())}'.lower()
        )

        # Set arguments
        config = {"num_inputs": self.num_inputs}
        arguments = []
        kwargs.update(self.default_args)
        if len(kwargs) > 0:
            config["argument_types"] = {}
            for k in kwargs:
                if utils.is_builtin_class_instance(kwargs[k]):
                    config["argument_types"][k] = type(kwargs[k])
                    arguments.append(f"--{k.replace('_','-')}")
                    if config["argument_types"][k] is dict:
                        arguments.append(json.dumps(kwargs[k]))
                    else:
                        arguments.append(str(kwargs[k]))
                else:
                    raise Exception(f"{type(kwargs[k])} is not supported")

        # Serialize config
        config_file = utils.save_file(
            config, f"{globals.DEFAULTS.source_code_location}/config"
        )

        # Upload config to S3
        config_s3_path = sagemaker_utils.upload(
            config_file,
            f"{self.data_s3_prefix}/{job_name}",
            show_progress=False,
            session=self.session.boto_session,
        )

        # Upload function code to S3
        function_s3_path = sagemaker_utils.upload(
            self.function_file,
            f"{self.code_s3_prefix}/{job_name}",
            show_progress=False,
            session=self.session.boto_session,
        )

        arguments.append("--module")
        arguments.append(self.function_name)

        inputs = [
            ProcessingInput(
                input_name="config",
                source=config_s3_path,
                destination="/opt/ml/processing/input/config",
            ),
            ProcessingInput(
                input_name="code",
                source=function_s3_path,
                destination="/opt/ml/processing/input/code",
            ),
        ]

        # Create a ProcessingInput per required input parameter
        for i in range(self.num_inputs):
            input_file = utils.save_file(
                args[i], f"{globals.DEFAULTS.source_code_location}/input_{i+1}"
            )
            input_s3_path = sagemaker_utils.upload(
                input_file,
                f"{self.data_s3_prefix}/{job_name}",
                show_progress=False,
                session=self.session.boto_session,
            )

            inputs.append(
                ProcessingInput(
                    input_name=f"input_{i+1}",
                    source=input_s3_path,
                    destination=f"/opt/ml/processing/input/input_{i+1}",
                )
            )

        self.job_parameters = {
            "inputs": inputs,
            "outputs": [
                ProcessingOutput(
                    output_name=f"output_{i+1}",
                    source=f"/opt/ml/processing/output/output_{i+1}",
                    destination=f"{self.data_s3_prefix}/processed/{job_name}/output_{i+1}",
                )
                for i in range(self.num_outputs)
            ],
            "arguments": arguments,
        }

        self.processor.run(**dict({"job_name": job_name}, **self.job_parameters))

        self.processing_step = None

        outputs = []
        for i in range(self.num_outputs):
            output_files = sagemaker_utils.list_s3(
                f"{sagemaker_utils.get_processor_output_path(self.processor, f'output_{i+1}')}",
                session=self.session.boto_session,
            )

            if len(output_files) == 1:
                outputs.append(
                    sagemaker_utils.read_file(
                        output_files[0], session=self.session.boto_session
                    )
                )
            else:
                data_file = sagemaker_utils.list_s3(
                    f"{sagemaker_utils.get_processor_output_path(self.processor, f'output_{i+1}')}/output_{i+1}.data",
                    session=self.session.boto_session,
                )

                if len(data_file) == 1:
                    data_file = sagemaker_utils.read_json(
                        data_file[0], session=self.session.boto_session
                    )
                    original_path = data_file["value"].split("/")[-1]

                else:
                    original_path = ""

                output_files = sagemaker_utils.list_s3(
                    sagemaker_utils.get_processor_output_path(
                        self.processor, f"output_{i+1}"
                    ),
                    session=self.session.boto_session,
                )

                local_path = os.path.join("outputs", job_name, f"output_{i+1}")

                if os.path.exists(local_path):
                    shutil.rmtree(local_path)

                os.makedirs(local_path)

                if len(output_files) > 0:
                    for s3_path in output_files:
                        if f"output_{i+1}.data" not in s3_path:
                            sagemaker_utils.download(
                                s3_path,
                                os.path.join(local_path, os.path.basename(s3_path)),
                                show_progress=False,
                                session=self.session.boto_session,
                            )

                outputs.append(os.path.join(local_path, original_path))

        return tuple(outputs)

    def create_processing_step(self, name, **kwargs):
        self.processing_step_parameters = {
            "name": name,
            "processor": self.processor,
            "inputs": self.job_parameters["inputs"],
            "outputs": self.job_parameters["outputs"],
            "job_arguments": self.job_parameters["arguments"],
        }

        if "inputs" in kwargs:
            inputs = kwargs.pop("inputs")
            for input in inputs:
                if input.startswith("input_"):
                    num = input.replace("input_", "")
                    if num.isnumeric() and int(num) > 0 and int(num) <= self.num_inputs:
                        for idx, input_parameter in enumerate(
                            self.processing_step_parameters["inputs"]
                        ):
                            if input_parameter.input_name == input:
                                destination = input_parameter.destination
                                self.processing_step_parameters["inputs"][
                                    idx
                                ] = ProcessingInput(
                                    input_name=input,
                                    source=inputs[input],
                                    destination=destination,
                                )

        if "outputs" in kwargs:
            kwargs.pop("outputs")

        if "processor" in kwargs:
            kwargs.pop("processor")

        self.processing_step_parameters.update(kwargs)

        self.processing_step = ProcessingStep(**self.processing_step_parameters)

        return self.processing_step

    def step_output(self, i):
        if self.processing_step is not None:
            return self.processing_step.properties.ProcessingOutputConfig.Outputs[
                f"output_{i}"
            ].S3Output.S3Uri
        else:
            raise Exception("Step must be crated first")

    def static_step_output(self, i):
        if self.processing_step is not None:
            return self.processing_step.arguments["ProcessingOutputConfig"]["Outputs"][
                i - 1
            ]["S3Output"]["S3Uri"]
        else:
            raise Exception("Step must be crated first")

    @property
    def step_name(self):
        if self.processing_step is not None:
            return self.processing_step.name
        else:
            raise Exception("Step must be crated first")


class ProcessingJob:
    def __init__(self, function, **kwargs):
        self.__handler = ProcessingHandler(function, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.__handler.run(*args, **kwargs)

    def create_processing_step(self, name, **kwargs):
        return self.__handler.create_processing_step(name, **kwargs)

    def step_output(self, num):
        return self.__handler.step_output(num)

    def static_step_output(self, num):
        return self.__handler.static_step_output(num)

    @property
    def step_name(self):
        return self.__handler.step_name

    @property
    def image_uri(self):
        return self.__handler.image_uri

    @property
    def processor_parameters(self):
        return self.__handler.processor_parameters

    @property
    def job_parameters(self):
        return self.__handler.job_parameters

    @property
    def processor(self):
        return self.__handler.processor

    @property
    def processing_step_parameters(self):
        return self.__handler.processing_step_parameters

    @property
    def processing_step(self):
        return self.__handler.processing_step

    @property
    def experiment_config(self):
        return self.__handler.experiment_config

    @experiment_config.setter
    def experiment_config(self, experiment_config):
        self.__handler.experiment_config = experiment_config


def sm_processing_job(**kwargs):
    def wrapper(function):
        return ProcessingJob(function, **kwargs)

    return wrapper
