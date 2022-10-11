import asyncio
import logging
from abc import abstractmethod, abstractproperty
from dataclasses import dataclass, field
from timeit import default_timer
from typing import Dict, List, Optional, Type, TypeVar, Union

import faust
from aioprometheus import Counter, Service, Summary
from aioprometheus.collectors import Histogram
from betterproto import Message
from confluent_kafka.admin import AdminClient, NewTopic
from dacite import from_dict
from faust.serializers import Codec
from faust.streams import Stream
from faust.types import CodecArg
from faust.types.models import ModelT

from delphai_utils.config import get_config
from delphai_utils.patches import aiokafka_patch
from delphai_utils.utils import find_free_port

logger = logging.getLogger(__name__)

aiokafka_patch()


@dataclass
class Step:
    name: str
    partitions: int
    output: Optional[str]
    tables: Optional[List[str]] = field(default_factory=lambda: [])


T = TypeVar("T")


class FaustProtobufSerializer(Codec):
    def __init__(self, type_class: T, **kwargs):
        self.type_class = type_class
        super(FaustProtobufSerializer, self).__init__(type_class=type_class, **kwargs)

    def _loads(self, s: bytes) -> T:
        return self.type_class().from_json(s.decode("utf-8"))

    def _dumps(self, s: Message) -> bytes:
        return s.to_json().encode("utf-8")


@dataclass
class Metrics:
    inbound_counter: Optional[Counter] = None
    processed_counter: Optional[Counter] = None
    lag_timer: Optional[Summary] = None


class FaustAgent:
    step: str
    step_config: Step
    agent_id: str
    input_topic: faust.TopicT
    output_topic: faust.TopicT
    input_value_type: Type[ModelT]
    output_value_type: Type[ModelT]
    input_value_serializer: CodecArg
    output_value_serializer: CodecArg
    agent: faust.Agent
    metrics: Metrics
    metrics_server: Service

    def setup_metrics(self):
        self.metrics = Metrics()
        name = self.agent_id.replace(".", "_").replace("-", "_")
        self.metrics.inbound_counter = Counter(
            f"delphai_{name}_inbound_counter",
            "incoming requests",
            const_labels={
                "step": self.step,
                "pipeline": self.agent.app.conf.id,
            },
        )
        self.metrics.processed_counter = Counter(
            f"delphai_{name}_processed_counter",
            "processed requests",
            const_labels={
                "step": self.step,
                "pipeline": self.agent.app.conf.id,
            },
        )
        self.metrics.lag_timer = Histogram(
            f"delphai_{name}_lag_timer",
            "time to process requests",
            const_labels={
                "step": self.step,
                "pipeline": self.agent.app.conf.id,
            },
        )
        self.metrics_server.register(self.metrics.inbound_counter)
        self.metrics_server.register(self.metrics.processed_counter)
        self.metrics_server.register(self.metrics.lag_timer)

    @abstractproperty
    def step(self) -> str:
        pass

    @abstractproperty
    def input_value_type(self) -> Type[ModelT]:
        pass

    @abstractproperty
    def output_value_type(self) -> Type[ModelT]:
        pass

    @abstractproperty
    def input_value_serializer(self) -> CodecArg:
        pass

    @abstractproperty
    def output_value_serializer(self) -> CodecArg:
        pass

    @abstractmethod
    async def process(self, requests: Stream[Type[ModelT]]):
        pass

    async def on_start(self):
        logger.info(f"started agent {self.agent_id}")

    async def after_attach(self):
        pass

    def start_measure(self, labels: Dict[str, str] = {}):
        start = default_timer()
        self.metrics.inbound_counter.inc(labels)
        return start

    def end_measure(self, start: float, labels: Dict[str, str] = {}):
        end = default_timer()
        self.metrics.lag_timer.add(labels, end - start)
        self.metrics.processed_counter.inc(labels)


class FaustApp:
    app: faust.App
    worker: faust.Worker
    faust_config: Dict
    metrics: Service = Service()
    pipeline_name: str

    async def on_startup_finished(self):
        logger.info(f"started app {self.app._conf.id}")

    async def on_start(self):
        logger.info(f"starting app {self.app._conf.id}")

    async def on_shutdown(self):
        logger.info(f"shutting down {self.app._conf.id}")

    def __init__(
        self, pipeline_name: str, broker: str, step: Union[str, None] = None
    ) -> None:
        self.pipeline_name = pipeline_name
        app_id = self.pipeline_name if step is None else f"{self.pipeline_name}.{step}"
        try:
            faust_config = get_config("faust")
            if faust_config is None:
                self.faust_config = {}
            else:
                self.faust_config = faust_config.get("default", {})
                if step:
                    self.faust_config.update(faust_config.get(step, {}))
        except Exception:
            pass
        self.app = faust.App(
            id=app_id, broker=broker, web_enabled=False, **self.faust_config
        )
        loop = asyncio.get_event_loop()

        self.worker = faust.Worker(
            self.app,
            loop=loop,
            override_logging=False,
        )
        self.worker.on_startup_finished = self.on_startup_finished
        self.worker.on_start = self.on_start
        self.worker.on_shutdown = self.on_shutdown

    def start(self, agents: List[FaustAgent]):
        try:
            broker = str(self.app._conf.broker[0])
            steps = list(map(lambda s: s["name"], get_config("steps")))
            for step in steps:
                self.create_topic(broker, step)
            tasks = []
            for agent in agents:
                tasks.append(self.attach(agent))
            metrics_port = find_free_port(9191)
            asyncio.get_event_loop().create_task(self.metrics.start(port=metrics_port))
            logger.info(f"started metrics server on port {metrics_port}")
            self.worker.loop.run_until_complete(asyncio.gather(*tasks))
            self.worker.execute_from_commandline()
        except KeyboardInterrupt:
            logger.info("keyboard interrupt received")

    def get_step_config(self, step: str) -> Step:
        step_config = next((s for s in get_config("steps") if s["name"] == step), None)
        return from_dict(data_class=Step, data=step_config)

    def create_topic(self, broker: str, step: str):
        step_config = self.get_step_config(step)
        client = AdminClient({"bootstrap.servers": broker.replace("kafka://", "")})
        topics = client.list_topics().topics
        topic_names = [f"{self.pipeline_name}.{step_config.name}"]
        for table in step_config.tables:
            table_topic_name = f"{self.pipeline_name}-{table}-changelog"
            topic_names.append(table_topic_name)
        for topic_name in topic_names:
            if topic_name not in topics:
                logger.info(
                    f"creating topic {topic_name} with {step_config.partitions} partitions"
                )
                resp = client.create_topics(
                    [NewTopic(topic_name, step_config.partitions, replication_factor=1)]
                )
                resp[topic_name].result()
            else:
                logger.info(f"topic {topic_name} already exists")

    async def attach(self, agent: FaustAgent):
        agent.step_config = self.get_step_config(agent.step)
        agent.agent_id = f"{self.pipeline_name}.{agent.step}"
        agent.input_topic = self.app.topic(
            agent.agent_id,
            value_type=agent.input_value_type,
            value_serializer=agent.input_value_serializer,
        )
        output_topic_name = f"{self.pipeline_name}.{agent.step_config.output}"
        agent.output_topic = self.app.topic(
            output_topic_name,
            value_serializer=agent.output_value_serializer,
        )
        new_agent = self.app.agent(agent.input_topic)(agent.process)
        agent.agent = new_agent
        agent.metrics_server = self.metrics
        agent.setup_metrics()
        await agent.after_attach()
        await new_agent.start()
