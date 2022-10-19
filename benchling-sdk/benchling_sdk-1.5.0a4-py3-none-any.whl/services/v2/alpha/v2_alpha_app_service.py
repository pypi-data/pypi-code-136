from typing import Iterable, List, Optional

from benchling_api_client.v2.alpha.api.apps import (
    archive_app_configuration_items,
    archive_canvases,
    bulk_create_app_configuration_items,
    bulk_update_app_configuration_items,
    create_app_configuration_item,
    create_canvas,
    get_app_configuration_item_by_id,
    get_benchling_app_manifest,
    get_canvas,
    list_app_configuration_items,
    put_benchling_app_manifest,
    unarchive_app_configuration_items,
    unarchive_canvases,
    update_app_configuration_item,
    update_canvas,
)
from benchling_api_client.v2.alpha.models.app_config_item import AppConfigItem
from benchling_api_client.v2.alpha.models.app_config_item_bulk_update import AppConfigItemBulkUpdate
from benchling_api_client.v2.alpha.models.app_config_item_create import AppConfigItemCreate
from benchling_api_client.v2.alpha.models.app_config_item_update import AppConfigItemUpdate
from benchling_api_client.v2.alpha.models.app_config_items_archival_change import AppConfigItemsArchivalChange
from benchling_api_client.v2.alpha.models.app_config_items_archive import AppConfigItemsArchive
from benchling_api_client.v2.alpha.models.app_config_items_archive_reason import AppConfigItemsArchiveReason
from benchling_api_client.v2.alpha.models.app_config_items_bulk_create_request import (
    AppConfigItemsBulkCreateRequest,
)
from benchling_api_client.v2.alpha.models.app_config_items_bulk_update_request import (
    AppConfigItemsBulkUpdateRequest,
)
from benchling_api_client.v2.alpha.models.app_config_items_unarchive import AppConfigItemsUnarchive
from benchling_api_client.v2.alpha.models.app_configuration_paginated_list import (
    AppConfigurationPaginatedList,
)
from benchling_api_client.v2.alpha.models.benchling_app_manifest import BenchlingAppManifest
from benchling_api_client.v2.alpha.models.canvas import Canvas
from benchling_api_client.v2.alpha.models.canvas_create import CanvasCreate
from benchling_api_client.v2.alpha.models.canvas_update import CanvasUpdate
from benchling_api_client.v2.alpha.models.canvases_archival_change import CanvasesArchivalChange
from benchling_api_client.v2.alpha.models.canvases_archive import CanvasesArchive
from benchling_api_client.v2.alpha.models.canvases_archive_reason import CanvasesArchiveReason
from benchling_api_client.v2.alpha.models.canvases_unarchive import CanvasesUnarchive
from benchling_api_client.v2.alpha.models.list_app_configuration_items_sort import (
    ListAppConfigurationItemsSort,
)
from benchling_api_client.v2.stable.types import Response

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.pagination_helpers import NextToken, PageIterator
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.helpers.serialization_helpers import none_as_unset, optional_array_query_param
from benchling_sdk.models import AsyncTaskLink
from benchling_sdk.services.v2.base_service import BaseService


