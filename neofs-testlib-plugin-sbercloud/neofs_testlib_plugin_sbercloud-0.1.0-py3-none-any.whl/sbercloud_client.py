from typing import Optional

from neofs_testlib_plugin_sbercloud.sbercloud_auth_requests import SbercloudAuthRequests


class SbercloudClient:
    """Manages resources in Sbercloud via API.

    API reference:
    https://docs.sbercloud.ru/terraform/ug/topics/quickstart.html
    https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0020212668.html
    """

    def __init__(
        self,
        access_key_id: str,
        secret_key: str,
        ecs_endpoint: str,
        project_id: str,
    ) -> None:
        self.ecs_requests = SbercloudAuthRequests(
            endpoint=ecs_endpoint,
            base_path=f"/v1/{project_id}/cloudservers",
            access_key_id=access_key_id,
            secret_key=secret_key,
        )
        self.ecs_node_by_ip = {}

    def find_ecs_node_by_ip(self, ip: str) -> str:
        if ip not in self.ecs_node_by_ip:
            self.ecs_node_by_ip[ip] = self.get_ecs_node_id(ip)
        assert ip in self.ecs_node_by_ip
        return self.ecs_node_by_ip[ip]

    def get_ecs_node_id(self, ip: str) -> str:
        response = self.ecs_requests.get("/detail", {"ip": ip}).json()
        return response["servers"][0]["id"]

    def start_node(self, node_id: Optional[str] = None, node_ip: Optional[str] = None) -> None:
        data = {"os-start": {"servers": [{"id": node_id or self.find_ecs_node_by_ip(node_ip)}]}}
        self.ecs_requests.post("/action", data=data)

    def stop_node(
        self, node_id: Optional[str] = None, node_ip: Optional[str] = None, hard: bool = False
    ) -> None:
        data = {
            "os-stop": {
                "type": "HARD" if hard else "SOFT",
                "servers": [{"id": node_id or self.find_ecs_node_by_ip(node_ip)}],
            }
        }
        self.ecs_requests.post("/action", data=data)
