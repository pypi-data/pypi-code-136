import time
from datetime import datetime
from more_itertools import first_true
from ..services.models import ModelService
from typing import List, Optional, Tuple
from ..classes.model import Model
from ..classes.httpclient import HttpClient
from ..classes.trained_model import TrainedModel
from .training_job_status import TrainingJobStatus


class Workspace:
    """Class to represent and access a Tonic workspace.

    Parameters
    ----------
    id: str
        Workspace id.
    name: str
        Workspace name.
    models: List[Model]
        List of models in the workspace.
    client: HttpClient
        The http client to use.
    """
    def __init__(self, id: str, name: str, models: List[Model], client: HttpClient):
        self.id = id
        self.name = name
        self.models = models
        self.client = client
        self.model_service = ModelService(client)

    # this should take a model id as parameter
    def train(self, model_id: str) -> str:
        """Train a model with the current configuration for the model_id.
        """
        res = self.model_service.start_training(self.id, model_id)
        return res["id"]

    def get_trained_model_by_training_job_id(
        self, job_id: str
    ) -> Optional[TrainedModel]:
        job = self.model_service.get_job_status(job_id)
        status = TrainingJobStatus(job)
        if status.state != "Completed":
            status_messages = ["This training job is not complete."]
            self.__print_with_timestamp(status_messages)
            self.training_job_status(job_id)
        else:
            trained_model = self.model_service.get_trained_model(job_id)
            return self.__convert_to_trained_model(trained_model)

    def get_training_status_by_training_job_id(self, job_id: str) -> TrainingJobStatus:
        job = self.model_service.get_job_status(job_id)
        return TrainingJobStatus(job)
    
    def training_job_status(self, job_id: str):
        job = self.model_service.get_job_status(job_id)
        status = TrainingJobStatus(job)
        status_messages, _ = self.__handle_job_status(status, {})
        self.__print_with_timestamp(status_messages)
    
    def tail_training_job_status(self, job_id: str):
        """Print training status every ~5 seconds until the training job is done.

        Examples
        --------
        >>> training_job.tail_training_status()
        [07/06/22 15:27:50] Training status: Running your_model (905/3000 epochs completed)
        [07/06/22 15:28:00] Training status: Running your_model (906/3000 epochs completed)
        [07/06/22 15:28:16] Training status: Running your_model (907/3000 epochs completed)
        [07/06/22 15:28:32] Training status: Running your_model (908/3000 epochs completed)
        """
        status = None
        last_epoch_metadata = {}
        while status is None or status.state != "Completed":
            status = self.get_training_status_by_training_job_id(job_id)

            status_messages, last_epoch_metadata = self.__handle_job_status(
                status, last_epoch_metadata
            )

            if status.state in ["Completed", "Failed", "Canceled"]:
                break

            self.__print_with_timestamp(status_messages)

            time.sleep(5)

        # Last message(s)
        self.__print_with_timestamp(status_messages)
    
    def get_most_recent_trained_model_by_model_id(
        self, model_id: str
    ) -> Optional[TrainedModel]:
        """"Returns the most recently trained model for a given model id.
        """
        trained_model = self.model_service.get_most_recent_trained_model(model_id)
        return self.__convert_to_trained_model(trained_model)

    def get_most_recent_trained_model_old(
        self, model_id: str
    ) -> Optional[TrainedModel]:
        """"Returns the most recently trained model for a given model id.
        """
        trained_model = self.model_service.get_most_recent_trained_model_old(
            self.id, model_id
        )
        return self.__convert_to_trained_model(trained_model)

    def __convert_to_trained_model(self, model_json):
        return TrainedModel(
            model_json["modelTrainingId"],
            model_json["jobId"],
            self.id,
            Model(model_json["modelId"], model_json["model"]),
            self.client,
        )

    def __handle_epoch_updates(
        self,
        status: TrainingJobStatus,
        last_epoch_metadata: dict,
    ):
        status_messages = []
        epoch_metadata = status.current_epoch_progress()
        if epoch_metadata is not None:
            # Do not print epoch state when completed and we've never printed before
            if last_epoch_metadata == {} and status.state == "Completed":
                pass
            # Print epoch state when (not completed and we've never printed before)
            # or epoch updated
            elif last_epoch_metadata == {} or (
                epoch_metadata["steps_completed"]
                != last_epoch_metadata["steps_completed"]
            ):
                status_messages.append(
                    "Training status: Running "
                    + epoch_metadata["model_name"]
                    + " ("
                    + epoch_metadata["steps_completed"]
                    + "/"
                    + epoch_metadata["total_steps"]
                    + " epochs completed)"
                )
                last_epoch_metadata = epoch_metadata
        else:
            status_messages = [
                "Training status: Running (no training tasks reported yet)"
            ]

        return status_messages, last_epoch_metadata

    def __print_with_timestamp(self, messages):
        now = datetime.now().strftime("%D %H:%M:%S")
        for message in messages:
            print("[" + now + "] " + message)
    
    def __handle_job_status(
        self, status: TrainingJobStatus, last_epoch_metadata: dict
    ) -> Tuple[List[str], dict]:
        if status.state == "Completed":
            # Show the final epoch training status on completion
            (
                status_messages,
                last_epoch_metadata,
            ) = self.__handle_epoch_updates(status, last_epoch_metadata)
            status_messages.append("Training completed")
        elif status.state == "Failed":
            status_messages = ["Training failed: " + status.error]
        elif status.state == "Canceled":
            status_messages = ["Training was canceled by user"]
        elif status.state == "Running":
            (
                status_messages,
                last_epoch_metadata,
            ) = self.__handle_epoch_updates(status, last_epoch_metadata)
        else:
            status_messages = ["Training status: " + status.state]
        return status_messages, last_epoch_metadata

    def describe(self):
        """Print the workspace name, id, and number of models.
        
        Examples
        --------
        >>> workspace.describe()
        Workspace: your_workspace_name [b5f37f37-2665-a921-64fc-0450e64f0f51]
        Number of Models: 2
        """
        print("Workspace: " + self.name + " [" + self.id + "]")
        print("Number of Models: " + str(len(self.models)))
