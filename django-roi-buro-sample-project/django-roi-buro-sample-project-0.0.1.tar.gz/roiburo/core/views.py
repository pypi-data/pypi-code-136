"""Core views"""

from typing import Any, Dict

from django.views import generic
from rest_framework.generics import CreateAPIView

from .serializers import SystemStateSzr
from .services import get_context_data


class CreateSystemStateView(CreateAPIView):
    """Create system state record"""
    serializer_class = SystemStateSzr

    def perform_create(self, serializer):
        serializer.save(source_ip=self.request.META["REMOTE_ADDR"])


class SystemStateStatsView(generic.TemplateView):
    """Get statistics about system states"""

    template_name = "core/templates/system_state_stats.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return get_context_data(context)
