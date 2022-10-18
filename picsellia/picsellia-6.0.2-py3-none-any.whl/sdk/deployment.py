import base64
import logging
import mimetypes
import warnings
from functools import partial
from typing import List, Optional

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning
from picsellia_connexion_services import JwtServiceConnexion

from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.exceptions import ImpossibleAction, NoShadowModel, PicselliaError
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.datalake import Datalake
from picsellia.sdk.dataset import DatasetVersion
from picsellia.sdk.model_version import ModelVersion
from picsellia.sdk.project import Project
from picsellia.sdk.tag import Tag
from picsellia.sdk.taggable import Taggable
from picsellia.types.enums import (
    ContinuousDeploymentPolicy,
    ContinuousTrainingTrigger,
    ContinuousTrainingType,
    ServiceMetrics,
    TagTarget,
)
from picsellia.types.schemas import DeploymentSchema
from picsellia.types.schemas_prediction import PredictionFormat

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Deployment(Dao, Taggable):
    def __init__(self, connexion: Connexion, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.DEPLOYMENT)

        deployment = self.refresh(data)
        if deployment.oracle_host is not None:
            try:
                self._oracle_connexion = JwtServiceConnexion(
                    deployment.oracle_host,
                    {
                        "api_token": self.connexion.api_token,
                        "deployment_id": str(self.id),
                    },
                    login_path="/api/auth/login",
                )
                if self._oracle_connexion.jwt is None:
                    raise PicselliaError("Cannot authenticate to oracle")

                logging.info(
                    f"Connected with monitoring service at {deployment.oracle_host}"
                )
            except Exception as e:
                logger.error(
                    f"Could not bind {self} with our monitoring service at {deployment.oracle_host} because : {e}"
                )
                self._oracle_connexion.session.close()
                self._oracle_connexion = None
        else:
            self._oracle_connexion = None

        if deployment.serving_host is not None:
            try:
                self._serving_connexion = JwtServiceConnexion(
                    deployment.serving_host,
                    {
                        "api_token": self.connexion.api_token,
                        "deployment_id": str(self.id),
                    },
                    login_path="/api/login",
                )
                if self._serving_connexion.jwt is None:
                    raise PicselliaError("Cannot authenticate to serving")
                logging.info(
                    f"Connected with serving service at {deployment.serving_host}"
                )
            except Exception as e:
                logger.error(
                    f"Could not bind {self} with our serving service at {deployment.serving_host} because : {e}"
                )
                self._serving_connexion.session.close()
                self._serving_connexion = None
        else:
            self._serving_connexion = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def oracle_connexion(self) -> JwtServiceConnexion:
        assert (
            self._oracle_connexion is not None
        ), "You can't use this function with this deployment. Please contact the support."
        return self._oracle_connexion

    @property
    def serving_connexion(self) -> JwtServiceConnexion:
        assert (
            self._serving_connexion is not None
        ), "You can't use this function with this deployment. Please contact the support."
        return self._serving_connexion

    def __str__(self):
        return f"{Colors.CYAN}Deployment '{self.name}' {Colors.ENDC} (id: {self.id})"

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> DeploymentSchema:
        schema = DeploymentSchema(**data)
        self._name = schema.name
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/deployment/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve the tags of your deployment.

        Examples:
            ```python
                tags = deployment.get_tags()
                assert tags[0].name == "cool"
            ```

        Returns:
            List of tags as (Tag)
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def retrieve_information(self) -> dict:
        """Retrieve some information about this deployment from service.

        Examples:
            ```python
                print(my_deployment.retrieve_information())
                >>> {

                }
            ```
        """
        return self.oracle_connexion.get(path=f"/api/deployment/{self.id}").json()

    @exception_handler
    @beartype
    def update(
        self,
        name: str = None,
        active: bool = None,
        target_datalake: Datalake = None,
        min_threshold: float = None,
    ) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {}
        if name is not None:
            payload["name"] = name

        if active is not None:
            payload["active"] = active

        if min_threshold is not None:
            payload["min_threshold"] = min_threshold

        if target_datalake is not None:
            payload["target_datalake_id"] = target_datalake.id

        r = self.connexion.patch(
            f"/sdk/deployment/{self.id}", data=orjson.dumps(payload)
        ).json()
        self.refresh(r)
        logger.info(f"{self} updated")

    @exception_handler
    @beartype
    def delete(self, force_delete: bool = False) -> None:
        self.connexion.delete(
            f"/sdk/deployment/{self.id}", params={"force_delete": force_delete}
        )
        logger.info(f"{self} deleted.")

    @exception_handler
    @beartype
    def set_model(self, model_version: ModelVersion) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {"model_version_id": model_version.id}

        self.connexion.post(
            f"/sdk/deployment/{self.id}/model", data=orjson.dumps(payload)
        ).json()
        logger.info(f"{self} model is now {model_version}")

    @exception_handler
    @beartype
    def get_model_version(self) -> ModelVersion:
        """Retrieve currently used model version

        Examples:
            ```python
                model_version = deployment.get_model()
            ```

        Returns:
            A (Model) object
        """
        r = self.sync()

        r = self.connexion.get(f"/sdk/model/version/{r['model_version_id']}").json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def set_shadow_model(self, shadow_model_version: ModelVersion) -> None:
        """Update this deployment with a new name.

        Examples:
            ```python
                a_tag.update(name="new name")
            ```
        """
        payload = {"model_version_id": shadow_model_version.id}

        self.connexion.post(
            f"/sdk/deployment/{self.id}/shadow", data=orjson.dumps(payload)
        ).json()
        logger.info(f"{self} shadow model is now {shadow_model_version}")

    @exception_handler
    @beartype
    def get_shadow_model(self) -> ModelVersion:
        """Retrieve currently used shadow model

        Examples:
            ```python
                shadow_model = deployment.get_shadow_model()
            ```

        Returns:
            A (Model) object
        """
        r = self.sync()
        if "shadow_model_version_id" not in r or r["shadow_model_version_id"] is None:
            raise NoShadowModel("This deployment has no shadow model")

        r = self.connexion.get(
            f"/sdk/model/version/{r['shadow_model_version_id']}"
        ).json()
        return ModelVersion(self.connexion, r)

    @exception_handler
    @beartype
    def predict(self, file_path: str) -> dict:
        """Run a prediction on our Serving platform

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.predict('my-image.png')
            ```
        Arguments:
            file_path (str): path to the image to predict

        Returns:
            A (dict) with information of the prediction
        """
        with open(file_path, "rb") as file:
            files = {"media": file}
            resp = self.serving_connexion.post(
                path=f"/api/deployment/{self.id}/predict",
                files=files,
            )

            if resp.status_code != 200:
                raise PicselliaError(f"Could not predict because {resp.text}")

            return resp.json()

    @exception_handler
    @beartype
    def setup_feedback_loop(self, dataset_version: DatasetVersion) -> None:
        """Set up the Feedback Loop for a Deployment.
        This way, you will be able to attached reviewed predictions to the Dataset.
        This is a great option to increase your training set with quality data.

        Examples:
            ```python
                dataset = client.get_dataset(
                    name="my-dataset",
                    version="latest"
                )
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.setup_feedback_loop(
                    dataset
                )
            ```
        Arguments:
            dataset_version (DatasetVersion): a connected (DatasetVersion)
        """
        payload = {
            "dataset_version_id": dataset_version.id,
        }
        self.connexion.post(
            f"/sdk/deployment/{self.id}/pipeline/fl",
            data=orjson.dumps(payload),
        )
        logger.info(
            f"Feedback loop setup for {self}\nNow you will be able to add predictions\nto {dataset_version}"
        )

    @exception_handler
    @beartype
    def toggle_feedback_loop(self, active: bool) -> None:
        """Toggle the Feedback Loop for a Deployment.
        This way, you will be able to attached reviewed predictions to the updated Dataset.
        This is a great option to increase your training set with quality data.

        Examples:
            ```python
                dataset = client.get_dataset(
                    name="my-dataset",
                    version="new-version"
                )
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.toggle_feedback_loop(
                    dataset
                )
            ```
        Arguments:
            active (bool): (des)activate feedback loop
        """
        payload = {"active": active}
        self.connexion.put(
            f"/sdk/deployment/{self.id}/pipeline/fl",
            data=orjson.dumps(payload),
        )
        logger.info(
            f"Feedback loop for {self} is now {'active' if active else 'deactivated'}"
        )

    @exception_handler
    @beartype
    def setup_continuous_training(
        self,
        project: Project,
        dataset_version: DatasetVersion,
        model_version: ModelVersion,
        trigger: Optional[ContinuousTrainingTrigger] = None,
        threshold: Optional[int] = None,
        experiment_parameters: Optional[dict] = None,
        scan_config: Optional[dict] = None,
    ) -> None:
        """Initialize and activate the continuous training features of picsellia. 🥑
           A Training will be triggered using the configured Dataset
           and Model as base whenever your Deployment pipeline hit the trigger.

            There is 2 types of continuous training different:
            You can launch a continuous training via Scan configuration or via Experiment
            You need to give whether `experiment_parameters` or `scan_config` but not both
            For scan configuration: [more info](https://doc.picsellia.com/docs/initialize-a-scan).

        Examples:
            We want to set up a continuous training pipeline that will be trigger
            every 150 new predictions reviewed by your team.
            We will use the same training parameters as those used when building the first model.

            ```python
                deployment = client.get_deployment("awesome-deploy")
                project = client.get_project(name="my-project")
                dataset_version = project.get_dataset(name="my-dataset").get_version("latest")
                model_version = client.get_model(name="my-model").get_version(0)
                experiment = model_version.get_source_experiment()
                parameters = experiment.get_log('parameters')
                feedback_loop_trigger = 150
                deployment.setup_continuous_training(
                    project, dataset_version, model_version,
                    threshold=150, experiment_parameters=experiment_parameters
                )
            ```
        Arguments:
            project (Project): The project that will host your pipeline.
            dataset_version (DatasetVersion): The Dataset that will be used as training data for your training.
            model_version (ModelVersion):  The exported Model to perform transfer learning from.
            threshold (int): Number of images that need to be review to trigger the training.
            trigger (ContinuousTrainingTrigger): Type of trigger to use when there is enough reviews.
            experiment_parameters (Optional[dict], optional):  Training parameters. Defaults to None.
            scan_config (Optional[dict], optional): Scan configuration dict. Defaults to None.
        """
        payload = {
            "project_id": project.id,
            "dataset_version_id": dataset_version.id,
            "model_version_id": model_version.id,
        }

        if trigger is not None and threshold is not None:
            payload["trigger"] = trigger
            payload["threshold"] = threshold

        if experiment_parameters is not None:
            if scan_config is not None:
                raise PicselliaError(
                    "You cannot give both experiment_parameters and scan_config"
                )
            else:
                payload["training_type"] = ContinuousTrainingType.EXPERIMENT
                payload["experiment_parameters"] = experiment_parameters
        else:
            if scan_config is not None:
                payload["training_type"] = ContinuousTrainingType.SCAN
                payload["scan_config"] = scan_config
            else:
                raise PicselliaError(
                    "You need to give experiment_parameters or scan_config"
                )

        self.connexion.post(
            f"/sdk/deployment/{self.id}/pipeline/ct",
            data=orjson.dumps(payload),
        )
        logger.info(f"Continuous training setup for {self}\n")

    @exception_handler
    @beartype
    def toggle_continuous_training(self, active: bool) -> None:
        """Update your continuous training pipeline.

        Examples:
            ```python
                deployment = client.get_deployment("awesome-deploy")
                deployment.update_continuous_training(active=False)
            ```
        """
        payload = {"active": active}
        self.connexion.put(
            f"/sdk/deployment/{self.id}/pipeline/ct",
            data=orjson.dumps(payload),
        )
        logger.info(
            f"Continuous training for {self} is now {'active' if active else 'deactivated'}"
        )

    @exception_handler
    @beartype
    def setup_continuous_deployment(self, policy: ContinuousDeploymentPolicy) -> None:
        """Setup the continuous deployment for this pipeline

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.setup_continuous_deployment(ContinuousDeploymentPolicy.DEPLOY_MANUAL)
            ```
        Arguments:
            policy (ContinuousDeploymentPolicy): policy to use
        """
        payload = {"policy": policy}
        self.connexion.post(
            f"/sdk/deployment/{self.id}/pipeline/cd",
            data=orjson.dumps(payload),
        )
        logger.info(f"Continuous deployment setup for {self} with policy {policy}\n")

    @exception_handler
    @beartype
    def toggle_continuous_deployment(self, active: bool) -> None:
        """Toggle continuous deployment for this deployment

        Examples:
            ```python
                deployment = client.get_deployment(
                    name="awesome-deploy"
                )
                deployment.toggle_continuous_deployment(
                    dataset
                )
            ```
        Arguments:
            active (bool): (des)activate continuous deployment
        """
        payload = {"active": active}
        self.connexion.put(
            f"/sdk/deployment/{self.id}/pipeline/cd",
            data=orjson.dumps(payload),
        )
        logger.info(
            f"Continuous deployment for {self} is now {'active' if active else 'deactivated'}"
        )

    @exception_handler
    @beartype
    def get_stats(
        self,
        service: ServiceMetrics,
        model_version: ModelVersion = None,
        from_timestamp: float = None,
        to_timestamp: float = None,
        since: int = None,
        includes: List[str] = None,
        excludes: List[str] = None,
        tags: List[str] = None,
    ) -> dict:
        """Retrieve stats of this deployment stored in Picsellia environment.

        Mandatory param is "service" an enum of type ServiceMetrics. Values possibles are :
            PREDICTIONS_OUTLYING_SCORE
            PREDICTIONS_DATA
            REVIEWS_OBJECT_DETECTION_STATS
            REVIEWS_CLASSIFICATION_STATS
            REVIEWS_LABEL_DISTRIBUTION_STATS

            AGGREGATED_LABEL_DISTRIBUTION
            AGGREGATED_OBJECT_DETECTION_STATS
            AGGREGATED_PREDICTIONS_DATA
            AGGREGATED_DRIFTING_PREDICTIONS

        For aggregation, computation may not have been done by the past.
        You will need to force computation of these aggregations and retrieve them again.


        Examples:
            ```python
                my_deployment.get_stats(ServiceMetrics.PREDICTIONS_DATA)
                my_deployment.get_stats(ServiceMetrics.AGGREGATED_DRIFTING_PREDICTIONS, since=3600)
                my_deployment.get_stats(ServiceMetrics.AGGREGATED_LABEL_DISTRIBUTION, model_id=1239012)

            ```
        Arguments:
            service (str): service queried
            model_version (ModelVersion, optional): Model that shall be used when retrieving data.
                Defaults to None.
            from_timestamp (float, optional): System will only retrieve prediction data after this timestamp.
                Defaults to None.
            to_timestamp (float, optional): System will only retrieve prediction data before this timestamp.
                Defaults to None.
            since (int, optional): System will only retrieve prediction data that are in the last seconds.
                Defaults to None.
            includes (List[str], optional): Research will include these ids and excludes others.
                Defaults to None.
            excludes (List[str], optional): Research will exclude these ids.
                Defaults to None.
            tags (List[str], optional): Research will be done filtering by tags.
                Defaults to None.

        Returns:
            A dict with queried statistics about the service you asked
        """
        query_filter = self._build_filter(
            service=service.service,
            model_version=model_version,
            from_timestamp=from_timestamp,
            to_timestamp=to_timestamp,
            since=since,
            includes=includes,
            excludes=excludes,
            tags=tags,
        )

        if service.is_aggregation:
            resp = self.oracle_connexion.get(
                path=f"/api/deployment/{self.id}/stats", params=query_filter
            ).json()
            if "infos" in resp and "info" in resp["infos"]:
                logger.info("This computation is outdated or has never been done.")
                logger.info(
                    "You can compute it again by calling launch_computation with exactly the same params."
                )
            return resp
        else:
            return self.oracle_connexion.get(
                path=f"/api/deployment/{self.id}/predictions/stats",
                params=query_filter,
            ).json()

    @staticmethod
    def _build_filter(
        service: str,
        model_version: ModelVersion = None,
        from_timestamp: float = None,
        to_timestamp: float = None,
        since: int = None,
        includes: List[str] = None,
        excludes: List[str] = None,
        tags: List[str] = None,
    ) -> dict:

        query_filter = {"service": service}

        if model_version is not None:
            query_filter["model_id"] = model_version.id

        if from_timestamp is not None:
            query_filter["from_timestamp"] = from_timestamp

        if to_timestamp is not None:
            query_filter["to_timestamp"] = to_timestamp

        if since is not None:
            query_filter["since"] = since

        if includes is not None:
            query_filter["includes"] = includes

        if excludes is not None:
            query_filter["excludes"] = excludes

        if tags is not None:
            query_filter["tags"] = tags

        return query_filter

    @exception_handler
    @beartype
    def monitor(
        self,
        image_path: str,
        latency: float,
        height: int,
        width: int,
        prediction: PredictionFormat,
        source: str = None,
        tags: List[str] = None,
        timestamp: float = None,
        model_version: ModelVersion = None,
        shadow_model_version: ModelVersion = None,
        shadow_latency: float = None,
        shadow_raw_predictions: PredictionFormat = None,
    ) -> dict:
        with open(image_path, "rb") as img_file:
            content_type = mimetypes.guess_type(image_path, strict=False)[0]
            if content_type is None:  # pragma: no cover
                content_type = "image/jpeg"
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
            filename = image_path.split("/")[-1]

        if model_version is None:
            model_version = self.get_model_version()

        if prediction.model_type != model_version.type:
            raise PicselliaError(
                f"Prediction shape of this type {prediction.model_type} cannot be used with this model {model_version.type}"
            )

        payload = {
            "filename": filename,
            "content_type": content_type,
            "height": height,
            "width": width,
            "image": encoded_image,
            "raw_predictions": prediction.dict(),
            "latency": latency,
            "model_type": model_version.type,
            "model": model_version.id,
        }

        if source is not None:
            payload["source"] = source

        if tags is not None:
            payload["tags"] = tags

        if timestamp is not None:
            payload["timestamp"] = timestamp

        if shadow_raw_predictions is not None:
            if shadow_model_version is None:
                shadow_model_version = self.get_shadow_model()

            if shadow_latency is None:
                raise ImpossibleAction(
                    "Shadow latency and shadow raw predictions shall be defined if you want to push a shadow result"
                )
            payload["shadow_model"] = shadow_model_version.id
            payload["shadow_latency"] = shadow_latency
            payload["shadow_raw_predictions"] = shadow_raw_predictions.dict()

        resp = self.oracle_connexion.post(
            path=f"/api/deployment/{self.id}/predictions",
            data=orjson.dumps(payload),
        )

        if resp.status_code != 201:
            raise PicselliaError(f"Something went wrong: {resp.status_code}")

        return resp.json()
