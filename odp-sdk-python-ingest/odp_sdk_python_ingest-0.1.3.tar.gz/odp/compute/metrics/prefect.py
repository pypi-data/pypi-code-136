import prefect

__all__ = ["get_prefect_label_names", "get_prefect_labels"]


def get_prefect_label_names(*extra_labels):
    return [
        "flow",
        "flow_id",
        "flow_run_id",
        "task",
        "task_id",
        "task_run_id",
        *extra_labels,
    ]


def get_prefect_labels(*extra_labels):
    return [
        prefect.context["flow_name"],
        prefect.context["flow_id"],
        prefect.context["flow_run_id"],
        prefect.context["task_name"],
        prefect.context["task_id"],
        prefect.context["task_run_id"],
        *extra_labels,
    ]
