from typing import Any, Dict, Optional

import sentry_sdk


def set_scope_tags(
    scope: sentry_sdk.Scope, *, tags: Dict[str, Optional[Any]]
) -> None:
    for key, value in tags.items():
        if value or value is False:
            scope.set_tag(key, value)
