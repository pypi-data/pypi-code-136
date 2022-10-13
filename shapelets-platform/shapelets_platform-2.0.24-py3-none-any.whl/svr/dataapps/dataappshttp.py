# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
import json
from dataclasses import dataclass

from blacksheep import FromJSON, WebSocket
from blacksheep.server.controllers import ApiController, get, post, delete, ws
from requests import Session
from typing import List, Optional

from .idataappsservice import IDataAppsService
from ..docs import docs
from ..model.dataapps import DataAppProfile


@dataclass
class DataAppChangeListeners:
    ROOT_PANEL_DATA_APP = "*"
    by_app_name = {}
    listener_to_app_name = {}

    def add(self, dataapp_name: str, listener):
        listener_ws = self.by_app_name.get(dataapp_name)
        if not listener_ws:
            self.by_app_name[dataapp_name] = listener
        self.listener_to_app_name[listener] = dataapp_name

    async def notify(self, dataapp_name: str, is_delete: bool):
        change_listeners = self.by_app_name.get(dataapp_name)
        if change_listeners:
            message = f"{dataapp_name}:delete" if is_delete else dataapp_name
            sent = await self.send(message, change_listeners)
            if not sent or is_delete:
                self.remove(change_listeners)
        root_page_listeners = self.by_app_name.get(self.ROOT_PANEL_DATA_APP)
        if root_page_listeners:
            message = f"{self.ROOT_PANEL_DATA_APP}:delete" if is_delete else self.ROOT_PANEL_DATA_APP
            sent = await self.send(message, root_page_listeners)
            if not sent:
                self.remove(root_page_listeners)

    async def send(self, message: str, listener: WebSocket):
        can_notify = True
        try:
            if can_notify:
                await listener.send_text(message)
        except:
            can_notify = False
        return can_notify

    def remove(self, listener: WebSocket):
        dataapp_name = self.listener_to_app_name.get(listener)
        if dataapp_name:
            del self.listener_to_app_name[listener]
            change_listeners = self.by_app_name.get(dataapp_name)
            if change_listeners:
                del self.by_app_name[dataapp_name]


class DataAppsHttpServer(ApiController):
    def __init__(self, svr: IDataAppsService) -> None:
        self._svr = svr
        super().__init__()
        self.dataapp_change_listeners = DataAppChangeListeners()

    @classmethod
    def route(cls) -> Optional[str]:
        return '/api/dataapps'

    @ws("/ws")
    async def ws(self, websocket: WebSocket):
        await websocket.accept()
        try:
            msg = await websocket.receive_text()
            self.dataapp_change_listeners.add(msg, websocket)
            while True:
                msg = await websocket.receive_text()
        except Exception as e:
            print(e)
        finally:
            self.dataapp_change_listeners.remove(websocket)

    @get("/")
    async def dataapp_list(self) -> List[DataAppProfile]:
        return self._svr.get_all()

    @post("/")
    async def create(self, attributes: FromJSON[DataAppProfile]) -> DataAppProfile:
        dataapp_attributes = DataAppProfile(name=attributes.value.name,
                                            version=attributes.value.version,
                                            description=attributes.value.description,
                                            creationDate=attributes.value.creationDate,
                                            spec=attributes.value.spec,
                                            tags=attributes.value.tags)
        data_app = self._svr.create(dataapp_attributes)
        await self.dataapp_change_listeners.notify(dataapp_attributes.name, False)
        return data_app

    @get("/{id}")
    async def get_dataapp(self, dataAppName: str) -> DataAppProfile:
        return self._svr.get_dataapp(dataAppName)

    @delete("/")
    async def delete_all(self) -> bool:
        return self._svr.delete_all()

    @delete("/{id}")
    async def delete(self, dataAppName: str) -> bool:
        delete = self._svr.delete_dataapp(dataAppName)
        await self.dataapp_change_listeners.notify(dataAppName, True)
        return delete

    @get("/{id}/privileges")
    async def get_dataapp_privileges(self, dataapp_id: int) -> List[DataAppProfile]:
        return self._svr.get_dataapp_privileges(dataapp_id)

    @get("/{id}/versions")
    async def get_dataapp_versions(self, dataAppName: str) -> List[float]:
        return self._svr.get_dataapp_versions(dataAppName)

    @get("/{id}/lastVersion")
    async def get_dataapp_last_version(self, dataAppName: str) -> float:
        return self._svr.get_dataapp_last_version(dataAppName)

    @get("/{id}/tags")
    async def get_dataapp_tags(self, dataAppName: str) -> List[str]:
        return self._svr.get_dataapp_tags(dataAppName)


class DataAppsHttpProxy(IDataAppsService):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self) -> List[DataAppProfile]:
        return self.session.get('/api/dataapps/')

    def create(self, dataapp) -> DataAppProfile:
        payload = DataAppProfile(name=dataapp.name,
                                 version=dataapp.version,
                                 description=dataapp.description,
                                 creationDate=dataapp.creation_date,
                                 spec=dataapp.to_json(),
                                 tags=dataapp.tags)
        return self.session.post('/api/dataapps/', json=json.loads(payload.json()))

    def get_dataapp(self, dataAppName: str) -> DataAppProfile:
        return self.session.get('/api/dataapps/', params=[("dataAppName", dataAppName)])

    def delete_dataapp(self, dataAppName: str):
        self.session.delete('/api/dataapps/{id}', params=[("dataAppName", dataAppName)])

    def delete_all(self) -> bool:
        self.session.delete('/api/dataapps/')
        return True

    def get_dataapp_privileges(self, dataAppName: str) -> List[DataAppProfile]:
        pass

    def get_dataapp_versions(self, dataAppName: str) -> List[float]:
        return self.session.get('/api/{id}/versions', params=[("dataAppName", dataAppName)])

    def get_dataapp_last_version(self, dataAppName: str) -> float:
        return self.session.get('/api/{id}/lastVersion', params=[("dataAppName", dataAppName)])

    def get_dataapp_tags(self, dataAppName: str) -> List[str]:
        return self.session.get('/api/{id}/tags', params=[("dataAppName", dataAppName)])
