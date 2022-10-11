import dataclasses
from datetime import datetime
from types import NoneType
from typing import Type, TypeVar

import pydantic

from chalk.features import DataFrame, Feature, Filter
from chalk.features.feature import HasOnePathObj
from chalk.features.resolver import OfflineResolver, OnlineResolver, SinkResolver
from chalk.parsed.duplicate_input_gql import (
    KafkaConsumerConfigGQL,
    UpsertDataFrameGQL,
    UpsertFeatureGQL,
    UpsertFeatureIdGQL,
    UpsertFeatureReferenceGQL,
    UpsertFeatureTimeKindGQL,
    UpsertFilterGQL,
    UpsertHasManyKindGQL,
    UpsertHasOneKindGQL,
    UpsertReferencePathComponentGQL,
    UpsertResolverGQL,
    UpsertResolverOutputGQL,
    UpsertScalarKindGQL,
    UpsertSinkResolverGQL,
    UpsertStreamResolverGQL,
)
from chalk.streams.KafkaSource import KafkaConsumerConfig
from chalk.streams.stream import StreamResolver

T = TypeVar("T")


try:
    import attrs
except ImportError:
    attrs = None


def _get_feature_id(s: Feature):
    assert s.name is not None
    assert s.namespace is not None
    return UpsertFeatureIdGQL(
        fqn=s.fqn,
        name=s.name,
        namespace=s.namespace,
    )


def _convert_df(df: Type[DataFrame]) -> UpsertDataFrameGQL:
    return UpsertDataFrameGQL(
        columns=[_get_feature_id(f) for f in df.columns],
        filters=[convert_type_to_gql(f) for f in df.filters],
    )


def _get_path_component(pc: HasOnePathObj) -> UpsertReferencePathComponentGQL:
    assert isinstance(pc.parent, Feature)
    return UpsertReferencePathComponentGQL(
        parent=_get_feature_id(pc.parent),
        child=_get_feature_id(pc.child),
        parentToChildAttributeName=pc.parent_to_child_attribute_name,
    )


def convert_type_to_gql(t: T):
    if isinstance(t, KafkaConsumerConfig):
        return KafkaConsumerConfigGQL(
            broker=list(t.broker) if isinstance(t.broker, str) else t.broker,
            topic=list(t.topic) if isinstance(t.topic, str) else t.topic,
            sslKeystoreLocation=t.ssl_keystore_location,
            clientIdPrefix=t.client_id_prefix,
            groupIdPrefix=t.group_id_prefix,
            topicMetadataRefreshIntervalMs=t.topic_metadata_refresh_interval_ms,
            securityProtocol=t.security_protocol,
        )

    if isinstance(t, StreamResolver):
        return UpsertStreamResolverGQL(
            fqn=t.fqn,
            kind="stream",
            config=convert_type_to_gql(t.source.consumer_config),
            functionDefinition=t.function_definition,
            environment=[t.environment] if isinstance(t.environment, str) else t.environment,
            doc=t.fn.__doc__,
        )

    if isinstance(t, SinkResolver):
        return UpsertSinkResolverGQL(
            fqn=t.fqn,
            functionDefinition=t.function_definition,
            inputs=[
                UpsertFeatureReferenceGQL(
                    underlying=_get_feature_id(f),
                    path=[_get_path_component(p) for p in f.path or []],
                )
                for f in t.inputs
            ],
            environment=t.environment,
            tags=t.tags,
            doc=t.doc,
            machineType=t.machine_type,
            bufferSize=t.buffer_size,
            debounce=t.debounce,
            maxDelay=t.max_delay,
            upsert=t.upsert,
        )

    if isinstance(t, (OnlineResolver, OfflineResolver)):
        assert isinstance(
            t.cron, (NoneType, (NoneType, str))
        ), f"Only supporting cron as a string right now for {t.fqn}"

        return UpsertResolverGQL(
            fqn=t.fqn,
            kind="offline" if isinstance(t, OfflineResolver) else "online",
            functionDefinition=t.function_definition,
            inputs=[
                UpsertFeatureReferenceGQL(
                    underlying=_get_feature_id(f),
                    path=[_get_path_component(p) for p in f.path or []],
                )
                for f in t.inputs
            ],
            output=UpsertResolverOutputGQL(
                features=[
                    _get_feature_id(f)
                    for f in t.output.features
                    if not isinstance(f, type) or not issubclass(f, DataFrame)
                ],
                dataframes=[
                    _convert_df(f) for f in t.output.features if isinstance(f, type) and issubclass(f, DataFrame)
                ],
            ),
            environment=t.environment,
            tags=t.tags,
            doc=t.doc,
            cron=t.cron,
            machineType=t.machine_type,
        )

    if isinstance(t, Feature):
        assert t.name is not None
        assert t.namespace is not None
        scalar_kind_gql = None
        has_one_kind_gql = None
        has_many_kind_gql = None
        feature_time_kind_gql = None
        if t.is_has_one:
            has_one_kind_gql = UpsertHasOneKindGQL(join=convert_type_to_gql(t.join))
        elif t.is_has_many:
            has_many_kind_gql = UpsertHasManyKindGQL(
                join=convert_type_to_gql(t.join),
                columns=None,
                filters=None,
            )
        elif t.is_feature_time:
            assert t.typ is not None
            assert issubclass(t.typ.underlying, datetime)
            feature_time_kind_gql = UpsertFeatureTimeKindGQL()
        else:
            assert t.typ is not None
            underlying_type = t.typ.underlying
            assert isinstance(underlying_type, type)
            base_classes = [x.__name__ for x in type.mro(underlying_type)]

            # Attrs and Dataclasses don't technically have base classes
            # Pydantic calls their base class BaseModel which is way too generic for string comparison
            # For simplicity on the server-side validation, we'll come up with our own "base class" names
            if dataclasses.is_dataclass(underlying_type):
                base_classes.append("__dataclass__")
            if attrs is not None and isinstance(underlying_type, type) and attrs.has(underlying_type):
                base_classes.append("__attrs__")
            if issubclass(underlying_type, pydantic.BaseModel):
                base_classes.append("__pydantic__")

            scalar_kind_gql = UpsertScalarKindGQL(
                scalarKind=t.typ.underlying.__name__,
                primary=t.primary,
                baseClasses=base_classes,
                version=t.version,
                hasEncoderAndDecoder=t.encoder is not None and t.decoder is not None,
            )

        return UpsertFeatureGQL(
            id=UpsertFeatureIdGQL(
                fqn=t.fqn,
                name=t.name,
                namespace=t.namespace,
            ),
            maxStaleness=t.max_staleness,
            description=t.description,
            owner=t.owner,
            etlOfflineToOnline=t.etl_offline_to_online,
            tags=t.tags,
            hasOneKind=has_one_kind_gql,
            hasManyKind=has_many_kind_gql,
            scalarKind=scalar_kind_gql,
            featureTimeKind=feature_time_kind_gql,
        )

    if isinstance(t, Filter):
        return UpsertFilterGQL(
            lhs=_get_feature_id(t.lhs),
            op=t.operation,
            rhs=_get_feature_id(t.rhs),
        )

    return t
