import os
from typing import Any
import mlflow
import pandas as pd
import json
from contextlib import suppress
import datetime as dt


class PyfuncWrapper(mlflow.pyfunc.PythonModel):
    """Reusable MLflow pyfunc wrapper"""

    def __init__(self, model):
        """Map variables from model to wrapper
        :model class: The class object of the model to be wrapped and saved in MLflow
        :figures dict: A dictionary of {'<filename>': Plotly graph object} to be logged
        for model performance visualization
        """
        self.model = model
        try:
            self.figures: dict = model.figures
        except Exception:
            self.figures = None

    def predict(self, context, model_input: dict):
        """The wrapped model class must have a `predict` method which returns a dictionary"""
        return self.model.predict(model_input)


class Umlaut:
    """A class for abstracting training and querying models in MLflow"""

    def __init__(
        self,
        folder_name: str = None,
        tracking_server: str = None,
    ):
        self.DB_USERNAME = os.environ.get("DB_USERNAME")
        self.DB_PASSWORD = os.environ.get("DB_PASSWORD")
        self.DB_HOSTNAME = os.environ.get("DB_HOSTNAME")
        self.DB_NAME = os.environ.get("DB_NAME")
        self.DB_PORT = os.environ.get("DB_PORT")
        self.UMLAUT_ARTIFACT_TABLE = os.environ.get("UMLAUT_ARTIFACT_TABLE")

        if folder_name:
            self.folder_name = folder_name
        else:
            self.folder_name = str(dt.datetime.now())

        self.artifact_location = None
        # if tracking_server:
        #     self.tracking_server = tracking_server
        # else:
        #     self.tracking_server = os.environ.get("UMLAUT_TRACKING_SERVER") or None

        # self.model = None

        # if self.tracking_server:
        #     mlflow.set_tracking_uri(
        #         f"{self.tracking_server}"
        #     )
        #     self.artifact_location = f"mlflow-artifacts:/{self.folder_name}"
        # else:
        mlflow.set_tracking_uri(
            f"postgresql+psycopg2://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOSTNAME}:{self.DB_PORT}/{self.DB_NAME}"
        )
            # self.artifact_location = (
            #     f"s3://ml-artifacts/{self.folder_name}/"
            # )

    def track_model(self, model, model_name: str = None, run_name: str = "Update", code_path: list = None):
        """Trains a new version of the initiated model and pushes it to MLflow in a new run.
        Once pushed, the model can be associated to an existing model in the MLflow UI.
        :param object model: model to be created or updated
        :param list code_path: A list of local filesystem paths to Python file dependencies (or directories containing
                        file dependencies). These files are prepended to the system path before the model is loaded.
        """
        from mlflow.tracking import MlflowClient

        self.model = model
        self.model_name = model_name
        self.run_name = run_name

        mlf_client = MlflowClient()
        experiment = mlf_client.get_experiment_by_name(f"{self.model_name}")
        try:
            experiment_id = experiment.experiment_id or mlf_client.create_experiment(
                f"{self.model_name}", artifact_location=self.artifact_location
            )
        except AttributeError:
            experiment_id = mlf_client.create_experiment(
                f"{self.model_name}", artifact_location=self.artifact_location
            )

        with mlflow.start_run(experiment_id=experiment_id, run_name=self.run_name):
            self.model = PyfuncWrapper(self.model)
            mlflow.pyfunc.log_model(
                artifact_path="model",
                python_model=self.model,
                code_path=code_path,
                registered_model_name=f"{self.model_name}",
            )

            with suppress(Exception):
                if self.model.figures:
                    """The model `figures: dict` variable is used for logging Plotly performance plots.
                    All figures must be saved as html files.
                    Format: {"<plot_name>.html": plotly.express plot}
                    """
                    for figure_name in self.model.figures:
                        figure = self.model.figures.get(figure_name)
                        mlflow.log_figure(figure, figure_name)

    def query_model(
        self,
        model_name: str = "Default",
        input_config: dict = None,
        result_keys: list = None,
        stage: str = "Production",
        nested_run: bool = False,
    ) -> Any:
        """Queries the registered model.
        :param str model_name: 
        :param dict input_config: input parameters specific to the model
        :param list result_keys: list of items to be stored in results.txt
        :param str stage: stage of the model to be queried
        :param bool nested_run: whether to include a nested model
        :return Any: the result from the model with varying type {dict, list, tuple, or pd.Dataframe}
        """
        import datetime as dt
        from mlflow.tracking import MlflowClient

        mlf_client = MlflowClient()
        experiment_id = mlf_client.get_experiment_by_name(
            f"{model_name}"
        ).experiment_id
        self.model = mlflow.pyfunc.load_model(f"models:/{model_name}/{stage}")
        with mlflow.start_run(
            experiment_id=experiment_id, run_name="Query", nested=nested_run
        ):
            result = self.model.predict(data=input_config)

            mlflow.log_params(
                {
                    "timestamp": dt.datetime.now(),
                    "input_dict": input_config,
                    "model_id": str(self.model.metadata.model_uuid),
                    "model_run_id": str(self.model.metadata.run_id),
                    "model_created": str(self.model.metadata.utc_time_created),
                }
            )

            with suppress(TypeError):
                if result_keys:
                    """Drop any keys not in result_keys"""
                    result = {k: result[k] for k in result_keys if k in result}

            try:
                log_result: dict = {}
                if isinstance(result, list):
                    log_result = {"result": result}
                elif isinstance(result, dict):
                    log_result = result
                elif isinstance(result, tuple):
                    log_result = {y: x for x, y in result}
                elif isinstance(result, pd.DataFrame):
                    log_result = result.to_json(orient="records")
                mlflow.log_text(str(log_result), "results.json")
                with suppress(AttributeError, mlflow.exceptions.MlflowException):
                    """Only log numeric metrics"""
                    mlflow.log_metrics(log_result)
            except AttributeError as e:
                mlflow.log_text(str({"Error": e}), "results.json")

        return result

    def track_dataset(
        self,
        dataset: pd.DataFrame,
        edp_location: str = None,
        initial_query: str = None,
        transformations: list = None,
        date_field: str = None,
        dataset_name: str = None,
        run_name: str = "Update",
        custom_params: dict = None,
        custom_metrics: dict = None,
    ):
        """Saves a dataset to MLflow tracking.
        :param pd.DataFrame dataset: dataset to be tracked
        :param str edp_location: the schema.table location in EDP
        :param str initial_query: the initial query used to build the dataset
        :param list transformations: a list of transformations performed on the dataset
        :param str date_field: if the dataset is in time series, used for retrieving only the latest records
        :param str dataset_name: set a custom dataset name, defaults to the same name as the experiment
        :param str run_name: set a custom run name, defaults to "Update"
        :param dict custom_params: log a dictionary of custom params {"param_name": value}
        :param dict custom_metrics: log a dictionary of custom metrics {"metric_name": value}
        """
        from mlflow.tracking import MlflowClient
        import datetime as dt

        mlf_client = MlflowClient()
        experiment = mlf_client.get_experiment_by_name(f"{self.model_name}")
        experiment_id: str = (
            experiment.experiment_id
            if experiment
            else mlf_client.create_experiment(
                self.model_name, artifact_location=self.artifact_location
            )
        )

        with mlflow.start_run(experiment_id=experiment_id, run_name=run_name):
            mlflow.log_params(
                {
                    "timestamp": dt.datetime.now(),
                    "dataset": dataset_name or self.model_name,
                    "location": edp_location or None,
                    "length": len(dataset),
                }
            )
            with suppress(Exception):
                mlflow.log_param(
                    {"latest_records": dataset[date_field].max() if date_field else None}
                )
            with suppress(Exception):
                if custom_params:
                    mlflow.log_params(custom_params)
            with suppress(Exception):
                if custom_metrics:
                    mlflow.log_metrics(custom_metrics)
            with suppress(Exception):
                mlflow.log_text(
                    dataset.to_csv(),
                    artifact_file=f"{self.model_name}_{dt.date.today()}.csv",
                )
            if date_field:
                with suppress(Exception):
                    latest = dataset[
                        dataset[date_field] >= dataset[date_field].max()
                    ].reset_index(drop=True)
                    mlflow.log_text(
                        latest.to_csv(),
                        artifact_file=f"latest_{self.model_name}_{dt.date.today()}.csv",
                    )
            if initial_query:
                with suppress(Exception):
                    mlflow.log_text(
                        initial_query, artifact_file=f"{self.model_name}_query.txt"
                    )
            if transformations:
                with suppress(Exception):
                    mlflow.log_text(
                        json.dumps(transformations),
                        artifact_file=f"{self.model_name}_transformations.json",
                    )
