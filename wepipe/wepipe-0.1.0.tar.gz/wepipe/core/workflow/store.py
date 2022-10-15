import json
import logging
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pydantic import PrivateAttr
from sqlalchemy import Column, DateTime, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from wepipe.integrate.utils import obj_to_json
from wepipe.core.workflow.base_store import BaseStore

logger = logging.getLogger(__name__)

Base = declarative_base()  # type: Any


class ORMBase(Base):
    __abstract__ = True

    id = Column(String(100), default=lambda: str(uuid4()), primary_key=True)
    created = Column(DateTime, server_default=func.now())
    updated = Column(DateTime, server_default=func.now(), server_onupdate=func.now())


class WorkflowTable(ORMBase):
    __tablename__ = "workflow"

    config = Column(String(2000), nullable=False)
    source_state = Column(String(500), nullable=True)
    destination_state = Column(String(500), nullable=True)
    pipeline_state = Column(String(500), nullable=True)


class WorkflowStore(BaseStore):
    from wepipe.core.workflow.workflow import Workflow, WorkflowState
    _session: sessionmaker = PrivateAttr()

    def __init__(self, url: str = "sqlite:///wepipe.db", **data: Any):
        super().__init__(**data)
        engine = create_engine(url)
        ORMBase.metadata.create_all(engine)
        local_session = sessionmaker(bind=engine)
        self._session = local_session()

    def get(self, identifier: str) -> Optional[Workflow]:
        row = self._session.query(WorkflowTable).filter_by(id=identifier).all()
        return (
            None
            if row is None or len(row) == 0
            else self._convert_sql_row_to_workflow_data(row[0])
        )

    def get_all(self) -> List[Workflow]:
        rows = self._session.query(WorkflowTable).all()
        return [self._convert_sql_row_to_workflow_data(row) for row in rows]

    def get_workflow_state(self, identifier: str) -> Optional[WorkflowState]:
        row = (
            self._session.query(
                WorkflowTable.source_state,
                WorkflowTable.pipeline_state,
                WorkflowTable.destination_state,
            )
            .filter(id=identifier)
            .all()
        )

        return (
            None
            if row is None or len(row) == 0
            else self._convert_sql_row_to_workflow_state(row[0])
        )

    def get_source_state(self, identifier: str) -> Optional[Dict[str, Any]]:
        row = (
            self._session.query(WorkflowTable.source_state)
            .filter(WorkflowTable.id == identifier)
            .all()
        )
        return None if row[0].source_state is None else json.loads(row[0].source_state)

    def get_destination_state(self, identifier: str) -> Optional[Dict[str, Any]]:
        row = self._session.query(WorkflowTable.destination_state).filter(id=identifier).all()
        return None if row[0].destination_state is None else json.loads(row[0].destination_state)

    def get_pipeline_state(self, identifier: str) -> Optional[Dict[str, Any]]:
        row = self._session.query(WorkflowTable.pipeline_state).filter(id=identifier).all()
        return (
            None if row[0].pipeline_state is None else json.loads(row[0].pipeline_state)
        )

    def add_workflow(self, workflow: Workflow):
        self._session.add(
            WorkflowTable(
                id=workflow.id,
                config=obj_to_json(workflow.config),
                source_state=obj_to_json(workflow.states.source_state),
                destination_state=obj_to_json(workflow.states.destination_state),
                pipeline_state=obj_to_json(workflow.states.pipeline_state),
            )
        )
        self._commit_transaction()

    def update_workflow(self, workflow: Workflow):
        self._session.query(WorkflowTable).filter_by(id=workflow.id).update(
            {
                WorkflowTable.config: obj_to_json(workflow.config),
                WorkflowTable.source_state: obj_to_json(workflow.states.source_state),
                WorkflowTable.destination_state: obj_to_json(workflow.states.destination_state),
                WorkflowTable.pipeline_state: obj_to_json(
                    workflow.states.pipeline_state
                ),
            },
            synchronize_session=False,
        )
        self._commit_transaction()

    def update_workflow_state(self, workflow_id: str, workflow_state: WorkflowState):
        self._session.query(WorkflowTable).filter_by(id=workflow_id).update(
            {
                WorkflowTable.source_state: obj_to_json(workflow_state.source_state),
                WorkflowTable.destination_state: obj_to_json(workflow_state.destination_state),
                WorkflowTable.pipeline_state: obj_to_json(
                    workflow_state.pipeline_state
                ),
            },
            synchronize_session=False,
        )
        self._commit_transaction()

    def update_source_state(self, workflow_id: str, state: Dict[str, Any]):
        self._session.query(WorkflowTable).filter_by(id=workflow_id).update(
            {WorkflowTable.source_state: obj_to_json(state)}, synchronize_session=False
        )
        self._commit_transaction()

    def update_destination_state(self, workflow_id: str, state: Dict[str, Any]):
        self._session.query(WorkflowTable).filter_by(id=workflow_id).update(
            {WorkflowTable.destination_state: obj_to_json(state)}, synchronize_session=False
        )
        self._commit_transaction()

    def update_pipeline_state(self, workflow_id: str, state: Dict[str, Any]):
        self._session.query(WorkflowTable).filter_by(id=workflow_id).update(
            {WorkflowTable.pipeline_state: obj_to_json(state)},
            synchronize_session=False,
        )
        self._commit_transaction()

    def delete_workflow(self, id: str):
        self._session.query(WorkflowTable).filter_by(id=id).delete()
        self._commit_transaction()

    def _commit_transaction(self):
        try:
            self._session.commit()
        except Exception as ex:
            logger.error(f"Transaction rollback: {ex.__cause__}")
            # Rollback is important here otherwise self.session will be in inconsistent state and next call will fail
            self._session.rollback()
            raise ex

    @staticmethod
    def _convert_sql_row_to_workflow_state(row) -> Optional[WorkflowState]:
        from wepipe.core.workflow.workflow import WorkflowState

        if row is None:
            return None

        source_state_dict = (
            None if row.source_state is None else json.loads(row.source_state)
        )
        destination_state_dict = None if row.destination_state is None else json.loads(row.destination_state)
        pipeline_state_dict = (
            None if row.pipeline_state is None else json.loads(row.pipeline_state)
        )

        workflow_states: Optional[WorkflowState] = None
        if source_state_dict or destination_state_dict or pipeline_state_dict:
            workflow_states = WorkflowState(
                source_state=source_state_dict,
                destination_state=destination_state_dict,
                pipeline_state=pipeline_state_dict,
            )

        return workflow_states

    @staticmethod
    def _convert_sql_row_to_workflow_data(row) -> Workflow:
        from wepipe.core.workflow.workflow import WorkflowConfig, Workflow

        config_dict = json.loads(row.config)
        workflow = Workflow(
            id=row.id,
            config=WorkflowConfig(**config_dict),
            states=WorkflowStore._convert_sql_row_to_workflow_state(row),
        )
        return workflow
