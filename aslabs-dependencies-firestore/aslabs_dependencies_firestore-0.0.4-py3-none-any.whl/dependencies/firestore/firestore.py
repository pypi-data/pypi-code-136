from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from dataclasses import dataclass


@dataclass
class FirestoreClientConfig:
    sa_file: str
    project_id: str


def firestore_client_factory(config: FirestoreClientConfig, client_id: str = "client") -> firestore.firestore.Client:
    json = config.sa_file
    project_id = config.project_id
    app = None
    if json:
        cred = credentials.Certificate(json)
        app = firebase_admin.initialize_app(cred, name=client_id)
    elif firebase_admin._DEFAULT_APP_NAME not in firebase_admin._apps:
        cred = credentials.ApplicationDefault()
        app = firebase_admin.initialize_app(cred, options={
            'projectId': project_id,
        })

    return firestore.client(app=app)


T = TypeVar("T")


class FirestoreClientResolver(ResolverABC):
    def __init__(self):
        self._client = None

    def __call__(self, deps: DependenciesABC) -> T:
        if self._client is None:
            self._client = firestore_client_factory(deps.get(FirestoreClientConfig))
        return self._client

    @property
    def resolved_type(self) -> Type[T]:
        return firestore.firestore.Client
