import os


BACKEND = os.environ.get("CLINK_BACKEND", "clink.backends.kombu")

TRANSPORT_URL = os.environ.get(
    "CLINK_TRANSPORT_URL", "amqp://guest:guest@localhost:5672//"
)
