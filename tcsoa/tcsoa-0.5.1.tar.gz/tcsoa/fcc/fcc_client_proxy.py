import os
from dataclasses import dataclass
from typing import List, Optional


class FMSException(Exception):
    pass


@dataclass
class FccGetLastErrorResponse:
    return_code: int
    error_msg: str


@dataclass
class FccRegisterTicketsResponse:
    return_code: int
    ticket_uids: List[str]
    ifails: List[Optional[int]]


@dataclass
class FccUnRegisterTicketsResponse:
    return_code: int
    ifails: List[Optional[int]]


@dataclass
class FccDownloadFilesFromPlmResponse:
    return_code: int
    local_files: List[str]
    ifails: List[Optional[int]]


@dataclass
class FccDownloadRenderingFilesResponse:
    return_code: int
    results: List[str]
    ifails: List[Optional[int]]


@dataclass
class FccDownloadFilesToLocationResponse:
    return_code: int
    file_paths: List[str]
    ifails: List[Optional[int]]


@dataclass
class UploadFilesToPlmResponse:
    return_code: int
    volume_ids: List[str]
    ifails: List[Optional[int]]


@dataclass
class RollbackFilesUploadedToPlmResponse:
    return_code: int
    ifails: List[Optional[int]]


class FccClientProxy:
    def __init__(self):
        import clr
        dll_location = self._determine_dll_location()
        clr.AddReference(dll_location)
        from Teamcenter.FMS.FCCProxy.ClientCache import NetFileCacheProxy
        self.dll = NetFileCacheProxy()

    def _determine_dll_location(self) -> str:
        dll_location = None
        if 'FMS_HOME' in os.environ:
            dll_location = os.path.join(os.environ['FMS_HOME'], 'lib', 'FCCNetClientProxy4064.dll')
        if 'TCSOA_FSC_NET_DLL' in os.environ:
            dll_location = os.environ['TCSOA_FSC_NET_DLL']
        if not dll_location or not os.path.exists(dll_location):
            raise FMSException('FSC DLL could not be found! Please set either FMS_HOME or TCSOA_FSC_NET_DLL environment var!')
        return dll_location

    def fcc_set_locale(self, locale: str):
        self.dll.SetLocale(locale)

    def fcc_register_tickets(self, tickets: List[str]) -> FccRegisterTicketsResponse:
        ret_val, uids, ifails = self.dll.RegisterTickets(tickets, [], [])
        return FccRegisterTicketsResponse(0, list(uids), list(ifails))

    def fcc_unregister_tickets(self, uids: List[str]) -> FccUnRegisterTicketsResponse:
        ifails = self.dll.UnRegisterTickets(uids, [])
        return FccUnRegisterTicketsResponse(0, list(ifails))

    def fcc_download_files_from_plm(self, policy: str, uids: List[str], cb: Optional[object], client_object: Optional[object]) -> FccDownloadFilesFromPlmResponse:
        ret_val, local_files, ifails = self.dll.DownloadFilesFromPLM(policy, uids, cb, client_object, [], [])
        return FccDownloadFilesFromPlmResponse(0, list(local_files), list(ifails))

    def fcc_download_files_to_location(self, policy: str, uids: List[str], cb: Optional[object], client_object: Optional[object], target_dir: str) -> FccDownloadFilesToLocationResponse:
        ret_val, file_paths, ifails = self.dll.DownloadFilesToLocation(policy, uids, cb, client_object, target_dir, [], [])
        return FccDownloadFilesToLocationResponse(0, list(file_paths), list(ifails))

    def fcc_upload_files_to_plm(self, uids: List[str], cb: Optional[object], client_object: Optional[object], file_paths: List[str]) -> UploadFilesToPlmResponse:
        ret_val, volume_ids, ifails = self.dll.UploadFilesToPLM(uids, cb, client_object, file_paths, True, [], [])
        return UploadFilesToPlmResponse(0, list(volume_ids), list(ifails))

    def fcc_rollback_files_uploaded_to_plm(self, uids: List[str], volume_ids: List[str]) -> RollbackFilesUploadedToPlmResponse:
        ret_val, ifails = self.dll.RollbackFilesUploadedToPLM(uids, volume_ids, [])
        return RollbackFilesUploadedToPlmResponse(0, list(ifails))

    def register_tickets(self, tickets: List[str]) -> List[str]:
        if tickets is None or len(tickets) == 0:
            raise FMSException('Error -3002: ArgumentError - pass a non-empty list of tickets')
        result = self.fcc_register_tickets(tickets)
        return result.ticket_uids

    def unregister_tickets(self, uids: List[str]):
        if uids is None or len(uids) == 0:
            raise FMSException('Error -3002: ArgumentError - pass a non-empty list of UIDs')
        self.fcc_unregister_tickets(uids)

    def download_files_from_plm(self, policy: str, uids: List[str]) -> List[str]:
        if uids is None or len(uids) == 0:
            raise FMSException('Error -3002: ArgumentError - pass a non-empty list of UIDs')
        result = self.fcc_download_files_from_plm(policy, uids, None, None)
        return result.local_files

    def upload_files_to_plm(self, uids: List[str], file_paths: List[str]) -> List[str]:
        if uids is None or len(uids) == 0:
            raise FMSException('Error -3002: ArgumentError - pass a non-empty list of UIDs')
        result = self.fcc_upload_files_to_plm(uids, None, None, file_paths)
        return result.volume_ids

    def rollback_files_uploaded_to_plm(self, uids: List[str], volume_ids: List[str]):
        self.fcc_rollback_files_uploaded_to_plm(uids, volume_ids)
