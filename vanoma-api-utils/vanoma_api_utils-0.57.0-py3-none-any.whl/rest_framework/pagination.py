from typing import Any, Dict, List


def create_page(
    count: int, results: List[Any], next: str = None, previous: str = None
) -> Dict[str, Any]:
    return {
        "count": count,
        "next": next,
        "previous": previous,
        "results": results,
    }
