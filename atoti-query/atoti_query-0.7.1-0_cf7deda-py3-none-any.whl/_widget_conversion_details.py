from dataclasses import dataclass

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class WidgetConversionDetails:
    mdx: str
    session_id: str
    widget_creation_code: str
