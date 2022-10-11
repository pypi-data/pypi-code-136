import asyncio
import time
import warnings

from aiohttp import ClientConnectorError, ClientResponseError
from grpclib import GRPCError, Status
from grpclib.exceptions import StreamTerminatedError
from modal_version import __version__
from sentry_sdk import capture_exception

from modal.exception import DeprecationError
from modal_proto import api_grpc, api_pb2
from modal_utils import async_utils
from modal_utils.async_utils import TaskContext, synchronize_apis
from modal_utils.grpc_utils import (
    RETRYABLE_GRPC_STATUS_CODES,
    ChannelPool,
    retry_transient_errors,
)
from modal_utils.http_utils import http_client_with_tls

from .config import config, logger
from .exception import AuthError, ConnectionError, InvalidError, VersionError

CLIENT_CREATE_TIMEOUT = 10.1
HEARTBEAT_INTERVAL = 15.0
HEARTBEAT_TIMEOUT = 10.1


async def _http_check(url: str, timeout: float) -> str:
    # Used for sanity checking connection issues
    try:
        async with http_client_with_tls(timeout=timeout) as session:
            async with session.get(url) as resp:
                return f"HTTP status: {resp.status}"
    except ClientResponseError as exc:
        return f"HTTP status: {exc.status}"
    except ClientConnectorError as exc:
        return f"HTTP exception: {exc.os_error.__class__.__name__}"
    except Exception as exc:
        return f"HTTP exception: {exc.__class__.__name__}"


async def _grpc_exc_string(exc: GRPCError, method_name: str, server_url: str, timeout: float) -> str:
    http_status = await _http_check(server_url, timeout=timeout)
    return f"{method_name}: {exc.message} [GRPC status: {exc.status.name}, {http_status}]"


