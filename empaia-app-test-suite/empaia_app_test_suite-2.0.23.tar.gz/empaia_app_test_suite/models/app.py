import json
from enum import Enum
from sqlite3 import Timestamp
from typing import Dict, List, Optional, Union

from pydantic import UUID4, BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint

ItemCount = conint(ge=0)


class AppMediaPurpose(str, Enum):
    PEEK = "peek"
    BANNER = "banner"
    WORKFLOW = "workflow"
    MANUAL = "manual"


class ListingStatus(str, Enum):
    LISTED = "LISTED"
    DELISTED = "DELISTED"
    ADMIN_DELISTED = "ADMIN_DELISTED"
    DRAFT = "DRAFT"


class AppStatus(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    DRAFT = "DRAFT"


class Language(str, Enum):
    DE = "DE"
    EN = "EN"


class RestrictedBaseModel(BaseModel):
    """Abstract Super-class not allowing unknown fields in the **kwargs."""

    class Config:
        extra = "forbid"


ConfigurationModel = Dict[StrictStr, Union[StrictStr, StrictInt, StrictFloat, StrictBool]]


class TextTranslation(RestrictedBaseModel):
    lang: Language = Field(example=Language.EN, description="Language abbreviation")
    text: str = Field(example="Some text", description="Translated tag name")


class PostAppTag(RestrictedBaseModel):
    tag_group: str = Field(example="TISSUE", description="Tag group. See definitions for valid tag groups.")
    tag_name: str = Field(example="SKIN", description="Tag name. See definitions for valid tag names.")


class AppTag(RestrictedBaseModel):
    name: str = Field(example="SKIN", description="Tag name. See definitions for valid tag names.")
    tag_translations: List[TextTranslation]


class TagList(RestrictedBaseModel):
    tissues: Optional[List[AppTag]] = Field(default=[], description="List of tissues")
    stains: Optional[List[AppTag]] = Field(default=[], description="List of stains")
    indications: Optional[List[AppTag]] = Field(default=[], description="List of indications")
    analysis: Optional[List[AppTag]] = Field(default=[], description="List of analysis")


class MediaMetadata(RestrictedBaseModel):
    caption: Optional[Dict[str, str]] = Field(
        example={"EN": "Description in english", "DE": "Beschreibung auf Deutsch"}, description="Caption"
    )
    alternative_text: Optional[Dict[str, str]] = Field(
        example={"EN": "Description in english", "DE": "Beschreibung auf Deutsch"}, description="Alternative text"
    )

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class MediaObjectCore(RestrictedBaseModel):
    index: int = Field(
        example=2, description="Number of the step, required when media purpose is 'PREVIEW', 'BANNER' or 'WORKFLOW"
    )
    caption: Optional[List[TextTranslation]] = Field(description="Media caption")
    alt_text: Optional[List[TextTranslation]] = Field(
        description="Alternative text for media",
    )
    internal_path: str = Field(example="/internal/path/to", description="Internam Minio path")
    content_type: str = Field(example="image/jpeg", description="Content type of the media object")
    presigned_media_url: Optional[str] = Field(
        example="https://url.to/image", description="Presigned url to the media object"
    )


class MediaObject(MediaObjectCore):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Media ID")


PostMediaObject = MediaObjectCore


class MediaList(RestrictedBaseModel):
    peek: List[MediaObject] = Field(default=[], description="Peek media")
    banner: List[MediaObject] = Field(default=[], description="Banner media")
    workflow: List[MediaObject] = Field(default=[], description="Workflow media")
    manual: List[MediaObject] = Field(default=[], description="Manual media")


# App UI Config

# CSP - unsafe-inline and unsafe-eval policy settings for supported *-src csp directives
class AppUiConfigSrcPolicies(RestrictedBaseModel):
    unsafe_inline: Optional[bool] = Field(
        example=True, description="Set unsafe-inline for App-UI code if set to 'true'."
    )
    unsafe_eval: Optional[bool] = Field(example=True, description="Set unsafe-eval for App-UI code if set to 'true'.")


class AppUiCspConfiguration(RestrictedBaseModel):
    script_src: Optional[AppUiConfigSrcPolicies] = Field(description="CSP script-src setting for App-UIs.")
    style_src: Optional[AppUiConfigSrcPolicies] = Field(description="CSP style-src setting for App-UIs.")
    font_src: Optional[AppUiConfigSrcPolicies] = Field(description="CSP font-src setting for App-UIs.")


class AppUiConfiguration(RestrictedBaseModel):
    csp: Optional[AppUiCspConfiguration] = Field(description="CSP settings for App-UIs.")

    # ORM mode needs to be set to true, to allow posting dictionaries as form data
    class Config:
        orm_mode = True


# App


class AppDetailsCore(RestrictedBaseModel):
    name: str = Field(example="PD-L1 Quantifier", description="Qualified app name displayed in the portal")


class PostAppDetails(AppDetailsCore):
    description: Dict[str, str] = Field(
        example={"EN": "Description in english", "DE": "Beschreibung auf Deutsch"}, description="Description"
    )


class AppDetails(AppDetailsCore):
    marketplace_url: str = Field(example="http://url.to/store", description="Url to app in the marketplace")
    description: List[TextTranslation] = Field(description="Description")


class PostApp(RestrictedBaseModel):
    ead: Optional[dict] = Field(example={}, description="EAD content of the app")
    registry_image_url: Optional[str] = Field(
        example="https://registry.gitlab.com/empaia/integration/ap_xyz",
        description="Url to the container image in the registry",
    )
    app_ui_url: Optional[str] = Field(example="http://app1.emapaia.org", description="Url where the app UI is located")
    app_ui_configuration: Optional[AppUiConfiguration] = Field(example={}, description="App UI configuration")


class PostAdminApp(PostApp):
    id: Optional[UUID4] = Field(
        default=None, example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="External ID of the app"
    )


class PublicApp(PostApp):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the app")
    version: Optional[str] = Field(example="v1.2", description="Version of the app")
    has_frontend: bool = Field(example=True, description="If true, app is shipped with a frontend")


class ClosedApp(PublicApp):
    status: AppStatus = Field(example=AppStatus.DRAFT, description="Status of the app")
    portal_app_id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app")
    creator_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Creator ID")
    created_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")
    updated_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")


# Portal App Preview


class PublicPortalAppPreview(RestrictedBaseModel):
    version: Optional[str] = Field(example="v1.2", description="Version of the currently active app")
    details: Optional[AppDetails]
    media: Optional[MediaList]
    tags: Optional[TagList]
    non_functional: Optional[bool] = Field(
        example=False,
        default=False,
        description="If true, portal app can be listed although technical app is not yet available",
    )
    created_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")
    reviewed_at: Optional[Timestamp] = Field(
        example=1598611645, description="UNIX timestamp in seconds - set by server"
    )


class ClosedPortalAppPreview(PublicPortalAppPreview):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app preview")
    portal_app_id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app")
    organization_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Organization ID")
    status: AppStatus = Field(example=AppStatus.DRAFT, descritpion="Status of the app")
    app: Optional[ClosedApp]
    creator_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the preview creator")
    review_comment: Optional[str] = Field(
        example="Review comment", description="Review commet, i.e. in case of rejection"
    )
    reviewer_id: Optional[str] = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the reviewer")


# Portal App


class PostAdminPortalApp(RestrictedBaseModel):
    id: Optional[UUID4] = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Portal App ID")
    organization_id: str = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the organization providing the portal app"
    )
    status: Optional[ListingStatus] = Field(
        example=ListingStatus.LISTED, description="Listing status of the portal app"
    )
    details: Optional[PostAppDetails]
    active_app: Optional[PostAdminApp] = Field(description="Active app for Workbench 2.0")
    active_app_legacy: Optional[PostAdminApp] = Field(description="Active app for Workbench 1.0 (legacy)")
    tags: Optional[List[PostAppTag]]
    non_functional: Optional[bool] = Field(
        example=False,
        default=False,
        description="If true, portal app can be listed although technical app is not yet available",
    )


