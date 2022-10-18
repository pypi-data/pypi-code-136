from datetime import datetime, timezone
from typing import Union

from .validate import validate_max_tokens, validate_replenish_time


class TokenBucket:
    def __init__(self, replenish_time: int, max_tokens: int) -> None:
        self.replenish_time: int = replenish_time
        self.max_tokens: int = max_tokens
        self.tokens: int = max_tokens
        self.last_replenished: float = datetime.now(timezone.utc).timestamp()
        self.identifier: Union[str, None] = None
        self.cost: int = 0
        validate_max_tokens(self.max_tokens)
        validate_replenish_time(self.replenish_time)

    def consume(self) -> bool:
        if self.tokens < self.cost:
            return False

        self.tokens -= self.cost
        return True
