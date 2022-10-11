from dataclasses import dataclass, field
from datetime import datetime, timedelta
from threading import Lock
from typing import Optional, Dict
from uuid import UUID, uuid4 as generate_uuid

from odp.compute.flow_state import WatermarkStore, get_watermark_store


@dataclass
class FlowLockState:
    """Structure that tracks the lock state

    Locks have an expiration `ttl` and will automatically unlock once elapsed
    """

    ttl: timedelta
    lock_count_max: int = 1

    locks: Dict[UUID, datetime] = field(init=False)

    def __post_init__(self):
        self.locks = {}

    @property
    def lock_count(self):
        """Get the number of locks on state

        Returns:
            Number of locks on state
        """
        return len(self.locks)

    def acquire(self) -> UUID:
        """Acquire a lock

        Returns:
            A new lock
        """
        if self.lock_count >= self.lock_count_max:
            raise BlockingIOError("FlowLock is locked")

        lock_key = generate_uuid()
        self.locks[lock_key] = datetime.now()

        return lock_key

    def release(self, lock_key: UUID) -> None:
        """Release a lock

        Args:
            lock_key: The lock to be released

        Returns:

        """
        try:
            self.locks.pop(lock_key)
        except KeyError as e:
            raise ValueError("FlowLock is already open") from e

    def refresh(self, lock_key) -> None:
        """Refresh a lock

        Args:
            lock_key: Lock to be refreshed
        """
        try:
            assert lock_key in self.locks
            self.locks[lock_key] = datetime.now()
        except AssertionError as e:
            raise ValueError("FlowLock is already open") from e

    def is_open(self) -> bool:
        """Check whether lockstate is open

        Returns:
            `True` if state is open, `False` otherwise
        """
        t = datetime.now()

        if self.lock_count < self.lock_count_max:
            return True

        for key, last_refereshed in self.locks.items():
            if last_refereshed + self.ttl >= t:
                return True

        return False

    def is_locked(self) -> bool:
        """Check whether lockstate is closed

        Returns:
            `True`  is locked, `False` otherwise
        """
        return not self.is_open()


@dataclass
class FlowLock:
    """Track lock state in a `WatermarkStore`"""

    key: str
    ttl: timedelta = timedelta(seconds=60.0)
    lock_count_max: int = 1

    store: Optional[WatermarkStore] = None
    state: Optional[FlowLockState] = field(init=False)
    lock: Lock = field(init=False)

    def __post_init__(self):
        self.lock = Lock()
        if not self.store:
            self.store = get_watermark_store()

    def _update(self) -> None:
        """Update lock state from watermark storage"""
        self.state = self.store.get(self.key)
        if not self.state:
            self.state = FlowLockState(ttl=self.ttl, lock_count_max=self.lock_count_max)

    def _persist(self) -> None:
        """Persist lock state to watermark storage"""
        if self.store:
            self.store.set(self.key, self.store)

    def acquire(self) -> UUID:
        """Acquire a new lock

        Returns:
            New lock
        """

        with self.lock:
            self._update()
            lock_key = self.state.acquire()
            self._persist()

        return lock_key

    def release(self, lock_key: UUID) -> None:
        """Release a lock

        Args:
            lock_key: Lock to be released
        """

        with self.lock:
            self._update()
            self.state.release(lock_key)
            self._persist()

    def refresh(self, lock_key: UUID) -> None:
        """Refresh a lock

        Args:
            lock_key: Lock to be refreshed
        """

        with self.lock:
            self._update()
            self.state.refresh(lock_key)
            self._persist()
