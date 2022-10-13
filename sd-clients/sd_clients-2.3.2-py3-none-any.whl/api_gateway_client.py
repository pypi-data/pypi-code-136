from typing import List
from posixpath import join as urljoin
from clients_core.service_list_provider import ServiceListProvider, Service


def generate_definitions(base: str) -> List[Service]:

    adt = Service.from_service(
        {
            "name": "E360-AnalyticDatasetTools-Service",
            "endpoints": [
                {
                    "name": "AnalyticDataset",
                    "properties": {"uri": urljoin(base, "analytic-dataset-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    fs = Service.from_service(
        {
            "name": "E360-File-Service",
            "endpoints": [
                {
                    "name": "Files",
                    "properties": {"uri": urljoin(base, "file-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    fss = Service.from_service(
        {
            "name": "E360-Filestore-Service",
            "endpoints": [
                {
                    "name": "Files",
                    "properties": {"uri": urljoin(base, "file-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    ws = Service.from_service(
        {
            "name": "E360-Workspace-Service",
            "endpoints": [
                {
                    "name": "ContainerService",
                    "properties": {"uri": urljoin(base, "platform-containers-service")},
                    "version": {"major": 2, "minor": 0, "patch": 0},
                },
                {
                    "name": "AssetService",
                    "properties": {"uri": urljoin(base, "platform-assets-service")},
                    "version": {"major": 3, "minor": 0, "patch": 0},
                },
                {
                    "name": "HealthCheck",
                    "properties": {
                        "uri": urljoin(base, "platform-workspaces-healthcheck-service")
                    },
                    "version": {"major": 2, "minor": 0, "patch": 0},
                },
            ],
        }
    )
    perm = Service.from_service(
        {
            "name": "E360-Permission-Service",
            "endpoints": [
                {
                    "name": "Permissions",
                    "properties": {"uri": urljoin(base, "permissions-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    td_import = Service.from_service(
        {
            "name": "TDImportService",
            "endpoints": [
                {
                    "name": "TDBundleImport",
                    "properties": {"uri": urljoin(base, "td-bundle-import-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    card = Service.from_service(
        {
            "name": "E360-Card-Service",
            "endpoints": [
                {
                    "name": "PatientCard",
                    "properties": {"uri": urljoin(base, "card-service")},
                    "version": {"major": 1, "minor": 1, "patch": 0},
                }
            ],
        }
    )
    chart = Service.from_service(
        {
            "name": "E360-ChartImage-Service",
            "endpoints": [
                {
                    "name": "Plotly",
                    "properties": {"uri": urljoin(base, "chart-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    vis = Service.from_service(
        {
            "name": "visualization-resource-service",
            "endpoints": [
                {
                    "name": "Plotly",
                    "properties": {"uri": urljoin(base, "visualization-service")},
                    "version": {"major": 1, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    dash = Service.from_service(
        {
            "name": "E360-Dashboard-Service",
            "endpoints": [
                {
                    "name": "Dashboards",
                    "properties": {"uri": urljoin(base, "dashboard-service-v2")},
                    "version": {"major": 2, "minor": 0, "patch": 0},
                }
            ],
        }
    )
    return [adt, fs, fss, ws, perm, td_import, card, chart, vis, dash]


class ApiGatewayProvider(ServiceListProvider):
    service_url: str

    def __init__(self, service_url: str):
        self.service_url = service_url.rstrip("/")

    @property
    def source(self) -> str:
        return self.service_url

    @property
    def api_endpoint(self) -> str:
        return f"{self.source}/api"

    def get_service_list(self) -> List[Service]:
        return generate_definitions(self.api_endpoint)
