from rest_framework import serializers
from stepwise_plugin.models import Configuration


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Configuration
        fields = "__all__"
