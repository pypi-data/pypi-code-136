import sagemaker_utils
from time import gmtime, strftime
from sagemaker.workflow.step_collections import RegisterModel
from sagemaker.model import Model as SM_Model
from sagemakerify import utils, globals


class Model:
    def __init__(self, Cls, **kwargs):
        self.cls = Cls
        self.session = kwargs.get("session", globals.DEFAULTS.get("session", None))

        self.default_prefix = globals.DEFAULTS.get("prefix", "sagemakerify")
        self.project = globals.DEFAULTS.get("project", self.default_prefix)
        self.default_bucket = globals.DEFAULTS.get(
            "bucket", self.session.default_bucket()
        )

        self.base_image = kwargs.get(
            "base_image", globals.DEFAULTS.get("base_image", None)
        )
        self.secret = kwargs.get("secret", globals.DEFAULTS.get("secret", None))
        self.codebuild_role = kwargs.get(
            "codebuild_role", globals.DEFAULTS.get("codebuild_role", None)
        )
        self.role = kwargs.get("role", globals.DEFAULTS.get("role", None))
        self.image_env = kwargs.get("image_env", {})
        self.data_s3_prefix = kwargs.get("data_s3_prefix", None)
        self.code_s3_prefix = kwargs.get("code_s3_prefix", None)
        self.image_s3_prefix = kwargs.get("image_s3_prefix", None)
        self.image_uri = kwargs.get("image_uri", None)
        self.libraries = kwargs.get("libraries", None)
        self.dependencies = kwargs.get("dependencies", None)
        self.image_name = kwargs.get("image_name", None)
        self.model_name = kwargs.get("model_name", None)
        self.model_data = kwargs.get("model_data", None)
        self.others = kwargs.get("others", None)

        build_image = self.image_uri is None

        self.role = utils.get_execution_role(self.role)
        if self.role is None:
            raise Exception("role is required")

        if self.model_data is None:
            raise Exception("model_data is required")

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
        self.class_name, self.class_file = utils.create_class_file(Cls)

        if self.model_name is None:
            self.model_name = f"{self.project}-{self.class_name}"

        self.model_name = f'{self.model_name}-{strftime("%d-%m-%y-%H-%M-%S", gmtime())}'
        self.model_name = self.model_name.lower().replace("_", "-")

        self.code_tar_file = sagemaker_utils.create_tar_gz(
            self.class_file,
            f"{globals.DEFAULTS.source_code_location}/{self.class_name}.tar.gz'",
        )

        # Upload code file to S3
        self.code_s3_path = sagemaker_utils.upload(
            self.code_tar_file,
            f"{self.code_s3_prefix}/{self.model_name}",
            show_progress=False,
            session=self.session.boto_session,
        )

        utils.copy_serving_files()

        if build_image:
            # Create docker image
            self.parameters = {
                "image_name": self.image_name
                if self.image_name is not None
                else self.model_name,
                "base_image": self.base_image,
                "s3_path": self.image_s3_prefix,
                "role": self.codebuild_role,
                "wait": True,
            }

            if self.libraries is not None:
                self.parameters["libraries"] = self.libraries
            else:
                self.parameters["libraries"] = []

            self.parameters["libraries"]["multi-model-server"] = "1.1.8"
            self.parameters["libraries"]["sagemaker-inference"] = "1.5.11"
            self.parameters["libraries"]["boto3"] = "1.24.2"

            if self.secret is not None:
                self.parameters["secret"] = self.secret

            if self.dependencies is not None:
                self.parameters["dependencies"] = self.dependencies
            else:
                self.parameters["dependencies"] = []

            self.parameters["dependencies"].append(
                (f"{globals.DEFAULTS.source_code_location}/serving", "/opt/ml/serving")
            )

            if self.others is not None:
                self.parameters["others"] = self.others
            else:
                self.parameters["others"] = []

            self.parameters["others"] += [
                "RUN pip install -e /opt/ml/serving",
                "LABEL com.amazonaws.sagemaker.capabilities.multi-models=true",
                "LABEL com.amazonaws.sagemaker.capabilities.accept-bind-to-port=true",
            ]

            self.parameters["entrypoint"] = [
                "python",
                "/opt/ml/serving/custom_inference/serving.py",
            ]

            self.parameters["cmd"] = ["serve"]

            hash = utils.dict_hash(self.parameters)
            if self.parameters["image_name"] not in globals.LAST_CONFIG or (
                self.parameters["image_name"] in globals.LAST_CONFIG
                and globals.LAST_CONFIG[self.parameters["image_name"]]["hash"] != hash
            ):

                self.image_uri = sagemaker_utils.create_docker_image(**self.parameters)

                globals.LAST_CONFIG[self.parameters["image_name"]] = {
                    "uri": self.image_uri,
                    "hash": hash,
                }

            else:
                self.image_uri = globals.LAST_CONFIG[self.parameters["image_name"]][
                    "uri"
                ]

        # Create model
        self.model = SM_Model(
            image_uri=self.image_uri,
            model_data=self.model_data,
            role=self.role,
            name=self.model_name,
            source_dir=self.code_s3_path,
            entry_point=self.class_file,
            sagemaker_session=self.session,
        )

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

    def create_model(self, **kwargs):
        self.model.create(**kwargs)

    def register_model(self, **kwargs):
        if "image_uri" not in kwargs:
            kwargs["image_uri"] = self.image_uri

        self.model.register(**kwargs)

    def create_register_model_step(self, name, **kwargs):
        self.register_model_step_parameters = {
            "name": name,
            "image_uri": self.image_uri,
            "entry_point": self.class_file,
        }

        self.register_model_step_parameters.update(kwargs)

        self.register_model_step = RegisterModel(**self.register_model_step_parameters)

        return self.register_model_step

    def deploy(self, **kwargs):

        if "endpoint_name" not in kwargs:
            kwargs["endpoint_name"] = self.model_name

        self.endpoint_name = kwargs["endpoint_name"]

        self.model.deploy(**kwargs)


def sm_model(**kwargs):
    def wrapper(Cls):
        return Model(Cls, **kwargs)

    return wrapper
