import logging
import threading
import time

top_logger = logging.getLogger(__name__)


class BufferingTracer(object):

    def __init__(self, freedom_api, account_id, max_objects=100, max_time=5, logger=None):
        self.freedom_api = freedom_api
        self.account_id = account_id
        self.max_objects = max_objects
        self.max_time = max_time

        self.buffer = []
        self.last_upload_time = time.time()

        self.is_shutdown = False
        self.lock = threading.Lock()
        self.worker_thread = threading.Thread(target=self.worker_loop)
        self.worker_thread.daemon = True

        if logger:
            self.logger = logger
        else:
            self.logger = top_logger

    def start(self):
        if not self.is_shutdown:
            if self.worker_thread.is_alive():
                # thread is already started, ignore
                return
            self.worker_thread.start()

    def shutdown(self):
        if self.is_shutdown:
            return

        self.is_shutdown = True
        self.worker_thread.join()

    def trace(self, data: dict):
        if 'component' not in data:
            raise ValueError('Data must contain a `component` key')

        with self.lock:
            self.buffer.append(data)

    def trace_many(self, data):
        for item in data:
            if 'component' not in item:
                raise ValueError('Data must contain a `component` key')

        with self.lock:
            self.buffer += data

    def worker_loop(self):

        while not self.is_shutdown:
            now = time.time()

            if now - self.last_upload_time >= self.max_time:
                self.drain()

            if len(self.buffer) >= self.max_objects:
                self.drain()

            time.sleep(1)

    def drain(self):
        with self.lock:
            buffer = self.buffer
            self.buffer = []

        if len(buffer) == 0:
            return

        try:
            self.freedom_api.trace(self.account_id, buffer)
        except Exception as e:
            self.logger.error("Failed to upload traces")
            time.sleep(1)
            with self.lock:
                # put the data that failed to upload back in the buffer,
                # but cap it to a max of 1000 datapoints (otherwise memory would grow unbounded)
                self.buffer = (buffer + self.buffer)[:1000]

    def __del__(self):
        self.shutdown()
