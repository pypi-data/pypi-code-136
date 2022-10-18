from typing import Any, Dict

from kilroy_module_py_shared import SerializableModel


class MetricConfig(SerializableModel):
    id: str
    label: str
    group: str
    config: Dict[str, Any]


class MetricData(SerializableModel):
    metric_id: str
    dataset_id: int
    data: Dict[str, Any]
