"""Core serializers"""

from rest_framework import serializers

from core.models import SystemState


class SystemStateSzr(serializers.ModelSerializer):
    """System state serializer"""
    created = serializers.DateTimeField(read_only=True)
    source_ip = serializers.IPAddressField(read_only=True)

    class Meta:
        model = SystemState
        fields = ("created", "cpu_usage", "source_ip")
