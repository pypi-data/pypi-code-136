import abc
import datetime
import logging
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Type, TypeVar, Union

import marshmallow

from . import base, trace_context


try:
    import zoneinfo
except ImportError:  # Python < 3.9
    from backports import zoneinfo


__all__ = ["Event", "TraceParent", "TraceState"]


logger = logging.getLogger(__name__)


def _get_utc_now() -> datetime.datetime:
    return datetime.datetime.now(tz=zoneinfo.ZoneInfo("UTC"))


TraceParent = trace_context.TraceParent


TraceState = trace_context.TraceState


CloudEventType = TypeVar("CloudEventType", bound="CloudEvent")


class CloudEventSchema(marshmallow.Schema):
    """CloudEvent schema."""

    source = marshmallow.fields.String(required=True)

    type = marshmallow.fields.String(required=True)

    data = marshmallow.fields.Dict()

    data_content_type = marshmallow.fields.String(data_key="datacontenttype")

    data_schema = marshmallow.fields.String(data_key="dataschema")

    id = marshmallow.fields.UUID(required=True)

    spec_version = marshmallow.fields.String(
        required=True, data_key="specversion"
    )

    subject = marshmallow.fields.String()

    time = marshmallow.fields.AwareDateTime()

    trace_parent = marshmallow.fields.String(data_key="traceparent")

    trace_state = marshmallow.fields.String(data_key="tracestate")

    class Meta:
        fields = [
            "source",
            "type",
            "data",
            "data_content_type",
            "data_schema",
            "id",
            "spec_version",
            "subject",
            "time",
            "trace_parent",
            "trace_state",
        ]

    @marshmallow.post_dump
    def remove_none_values(
        self, data: Dict[str, Any], **kwargs: Any
    ) -> Dict[str, Any]:
        return {key: value for key, value in data.items() if value is not None}

    @marshmallow.post_load
    def to_trace_parent(
        self, data: Dict[str, Any], **kwargs: Any
    ) -> Dict[str, Any]:
        if "trace_parent" in data:
            data["trace_parent"] = TraceParent.from_string(
                data["trace_parent"]
            )
        return data

    @marshmallow.post_load
    def to_trace_state(
        self, data: Dict[str, Any], **kwargs: Any
    ) -> Dict[str, Any]:
        if "trace_state" in data:
            data["trace_state"] = TraceState.from_string(data["trace_state"])
        return data

    @marshmallow.post_load
    def to_utc(self, data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        if "time" in data:
            data["time"] = data["time"].astimezone(zoneinfo.ZoneInfo("UTC"))
        return data


@dataclass
class CloudEvent:
    """Partial implementation of a CloudEvent object.

    Specification doc strings adapted from https://github.com/cloudevents/spec
    (licensed under Apache License 2.0). Copyright 2018 CloudEvents Authors.
    """

    Schema = CloudEventSchema

    source: str
    """Identifies the context in which an event happened. Often this will
    include information such as the type of the event source, the organization
    publishing the event or the process that produced the event. The exact
    syntax and semantics behind the data encoded in the URI is defined by the
    event producer.

    Producers MUST ensure that source + id is unique for each distinct event.

    An application MAY assign a unique source to each distinct producer, which
    makes it easy to produce unique IDs since no other producer will have the
    same source. The application MAY use UUIDs, URNs, DNS authorities or an
    application-specific scheme to create unique source identifiers.

    A source MAY include more than one producer. In that case the producers
    MUST collaborate to ensure that source + id is unique for each distinct
    event.

    Constraints:
        REQUIRED
        MUST be a non-empty URI-reference
        An absolute URI is RECOMMENDED

    Examples
        Internet-wide unique URI with a DNS authority.
            https://github.com/cloudevents
            mailto:cncf-wg-serverless@lists.cncf.io
        Universally-unique URN with a UUID:
            urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66
        Application-specific identifiers
            /cloudevents/spec/pull/123
            /sensors/tn-1234567/alerts
            1-555-123-4567
    """

    type: str
    """This attribute contains a value describing the type of event related to
    the originating occurrence. Often this attribute is used for routing,
    observability, policy enforcement, etc. The format of this is producer
    defined and might include information such as the version of the type -
    see Versioning of Attributes in the Primer for more information.

    Constraints:
        REQUIRED
        MUST be a non-empty string
        SHOULD be prefixed with a reverse-DNS name. The prefixed domain
        dictates the organization which defines the semantics of this event
        type.

    Examples
        com.github.pull_request.opened
        com.example.object.deleted.v2
    """

    data: Optional[dict] = None
    """The event payload. This specification does not place any restriction on
    the type of this information. It is encoded into a media format which is
    specified by the datacontenttype attribute (e.g. application/json), and
    adheres to the dataschema format when those respective attributes are
    present.

    Constraints:
        OPTIONAL
    """

    data_content_type: Optional[str] = None
    """Content type of data value. This attribute enables data to carry any
    type of content, whereby format and encoding might differ from that of the
    chosen event format. For example, an event rendered using the JSON envelope
    format might carry an XML payload in data, and the consumer is informed by
    this attribute being set to "application/xml". The rules for how data
    content is rendered for different datacontenttype values are defined in the
    event format specifications; for example, the JSON event format defines the
    relationship in section 3.1.

    For some binary mode protocol bindings, this field is directly mapped to
    the respective protocol's content-type metadata property. Normative rules
    for the binary mode and the content-type metadata mapping can be found in
    the respective protocol

    In some event formats the datacontenttype attribute MAY be omitted. For
    example, if a JSON format event has no datacontenttype attribute, then it
    is implied that the data is a JSON value conforming to the
    "application/json" media type. In other words: a JSON-format event with no
    datacontenttype is exactly equivalent to one with
    datacontenttype="application/json".

    When translating an event message with no datacontenttype attribute to a
    different format or protocol binding, the target datacontenttype SHOULD be
    set explicitly to the implied datacontenttype of the source.

    Constraints:
        OPTIONAL
        If present, MUST adhere to the format specified in RFC 2046

    For Media Type examples see IANA Media Types
    """

    data_schema: Optional[str] = None
    """Identifies the schema that data adheres to. Incompatible changes to the
    schema SHOULD be reflected by a different URI. See Versioning of Attributes
    in the Primer for more information.

    Constraints:
        OPTIONAL
        If present, MUST be a non-empty URI
    """

    id: uuid.UUID = field(default_factory=uuid.uuid1)
    """Identifies the event. Producers MUST ensure that source + id is unique
    for each distinct event. If a duplicate event is re-sent (e.g. due to a
    network error) it MAY have the same id. Consumers MAY assume that Events
    with identical source and id are duplicates.

    Constraints:
        REQUIRED
        MUST be a non-empty string
        MUST be unique within the scope of the producer

    Examples:
        An event counter maintained by the producer
        A UUID
    """

    spec_version: str = "1.0"
    """The version of the CloudEvents specification which the event uses. This
    enables the interpretation of the context. Compliant event producers MUST
    use a value of 1.0 when referring to this version of the specification.

    Currently, this attribute will only have the 'major' and 'minor' version
    numbers included in it. This allows for 'patch' changes to the
    specification to be made without changing this property's value in the
    serialization. Note: for 'release candidate' releases a suffix might be
    used for testing purposes.

    Constraints:
        REQUIRED
        MUST be a non-empty string
    """

    subject: Optional[str] = None
    """This describes the subject of the event in the context of the event
    producer (identified by source). In publish-subscribe scenarios, a
    subscriber will typically subscribe to events emitted by a source, but the
    source identifier alone might not be sufficient as a qualifier for any
    specific event if the source context has internal sub-structure.

    Identifying the subject of the event in context metadata (opposed to only
    in the data payload) is particularly helpful in generic subscription
    filtering scenarios where middleware is unable to interpret the data
    content. In the above example, the subscriber might only be interested in
    blobs with names ending with '.jpg' or '.jpeg' and the subject attribute
    allows for constructing a simple and efficient string-suffix filter for
    that subset of events.

    Constraints:
        OPTIONAL
        If present, MUST be a non-empty string

    Example:
        A subscriber might register interest for when new blobs are created
        inside a blob-storage container. In this case, the event source
        identifies the subscription scope (storage container), the type
        identifies the "blob created" event, and the id uniquely identifies
        the event instance to distinguish separate occurrences of a same-named
        blob having been created; the name of the newly created blob is carried
        in subject:
            source: https://example.com/storage/tenant/container
            subject: mynewfile.jpg
    """

    time: Optional[datetime.datetime] = field(default_factory=_get_utc_now)
    """Timestamp of when the occurrence happened. If the time of the occurrence
    cannot be determined then this attribute MAY be set to some other time
    (such as the current time) by the CloudEvents producer, however all
    producers for the same source MUST be consistent in this respect. In other
    words, either they all use the actual time of the occurrence or they all
    use the same algorithm to determine the value used.

    Constraints:
        OPTIONAL
        If present, MUST adhere to the format specified in RFC 3339
    """

    trace_parent: TraceParent = field(default_factory=TraceParent)
    """Contains a version, trace ID, span ID, and trace options.

    Distributed tracing extension:
    https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/distributed-tracing.md

    Constraints:
        REQUIRED
    """  # noqa: E501

    trace_state: Optional[TraceState] = None
    """A comma-delimited list of key=value pairs.

    Distributed tracing extension:
    https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/distributed-tracing.md

    Constraints:
        OPTIONAL
    """  # noqa: E501

    _metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.data is not None and not self.data_content_type:
            self.data_content_type = "application/json"
        if self.trace_state is None:
            self.trace_state = TraceState(
                {TraceState.slugify(self.source): self.trace_parent.parent_id}
            )

    @classmethod
    def from_dict(
        class_: Type[CloudEventType],
        data: Dict[str, Any],
        *,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CloudEventType:
        instance = class_(**class_.Schema().load(data))
        instance._metadata = metadata if metadata is not None else dict()
        return instance

    @classmethod
    def from_json(
        class_: Type[CloudEventType],
        data: str,
        *,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CloudEventType:
        instance = class_(**class_.Schema().loads(data))
        instance._metadata = metadata if metadata is not None else dict()
        return instance

    def to_dict(self) -> Dict[str, Any]:
        return self.Schema().dump(self)

    def to_json(self) -> str:
        return self.Schema().dumps(self)


class EventSchema(CloudEventSchema):
    """Event schema."""

    dry_run = marshmallow.fields.Boolean(truthy=set(), data_key="dryrun")

    class Meta:
        fields = ["dry_run"] + CloudEventSchema.Meta.fields
        unknown = marshmallow.EXCLUDE


@dataclass
class SubjectURN:
    """Subject URN"""

    partition: str

    service: str = field(default="")

    region: str = field(default="")

    account: str = field(default="")

    resource: "SubjectURN.Resource" = field(
        default_factory=lambda: SubjectURN.Resource()
    )

    @dataclass
    class Resource:

        type: str = field(default="")

        id: str = field(default="")

        def __str__(self) -> str:
            return f"{self.type}/{self.id}" if self.type else f"{self.id}"

        @classmethod
        def from_string(
            class_: Type["SubjectURN.Resource"], resource: str
        ) -> "SubjectURN.Resource":
            return class_(*resource.split("/", maxsplit=1))

    def __str__(self) -> str:
        return (
            f"urn:{self.partition}:{self.service}:{self.region}:{self.account}"
            f":{self.resource}"
        )

    @classmethod
    def from_string(class_: Type["SubjectURN"], subject: str) -> "SubjectURN":
        _, partition, service, region, account, resource = subject.split(
            ":", maxsplit=5
        )
        return class_(
            partition=partition,
            service=service,
            region=region,
            account=account,
            resource=class_.Resource.from_string(resource),
        )

    def verify(
        # instance is "self" if a SubjectURN instance, but has to be explicitly
        # either a SubjectURN or Event if not
        instance: Union["SubjectURN", "Event"],
        *,
        resource_type: Optional[str] = None,
    ) -> None:
        if type(instance) is SubjectURN:
            subject_urn = instance
        elif type(instance) is Event:
            subject_urn = instance.subject_urn  # type: ignore[assignment]
        else:
            raise ValueError(
                f'Expected SubjectURN or Event, not "{type(instance)}".'
            )

        # TODO: Add verification for all parts of subject URN

        if resource_type is not None:
            if subject_urn is None:
                if type(instance) is Event and instance.subject:
                    raise ValueError(
                        f'Expected a resource type of "{resource_type}", but '
                        f"could not parse event subject urn "
                        f'"{instance.subject}".'
                    )
                else:
                    raise ValueError(
                        f'Expected a resource type of "{resource_type}", but '
                        "event subject was not set."
                    )

            elif not subject_urn.resource.type == resource_type:
                raise ValueError(
                    f'Expected a resource type of "{resource_type}", not '
                    f'"{subject_urn.resource.type}".'
                )


@dataclass
class BaseEvent(CloudEvent, base.BaseMessage, metaclass=abc.ABCMeta):
    """Base event."""

    Schema = EventSchema

    dry_run: bool = False

    @classmethod
    def from_preceding_event(
        class_,
        preceding_event: "BaseEvent",
        *,
        source: str,
        type: str,
        **kwargs: Any,
    ) -> "BaseEvent":
        kwargs.update({"source": source, "type": type})
        kwargs.setdefault("dry_run", preceding_event.dry_run)

        kwargs.setdefault(
            "trace_parent",
            TraceParent(trace_id=preceding_event.trace_parent.trace_id),
        )

        if preceding_event.trace_state:
            trace_state = TraceState(**preceding_event.trace_state)
            trace_state_source = trace_state.slugify(kwargs["source"])
            trace_state[trace_state_source] = kwargs["trace_parent"].parent_id
            kwargs.setdefault("trace_state", trace_state)

        return class_(**kwargs)

    @property
    def subject_urn(self) -> Optional[SubjectURN]:
        if self.subject is None:
            return None
        else:
            try:
                return SubjectURN.from_string(self.subject)
            except ValueError:
                return None

    @subject_urn.setter
    def subject_urn(self, subject: SubjectURN) -> None:
        self.subject = str(subject)


@dataclass
class Event(BaseEvent):
    """Event."""

    pass
