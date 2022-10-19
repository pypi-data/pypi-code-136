# Parsing every util class for redis connection
from iot_rdb.util import IotRedisBasic
from iot_rdb.util import IotRedisPublisher
from iot_rdb.util import IotRedisSubscriber
from iot_rdb.util import IotRedisPubSub


class IotRedisCommon:
    """Common variable to all containers

    This standard is for defining all PubSub clients
    in every container to be created.

    CROSS_CONNECTION_REDIS = {
        "container_name": (tuple with channels to listen),
        "container_name2": (),
        ...
    }
    """
    class CrossConnection:
        OPCUA = ("control_input")
        CONTROLLER = ("filtered_outputs", "raw_outputs")
        AUTOENCODER = ("raw_outputs")
        DB = ("filtered_outputs")
        DBDRIVER = ("filtered_outputs", "raw_outputs")
        MANAGER = ()