class PortalAppCore(RestrictedBaseModel):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app")
    organization_id: str = Field(
        example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the organization providing the portal app"
    )
    status: ListingStatus = Field(example=ListingStatus.DRAFT, descritpion="Status of the app")


class PublicPortalApp(PortalAppCore, PublicPortalAppPreview):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app")


class CustomerPortalApp(PublicPortalApp):
    apps: Optional[List[str]] = Field(description="List of currently active app ids of portal app")


class ClosedPortalApp(PortalAppCore):
    id: UUID4 = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="ID of the portal app")
    active_preview: Optional[ClosedPortalAppPreview] = Field(description="Currently active portal app preview")
    active_preview_legacy: Optional[ClosedPortalAppPreview] = Field(
        description="Currently active legacy portal app preview"
    )
    creator_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="Creator ID")
    created_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")
    updated_at: Timestamp = Field(example=1598611645, description="UNIX timestamp in seconds - set by server")


class PublicPortalAppList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=123, description="Count of all available apps")
    items: List[PublicPortalApp]


class CustomerPortalAppList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=123, description="Count of all available apps")
    items: List[CustomerPortalApp]


class ClosedPortalAppList(RestrictedBaseModel):
    item_count: ItemCount = Field(example=123, description="Count of all available apps")
    items: List[ClosedPortalApp]


# Queries


class BaseQuery(RestrictedBaseModel):
    pass


class PortalAppQuery(BaseQuery):
    tissues: Optional[List[str]] = Field(example=["SKIN", "BREAST"], description="Filter option for tissue types")
    stains: Optional[List[str]] = Field(example=["HE", "PHH3"], description="Filter option for stain types")
    indications: Optional[List[str]] = Field(
        example=["MELANOMA", "PROSTATE_CANCER"], description="Filter option for indication types"
    )
    analysis: Optional[List[str]] = Field(
        example=["GRADING", "QUANTIFICATION"], description="Filter option for analysis types"
    )


class CustomerPortalAppQuery(BaseQuery):
    apps: Optional[List[str]] = Field(example=["b10648a7-340d-43fc-a2d9-4d91cc86f33f"], description="List of app IDs")


class AdminPortalAppQuery(PortalAppQuery, CustomerPortalAppQuery):
    statuses: Optional[List[AppStatus]] = Field(example=[AppStatus.DRAFT], description="Filter option for app status")
    creators: Optional[List[str]] = Field(example=["b10648a7-340d-43fc-a2d9-4d91cc86f33f"])


# App Configuratuin


class PostAppConfiguration(RestrictedBaseModel):
    content: ConfigurationModel = Field(
        example={"secret1": "value", "secret2": 100}, description="Dictionary of key-value-pairs"
    )


class AppConfiguration(PostAppConfiguration):
    app_id: str = Field(example="b10648a7-340d-43fc-a2d9-4d91cc86f33f", description="App ID")
    version: int = Field(example=1, description="Version of the vault secret")
