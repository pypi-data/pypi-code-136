import socket

from blam_sdk.sdk_config import SdkConfig
from blam_sdk.services.base_service import BlamBaseService


class ActionService(BlamBaseService):
    def __init__(self, config: SdkConfig = None):
        super().__init__("action", config)

    def get_actions(self):
        return self._get()

    def get_executions(self):
        return self._get("executions")

    def create_execution(self, action_id, asset_id="", parameters={}):
        return self._post(
            f"execute/{action_id}",
            {"asset_id": asset_id, "parameters": parameters},
        )

    def register_agent(
        self, name=socket.gethostname(), commands=[], action_ids=[]
    ):
        return self._post(
            "agents",
            {
                "name": name,
                "commands": commands,
                "action_ids": action_ids,
            },
        )

    def update_agent_capabilities(self, agent_id, commands=[], action_ids=[]):
        return self._put(
            f"agents/{agent_id}",
            {
                "commands": commands,
                "action_ids": action_ids,
            },
        )

    def create_queue(self, name):
        return self._post("queue", {"name": name})

    def queue_login(self, queue_name):
        return self._get(f"queue/{queue_name}/login")

    def update_execution_status(self, execution_id, status):
        return self._put(f"execution/{execution_id}/{status}")