class V2AlphaAppService(BaseService):
    """
    V2-Alpha Apps.

    Create and manage Apps on your tenant.

    https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps
    """

    @api_method
    def _list_app_configuration_items_page(
        self,
        *,
        app_id: Optional[str] = None,
        ids: Optional[Iterable[str]] = None,
        page_size: Optional[int] = 50,
        next_token: Optional[str] = None,
        modified_at: Optional[str] = None,
        sort: Optional[ListAppConfigurationItemsSort] = None,
        archive_reason: Optional[str] = None,
    ) -> Response[AppConfigurationPaginatedList]:
        return list_app_configuration_items.sync_detailed(  # type: ignore
            client=self.client,
            app_id=none_as_unset(app_id),
            ids=none_as_unset(optional_array_query_param(ids)),
            page_size=none_as_unset(page_size),
            next_token=none_as_unset(next_token),
            modified_at=none_as_unset(modified_at),
            sort=none_as_unset(sort),
            archive_reason=none_as_unset(archive_reason),
        )

    def list_app_configuration_items(
        self,
        *,
        app_id: Optional[str] = None,
        ids: Optional[Iterable[str]] = None,
        page_size: Optional[int] = 50,
        modified_at: Optional[str] = None,
        sort: Optional[ListAppConfigurationItemsSort] = None,
        archive_reason: Optional[str] = None,
        # TODO BNCH-51788 Probably need TypeVar or Union[] instead of AppConfigItem
    ) -> PageIterator[AppConfigItem]:
        """
        Get app configuration items.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/listAppConfigurationItems
        """

        def api_call(next_token: NextToken) -> Response[AppConfigurationPaginatedList]:
            return self._list_app_configuration_items_page(
                app_id=app_id,
                ids=ids,
                page_size=page_size,
                modified_at=modified_at,
                sort=sort,
                archive_reason=archive_reason,
                next_token=next_token,
            )

        def results_extractor(
            body: AppConfigurationPaginatedList,
        ) -> Optional[List[AppConfigItem]]:
            return body.app_configuration_items

        return PageIterator(api_call, results_extractor)

    @api_method
    # TODO BNCH-51788 Probably need TypeVar or Union[] instead of AppConfigItem
    def get_app_configuration_item_by_id(self, item_id: str) -> AppConfigItem:
        """
        Get app configuration.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/getAppConfigurationItemById
        """
        response = get_app_configuration_item_by_id.sync_detailed(client=self.client, item_id=item_id)
        return model_from_detailed(response)

    @api_method
    # TODO BNCH-51788 Probably need TypeVar or Union[] instead of AppConfigItem and AppConfigItemCreate
    def create_app_configuration_item(self, configuration_item: AppConfigItemCreate) -> AppConfigItem:
        """
        Create app configuration item.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/createAppConfigurationItem
        """
        response = create_app_configuration_item.sync_detailed(
            client=self.client, json_body=configuration_item
        )
        return model_from_detailed(response)

    @api_method
    def update_app_configuration_item(
        # TODO BNCH-51788 Probably need TypeVar or Union[] instead of AppConfigItemUpdate
        self,
        item_id: str,
        configuration_item: AppConfigItemUpdate
        # TODO BNCH-51788 Probably need TypeVar or Union[] instead of AppConfigItem
    ) -> AppConfigItem:
        """
        Update app configuration item.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/updateBenchlingAppConfigurationItem
        """
        # TODO BNCH-51788 Should probably be renamed update_app_configuration_item for consistency
        response = update_app_configuration_item.sync_detailed(
            client=self.client, item_id=item_id, json_body=configuration_item
        )
        return model_from_detailed(response)

    @api_method
    def archive_app_configuration_items(
        self, item_ids: Iterable[str], reason: AppConfigItemsArchiveReason
    ) -> AppConfigItemsArchivalChange:
        """
        Archive app configuration items.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/archiveAppConfigurationItems
        """
        archive_request = AppConfigItemsArchive(reason=reason, item_ids=list(item_ids))
        response = archive_app_configuration_items.sync_detailed(
            client=self.client, json_body=archive_request
        )
        return model_from_detailed(response)

    @api_method
    def unarchive_app_configuration_items(self, item_ids: Iterable[str]) -> AppConfigItemsArchivalChange:
        """
        Unarchive app configuration items.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/unarchiveAppConfigurationItems
        """
        unarchive_request = AppConfigItemsUnarchive(item_ids=list(item_ids))
        response = unarchive_app_configuration_items.sync_detailed(
            client=self.client, json_body=unarchive_request
        )
        return model_from_detailed(response)

    @api_method
    def bulk_create_app_configuration_items(self, items: Iterable[AppConfigItemCreate]) -> AsyncTaskLink:
        """
        Bulk create app configuration items.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/bulkCreateAppConfigurationItems
        """
        body = AppConfigItemsBulkCreateRequest(list(items))
        response = bulk_create_app_configuration_items.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)

    @api_method
    def bulk_update_app_configuration_items(self, items: Iterable[AppConfigItemBulkUpdate]) -> AsyncTaskLink:
        """
        Bulk update app configuration items.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/bulkUpdateAppConfigurationItems
        """
        body = AppConfigItemsBulkUpdateRequest(list(items))
        response = bulk_update_app_configuration_items.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)

    @api_method
    def get_manifest(self, app_id: str) -> BenchlingAppManifest:
        """
        Get app manifest.

        See https://benchling.com/api/v2-alpha/reference?stability=la/Apps/getBenchlingAppManifest
        """
        response = get_benchling_app_manifest.sync_detailed(client=self.client, app_id=app_id)
        return model_from_detailed(response)

    @api_method
    def update_manifest(self, app_id: str, manifest: BenchlingAppManifest) -> BenchlingAppManifest:
        """
        Update an app manifest.

        See https://benchling.com/api/v2-alpha/reference?stability=la#/Apps/putBenchlingAppManifest
        """
        response = put_benchling_app_manifest.sync_detailed(
            client=self.client, app_id=app_id, yaml_body=manifest
        )
        return model_from_detailed(response)

    @api_method
    def create_canvas(self, canvas: CanvasCreate) -> Canvas:
        """
        Create an App Canvas that a Benchling App can write to and read user interaction from.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/createCanvas
        """
        response = create_canvas.sync_detailed(
            client=self.client,
            json_body=canvas,
        )
        return model_from_detailed(response)

    @api_method
    def get_canvas(self, canvas_id: str) -> Canvas:
        """
        Get the current state of the App Canvas, including user input elements.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/getCanvas
        """
        response = get_canvas.sync_detailed(
            client=self.client,
            canvas_id=canvas_id,
        )
        return model_from_detailed(response)

    @api_method
    def update_canvas(self, canvas_id: str, canvas: CanvasUpdate) -> Canvas:
        """
        Update App Canvas.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/updateCanvas
        """
        response = update_canvas.sync_detailed(
            client=self.client,
            canvas_id=canvas_id,
            json_body=canvas,
        )
        return model_from_detailed(response)

    @api_method
    def archive_canvases(
        self, canvas_ids: Iterable[str], reason: CanvasesArchiveReason
    ) -> CanvasesArchivalChange:
        """
        Archive App Canvases.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/archiveCanvases
        """
        archive_request = CanvasesArchive(reason=reason, canvas_ids=list(canvas_ids))
        response = archive_canvases.sync_detailed(
            client=self.client,
            json_body=archive_request,
        )
        return model_from_detailed(response)

    @api_method
    def unarchive_canvases(self, canvas_ids: Iterable[str]) -> CanvasesArchivalChange:
        """
        Unarchive App Canvases.

        See https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps/unarchiveCanvases
        """
        unarchive_request = CanvasesUnarchive(canvas_ids=list(canvas_ids))
        response = unarchive_canvases.sync_detailed(client=self.client, json_body=unarchive_request)
        return model_from_detailed(response)
