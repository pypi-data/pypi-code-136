import os
from typing import Any, Dict, List, Optional, Union

from prefect.flows import Flow

from .kubernetes import Kubernetes


class KubernetesDask(Kubernetes):

    ENV_KUBERNETES_SERVICE_ACCOUNT_NAME = "KUBERNETES_SERVICE_ACCOUNT"

    def __init__(
        self,
        flow: Flow,
        namespace: Optional[str] = None,
        env: Optional[Dict[str, Union[None, str]]] = None,
        service_account_name: Optional[str] = None,
    ):
        service_account_name = service_account_name or os.environ.get(
            self.ENV_KUBERNETES_SERVICE_ACCOUNT_NAME, "prefect-dask-runner"
        )

        raise NotImplementedError("Be patient, Dask support is coming soon :)")

        super().__init__(flow, namespace, env, service_account_name)
