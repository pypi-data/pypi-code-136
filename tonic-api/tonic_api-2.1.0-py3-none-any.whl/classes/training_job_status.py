import re

class TrainingJobStatus:
    """Keeps track of information about the status of a training job.

    Parameters
    ----------
    job_json : dict
    """
    def __init__(self, job_json: dict):
        self.state = job_json["status"]
        self.error = job_json["errorMessages"] if "errorMessages" in job_json else None
        self.tasks = job_json["tasks"] if "tasks" in job_json else None

    def current_epoch_progress(self) -> dict:
        """If the job is currently training, returns the epoch the training job is on.
        
        Returns
        -------
        dict
        """
        epoch_metadata = {}
        if self.tasks is not None:
            epoch_task = [
                task
                for task in self.tasks
                if "Training AI Synthesizer Model" in task["action"]
            ]
            if len(epoch_task) > 1:
                raise ValueError(
                    f"there are {len(epoch_task)} training tasks when there should be 1"
                )
            if len(epoch_task) == 1:
                task = epoch_task[0]
                epoch_metadata["model_name"] = task["action"].split()[-1]
                epoch_metadata["steps_completed"] = str(task["stepsCompleted"])
                epoch_metadata["total_steps"] = str(task["totalSteps"])
                return epoch_metadata
        return None

    def describe(self):
        """Print job status."""
        print("Job status: " + self.state)
        if self.error is not None:
            print('Job failed due to: "' + self.error + '"')
