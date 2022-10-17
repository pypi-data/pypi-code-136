import os
from dataclasses import dataclass
from typing import List, Dict

from tcsoa.fcc.fcc_client_proxy import FccClientProxy
from tcsoa.gen.Core._2006_03.FileManagement import GetDatasetWriteTicketsInputData, CommitDatasetFileInfo, \
    DatasetFileInfo, DatasetFileTicketInfo
from tcsoa.gen.Core.services import FileManagementService
from tcsoa.gen.Server import ServiceData


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@dataclass
class PutFileRecord:
    file_info: DatasetFileInfo
    physical_path: str
    ticket_info: DatasetFileTicketInfo = None
    volume_id: str = None


class FileManagementUtility:
    fcc_client_proxy: FccClientProxy = None

    @classmethod
    def ensure_init(cls):
        if cls.fcc_client_proxy is None:
            cls.fcc_client_proxy = FccClientProxy()

    @classmethod
    def put_files(cls, inputs: List[GetDatasetWriteTicketsInputData]):
        cls.ensure_init()
        all_partial_errors = list()
        put_file_recors = dict()
        for i in inputs:
            for dataset_info in i.datasetFileInfos:
                if dataset_info.clientId not in put_file_recors:
                    put_file_recors[dataset_info.clientId] = PutFileRecord(dataset_info, os.path.abspath(dataset_info.fileName))
                dataset_info.fileName = os.path.basename(dataset_info.fileName)
        for chunk in chunks(inputs, 100):
            get_tickets_response = FileManagementService.getDatasetWriteTickets(chunk)
            all_partial_errors.extend(get_tickets_response.serviceData.partialErrors)
            cls._process_upload_commits(get_tickets_response.commitInfo, put_file_recors)
        return all_partial_errors

    @classmethod
    def _process_upload_commits(cls, commit_infos: List[CommitDatasetFileInfo], put_file_records: Dict[str, PutFileRecord]):
        for comm_info in commit_infos:
            tickets = list()
            file_paths = list()
            for ticket_info in comm_info.datasetFileTicketInfos:
                tickets.append(ticket_info.ticket)
                put_file_info = put_file_records[ticket_info.datasetFileInfo.clientId]
                file_paths.append(put_file_info.physical_path)
            ticket_uids = cls.fcc_client_proxy.register_tickets(tickets)
            try:
                cls.fcc_client_proxy.upload_files_to_plm(ticket_uids, file_paths)
            finally:
                cls.fcc_client_proxy.unregister_tickets(ticket_uids)
        commit_sd = FileManagementService.commitDatasetFiles(commitInput=commit_infos)
        cls._rollback_failed_uploads(commit_sd, put_file_records)

    @classmethod
    def _rollback_failed_uploads(cls, commit_service_data: ServiceData, put_file_records: Dict[str, PutFileRecord]):
        if not commit_service_data.partialErrors:
            return

        failed_client_ids = set(partial_error.clientId for partial_error in commit_service_data.partialErrors)
        tickets = list()
        volume_ids = list()
        for failed_client_id in failed_client_ids:
            put_file_record = put_file_records[failed_client_id]
            tickets.append(put_file_record.ticket_info.ticket)
            volume_ids.append(put_file_record.volume_id)
        ticket_uids = cls.fcc_client_proxy.register_tickets(tickets)
        try:
            cls.fcc_client_proxy.fcc_rollback_files_uploaded_to_plm(ticket_uids, volume_ids)
        finally:
            cls.fcc_client_proxy.unregister_tickets(ticket_uids)
