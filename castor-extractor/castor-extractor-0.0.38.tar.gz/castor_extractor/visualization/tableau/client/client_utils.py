from typing import Dict, Iterator, Optional

from ....utils import SerializedAsset
from ..assets import EXPORTED_FIELDS, QUERY_FIELDS, TableauAsset

QUERY_TEMPLATE = """
{{
  {object_type}Connection(first: {page_size}, after: AFTER_TOKEN_SIGNAL) {{
    nodes {{ {query_fields}
    }}
    pageInfo {{
      hasNextPage
      endCursor
    }}
    totalCount
  }}
}}
"""

RESOURCE_TEMPLATE = "{resource}Connection"


def get_paginated_objects(
    server, asset: TableauAsset, page_size: int
) -> SerializedAsset:

    fields = QUERY_FIELDS[asset]["fields"].value
    object_type = QUERY_FIELDS[asset]["object_type"].value
    query = QUERY_TEMPLATE.format(
        object_type=object_type,
        page_size=page_size,
        query_fields=fields,
    )
    resource = RESOURCE_TEMPLATE.format(resource=object_type)

    return [
        result
        for results in query_scroll(server, query, resource)
        for result in results
    ]


def query_scroll(
    server, query: str, resource: str
) -> Iterator[SerializedAsset]:
    """build a tableau query iterator handling pagination and cursor"""

    def _call(cursor: Optional[str]) -> dict:
        # If cursor is defined it must be quoted else use null token
        token = "null" if cursor is None else f'"{cursor}"'
        query_ = query.replace("AFTER_TOKEN_SIGNAL", token)

        return server.metadata.query(query_)["data"][resource]

    cursor = None
    while True:
        payload = _call(cursor)
        yield payload["nodes"]

        page_info = payload["pageInfo"]
        if page_info["hasNextPage"]:
            cursor = page_info["endCursor"]
        else:
            break


def extract_asset(asset: Dict, asset_type: TableauAsset) -> Dict:
    """Agnostic function extracting dedicated attributes with define asset"""
    return {key: getattr(asset, key) for key in EXPORTED_FIELDS[asset_type]}
