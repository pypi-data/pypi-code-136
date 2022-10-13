"""Core services"""

from typing import Dict, Any

from django.db.models import Avg, Min, Max

from .models import SystemState

TOP_COUNT = 5


def get_context_data(context: Dict[str, Any]) -> Dict[str, Any]:
    """Get context data for statistics page"""
    agg_total = SystemState.objects.aggregate(
        min=Min("cpu_usage"),
        max=Max("cpu_usage"),
        avg=Avg("cpu_usage"),
    )
    top_records = (
        SystemState.objects.all()
        .only("created", "cpu_usage", "source_ip")
        .order_by("-created")[:TOP_COUNT]
    )
    agg_top = top_records.aggregate(
        min=Min("cpu_usage"),
        max=Max("cpu_usage"),
        avg=Avg("cpu_usage"),
    )

    context["system_states"] = top_records
    context["top_count"] = TOP_COUNT
    context["avg"] = {
        "total": {
            "min": agg_total["min"],
            "max": agg_total["max"],
            "avg": agg_total["avg"],
        },
        "top": {
            "min": agg_top["min"],
            "max": agg_top["max"],
            "avg": agg_top["avg"],
        },
    }
    return context
