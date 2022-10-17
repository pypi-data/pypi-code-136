import sagemaker_utils
from sagemakerify import utils, globals


class LambdaHandler:
    def __init__(self, function, **kwargs):

        self.function = function
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
        self.description = kwargs.pop("description", "")
        self.timeout = kwargs.pop("timeout", globals.DEFAULTS.get("timeout", 300))
        self.memory_size = kwargs.pop(
            "memory_size", globals.DEFAULTS.get("memory_size", 256)
        )
        self.role = kwargs.pop("role", globals.DEFAULTS.get("role", None))
        self.tags = kwargs.pop("tags", globals.DEFAULTS.get("tags", None))
        self.base_name = kwargs.pop("base_name", f"{self.project}").lower()
        self.image_env = kwargs.pop("image_env", {})
        self.data_s3_prefix = kwargs.pop("data_s3_prefix", None)
        self.code_s3_prefix = kwargs.pop("code_s3_prefix", None)
        self.image_s3_prefix = kwargs.pop("image_s3_prefix", None)
        self.image_uri = kwargs.pop("image_uri", None)
        self.libraries = kwargs.pop("libraries", None)
        self.dependencies = kwargs.pop("dependencies", None)
        self.image_name = kwargs.pop("image_name", None)
        self.others = kwargs.pop("others", None)
        self.cmd = kwargs.pop("cmd", None)
        self.env = kwargs.pop("env", None)
        self.kwargs = kwargs

        build_image = self.image_uri is None

        self.role = utils.get_execution_role(self.role)

        if self.role is None:
            raise Exception("role is required")

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
        ) = utils.create_function_file(
            function, directory="lambda_function", name="app"
        )

        self.prefix_name = f"{self.base_name}-{self.function_name}".lower().replace(
            "_", "-"
        )

        if build_image:
            # Create docker image
            self.parameters = {
                "image_name": self.image_name
                if self.image_name is not None
                else self.prefix_name,
                "base_image": self.base_image,
                "s3_path": self.image_s3_prefix,
                "role": self.codebuild_role,
                "wait": True,
            }

            if self.libraries is not None:
                self.parameters["libraries"] = self.libraries
            else:
                self.parameters["libraries"] = {}

            if self.secret is not None:
                self.parameters["secret"] = self.secret

            if self.dependencies is not None:
                self.parameters["dependencies"] = self.dependencies
            else:
                self.parameters["dependencies"] = []

            parts = self.function_file.split("/")
            function_directory = "/".join(parts[:-1])
            function_filename = parts[-1]

            self.parameters["dependencies"].append((function_directory, "/function"))

            if self.others is not None:
                self.parameters["others"] = self.others
            else:
                self.parameters["others"] = []

            self.parameters["others"].append("WORKDIR /function")

            if self.cmd is not None:
                self.parameters["cmd"] = self.cmd
            else:
                self.parameters["cmd"] = []

            self.parameters["entrypoint"] = ["python", "-m", "awslambdaric"]

            self.parameters["cmd"].append(f"app.{self.function_name}")

            self.parameters["others"].append(
                "RUN pip install pandas pyarrow boto3 awslambdaric"
            )

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

        self.function_params = {
            "FunctionName": self.prefix_name,
            "Role": self.role,
            "Code": {"ImageUri": self.image_uri},
            "Description": self.description,
            "Timeout": self.timeout,
            "MemorySize": self.memory_size,
            "PackageType": "Image",
        }

        if self.env != None:
            self.function_params["Environment"] = {"Variables": self.env}

        lambda_response = sagemaker_utils.create_lambda_function(**self.function_params)

        self.function_arn = lambda_response["FunctionArn"]

    def run(self, *args, **kwargs):
        self.function(*args, **kwargs)


class Lambda:
    def __init__(self, function, **kwargs):
        self.__handler = LambdaHandler(function, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.__handler.run(*args, **kwargs)

    @property
    def image_uri(self):
        return self.__handler.image_uri

    @property
    def function_parameters(self):
        return self.__handler.function_params

    @property
    def function_name(self):
        return self.__handler.function_params["FunctionName"]

    @property
    def function_arn(self):
        return self.__handler.function_arn


def custom_lambda(**kwargs):
    def wrapper(function):
        return Lambda(function, **kwargs)

    return wrapper