class _Client:
    _client_from_env = None
    _client_from_env_lock = None

    def __init__(
        self,
        server_url,
        client_type,
        credentials,
        version=__version__,
    ):
        self.server_url = server_url
        self.client_type = client_type
        self.credentials = credentials
        self.version = version
        self._task_context = None
        self._channel_pool = None
        self._stub = None

    @property
    def stub(self):
        if self._stub is None:
            raise ConnectionError("The client is not connected to the modal server")
        return self._stub

    async def _start(self):
        from modal_utils.server_connection import GRPCConnectionFactory

        logger.debug("Client: Starting")
        if self._stub:
            raise Exception("Client is already running")
        self._task_context = TaskContext(grace=1)
        await self._task_context.start()
        self._connection_factory = GRPCConnectionFactory(
            self.server_url,
            self.client_type,
            self.credentials,
        )
        self._channel_pool = ChannelPool(self._task_context, self._connection_factory)
        await self._channel_pool.start()
        self._stub = api_grpc.ModalClientStub(self._channel_pool)  # type: ignore
        try:
            req = api_pb2.ClientCreateRequest(
                client_type=self.client_type,
                version=self.version,
            )
            resp = await retry_transient_errors(self.stub.ClientCreate, req, timeout=CLIENT_CREATE_TIMEOUT)
            if resp.deprecation_warning:
                ALARM_EMOJI = chr(0x1F6A8)
                warnings.warn(f"{ALARM_EMOJI} {resp.deprecation_warning} {ALARM_EMOJI}", DeprecationError)
            self._client_id = resp.client_id
        except GRPCError as exc:
            if exc.status == Status.FAILED_PRECONDITION:
                # TODO: include a link to the latest package
                raise VersionError(
                    f"The client version {self.version} is too old. Please update to the latest package."
                )
            elif exc.status == Status.UNAUTHENTICATED:
                raise AuthError(exc.message)
            else:
                exc_string = await _grpc_exc_string(exc, "ClientCreate", self.server_url, CLIENT_CREATE_TIMEOUT)
                raise ConnectionError(exc_string)
        except (OSError, asyncio.TimeoutError) as exc:
            raise ConnectionError(str(exc))
        if not self._client_id:
            raise InvalidError("Did not get a client id from server")

        # Start heartbeats
        self._last_heartbeat = time.time()
        self._task_context.infinite_loop(self._heartbeat, sleep=HEARTBEAT_INTERVAL)

        logger.debug("Client: Done starting")

    async def _stop(self):
        # TODO: we should trigger this using an exit handler
        logger.debug("Client: Shutting down")
        self._stub = None  # prevent any additional calls
        if self._task_context:
            await self._task_context.stop()
            self._task_context = None
        if self._channel_pool:
            self._channel_pool.close()
            self._channel_pool = None
        logger.debug("Client: Done shutting down")
        # Needed to catch straggling CancelledErrors and GeneratorExits that propagate
        # through our chains of async generators.
        await asyncio.sleep(0.01)

    async def _heartbeat(self):
        if self._stub is not None:
            req = api_pb2.ClientHeartbeatRequest(client_id=self._client_id, num_connections=self._channel_pool.size())
            try:
                await self.stub.ClientHeartbeat(req, timeout=HEARTBEAT_TIMEOUT)
                self._last_heartbeat = time.time()
            except asyncio.CancelledError as exc:  # Raised by grpclib when the connection is closed
                capture_exception(exc)
                logger.warning("Client heartbeat: cancelled")
                raise
            except asyncio.TimeoutError as exc:  # Raised by grpclib when the request times out
                capture_exception(exc)
                logger.warning("Client heartbeat: timeout")
            # Server terminates a connection abruptly.
            except StreamTerminatedError as exc:
                capture_exception(exc)
                logger.warning("Client heartbeat: stream terminated")
            except GRPCError as exc:
                exc_string = await _grpc_exc_string(exc, "ClientHeartbeat", self.server_url, HEARTBEAT_TIMEOUT)
                if exc.status == Status.NOT_FOUND:
                    # server has deleted this client - perform graceful shutdown
                    # can't simply await self._stop here since it recursively wait for this task as well
                    logger.warning(exc_string)
                    asyncio.ensure_future(self._stop())
                elif exc.status in RETRYABLE_GRPC_STATUS_CODES:
                    capture_exception(exc)
                    logger.warning(exc_string)
                else:
                    raise ConnectionError(exc_string)

    async def __aenter__(self):
        try:
            await self._start()
        except BaseException:
            await self._stop()
            raise
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._stop()

    async def verify(self):
        async with self:
            # Just connect and disconnect
            pass

    def _ok_to_recycle(self, override_time):
        # Used to check if a singleton client can be reused safely
        if not self._stub:
            # Client has been stopped
            return False
        elif self._last_heartbeat < override_time - (HEARTBEAT_INTERVAL + HEARTBEAT_TIMEOUT):
            # This can happen if a process goes into hibernation and then wakes up
            # (eg AWS Lambdas between requests, or closing the lid of a laptop)
            return False
        else:
            return True

    @property
    def client_id(self):
        """A unique identifier for the Client."""
        return self._client_id

    @classmethod
    async def from_env(cls, _override_config=None, _override_time=None) -> "_Client":
        if _override_config:
            # Only used for testing
            c = _override_config
        else:
            c = config

        server_url = c["server_url"]
        token_id = c["token_id"]
        token_secret = c["token_secret"]
        task_id = c["task_id"]
        task_secret = c["task_secret"]

        if task_id and task_secret:
            client_type = api_pb2.CLIENT_TYPE_CONTAINER
            credentials = (task_id, task_secret)
        elif token_id and token_secret:
            client_type = api_pb2.CLIENT_TYPE_CLIENT
            credentials = (token_id, token_secret)
        else:
            client_type = api_pb2.CLIENT_TYPE_CLIENT
            credentials = None

        if _override_time is None:
            # Only used for testing
            _override_time = time.time()

        if cls._client_from_env_lock is None:
            cls._client_from_env_lock = asyncio.Lock()

        async with cls._client_from_env_lock:
            if cls._client_from_env and cls._client_from_env._ok_to_recycle(_override_time):
                return cls._client_from_env
            else:
                client = _Client(server_url, client_type, credentials)
                await client._start()
                cls._client_from_env = client
                async_utils.on_shutdown(AioClient.stop_env_client())
                return client

    @classmethod
    def set_env_client(cls, client):
        """Just used from tests."""
        cls._client_from_env = client

    @classmethod
    async def stop_env_client(cls):
        # Only called from atexit handler and from tests
        if cls._client_from_env is not None:
            await cls._client_from_env._stop()
            cls._client_from_env = None


Client, AioClient = synchronize_apis(_Client)
