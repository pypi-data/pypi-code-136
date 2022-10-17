from typing import Dict, Union, Optional, Tuple
from threading import Thread, Event
from subprocess import Popen, PIPE
import shlex
import logging

import requests


def check_host(host: str, port: int = 22, logger_name: str = "") -> bool:
    """Check if a given host:port combination is online

    Uses :code:`nc` process to perform the check.

    Args:
        host: name or addr of host
        port: port to check. Defaults to 22

    """
    if "@" in host:
        host = host.split("@")[1]
    if logger_name:
        logger = logging.getLogger(logger_name)
    p = Popen(shlex.split(f"nc -z -v {host} {port}"), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(timeout=1)
    output = err.decode("utf-8").lower()
    if "sent" in output and "received" in output:
        return True
    elif "no route" in output:
        return False
    elif "connection refused" in output:
        return False
    else:
        if logger_name:
            logger.error(f"Unknown output {output}")
        else:
            print(f"Unknown output {output}")
        return False


class Get:
    """A :code:`get` method with progress tracking.

    Uses :mod:`requests` as a backend. The request takes place in the background
    and can be queried with :meth:`Get.finished`.

    Example:
        get = Get()
        url = "http://some_url/files/a_file"
        another_url = "http://some_other_url/files/b_file"
        get(url, **kwargs)                 # fetches url in background
        get(another_url, **kwargs)         # fetches url in background
        while not get.finished(url):
            print(get.progress(url))       # prints progress
            time.sleep(1)

    """

    def __init__(self):
        self._init: Dict[str, str] = {}
        self._status: Dict[str, int] = {}
        self._threads: Dict[str, Thread] = {}
        self._aborted: Dict[str, Event] = {}
        self._finished: Dict[str, Event] = {}
        self._dl_bytes: Dict[str, int] = {}
        self._progress: Dict[str, Union[int, float]] = {}
        self._responses: Dict[str, requests.Response] = {}
        self._result: Dict[str, bytes] = {}

    def __call__(self, url: str, **kwargs):
        """Call :func:`requests.get` with the :code:`url` and :code:`kwargs`.

        Args:
            url: The url to fetch
            kwargs: passed to :func:`requests.get`

        """
        self._finished[url] = Event()
        self._progress[url] = 0
        self._threads[url] = Thread(target=self._call_subr, args=[url], kwargs=kwargs)
        self._aborted[url] = Event()
        self._threads[url].start()

    def _call_subr(self, url, **kwargs):
        self._init[url] = True
        content = bytearray()
        response = requests.get(url, stream=True, **kwargs)
        self._responses[url] = response
        self._status[url] = response.status_code
        if response.status_code != 200:
            self._finished[url].set()
            self._result[url] = response.content
        else:
            total = response.headers.get('content-length')
            self._dl_bytes[url] = 0
            if total is not None:           # no content length header
                total_length = int(total)
            for data in response.iter_content(chunk_size=4096):
                if not self._aborted[url].is_set():
                    content.extend(data)
                    self._dl_bytes[url] += 4096
                    if total is not None:
                        self._progress[url] = (100 * (self._dl_bytes[url] / total_length))
                    else:
                        self._progress[url] = self._dl_bytes[url] / 1024
                else:
                    break
            self._finished[url].set()
            if self._aborted[url].is_set():
                self._result[url] = None
            else:
                self._result[url] = content

    def abort(self, url: str):
        """Abort the operation for `url`."""
        self._aborted[url].set()

    def cancel(self, url: str) -> bool:
        """Same as :meth:`abort`"""
        return self.abort(url)

    def aborted(self, url: str) -> bool:
        """Check if the operation for `url` was aborted."""
        return self._aborted[url].is_set()

    def cancelled(self, url: str) -> bool:
        """Same as aborted."""
        return self.aborted(url)

    def result(self, url: str) -> Tuple[int, Union[bytes, bytearray], requests.Response]:
        """Return the result of the fetch operation.

        Args:
            url: The url for which to perform operation

        Returns:
            A tuple of status, response and response content.

        """
        return self._status[url], self._responses[url], self._result[url]

    def finished(self, url: str) -> Optional[bool]:
        """Check if the URL has been fetched.

        Args:
            url: The url for which to perform operation

        """
        finished = self._finished.get(url)
        if finished:
            return finished.is_set()
        else:
            return None

    def bytes_downloaded(self, url: str) -> Optional[int]:
        """Display progress of URL.

        Args:
            url: The url for which to perform operation

        """
        return self._dl_bytes.get(url)

    def url_init(self, url: str) -> bool:
        """Check if URL fetch has started.

        Args:
            url: The url for which to perform operation

        """
        return bool(self._init.get(url, False))

    def progress(self, url: str) -> Optional[float]:
        """Display progress of URL.

        Args:
            url: The url for which to perform operation

        """
        return self._progress.get(url)

    def reset(self):
        """Reset all the internal state."""
        self.__init__()

    def clear(self, url: str):
        """Clear the artefacts for URL.

        Args:
            url: The url for which to perform operation

        """
        self._progress.pop(url)
        self._finished.pop(url)
        self._result.pop(url)
        self._dl_bytes.pop(url)
        self._status.pop(url)
        self._threads.pop(url)
        self._aborted.pop(url)
