from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping

from atoti_core import EMPTY_MAPPING, keyword_only_dataclass

import atoti as tt
from atoti._sources import DataSource


@keyword_only_dataclass
@dataclass(frozen=True)
class KafkaDataSource(DataSource):
    @property
    def key(self) -> str:
        return "KAFKA"

    def load_kafka_into_table(
        self,
        table: tt.Table,
        *,
        bootstrap_servers: str,
        topic: str,
        group_id: str,
        batch_duration: int,
        consumer_config: Mapping[str, str],
    ) -> None:
        """Consume a Kafka topic and stream its records in an existing table."""
        params: Dict[str, Any] = {
            "bootstrapServers": bootstrap_servers,
            "topic": topic,
            "consumerGroupId": group_id,
            "keyDeserializerClass": "org.apache.kafka.common.serialization.StringDeserializer",
            "batchDuration": batch_duration,
            "additionalParameters": consumer_config,
        }
        self.load_data_into_table(
            table.name,
            scenario_name=table.scenario,
            source_params=params,
        )


def load_kafka(
    self: tt.Table,
    bootstrap_server: str,
    topic: str,
    *,
    group_id: str,
    batch_duration: int = 1000,
    consumer_config: Mapping[str, str] = EMPTY_MAPPING,
) -> None:  # noqa: D417
    """Consume a Kafka topic and stream its records in the table.

    Note:
        This method requires the :mod:`atoti-kafka <atoti_kafka>` plugin.

    The records' key deserializer default to `StringDeserializer <https://kafka.apache.org/21/javadoc/org/apache/kafka/common/serialization/StringDeserializer.html>`__.

    The records' message must be a JSON object with columns' name as keys.

    Args:
        bootstrap_server: ``host[:port]`` that the consumer should contact to bootstrap initial cluster metadata.
        topic: Topic to subscribe to.
        group_id: The name of the consumer group to join.
        batch_duration: Milliseconds spent batching received records before publishing them to the table.
            If ``0``, received records are immediately published to the table.
            Must not be negative.
        consumer_config: Mapping containing optional parameters to set up the KafkaConsumer.
            The list of available params can be found `here <https://kafka.apache.org/10/javadoc/index.html?org/apache/kafka/clients/consumer/ConsumerConfig.html>`__.
    """
    KafkaDataSource(
        _load_data_into_table=self._java_api.load_data_into_table
    ).load_kafka_into_table(
        self,
        bootstrap_servers=bootstrap_server,
        topic=topic,
        group_id=group_id,
        batch_duration=batch_duration,
        consumer_config=consumer_config,
    )
