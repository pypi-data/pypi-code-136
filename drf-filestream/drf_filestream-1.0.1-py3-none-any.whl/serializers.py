import humanfriendly

from django.conf import settings
from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.ModelSerializer):

    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FileModel
        fields = '__all__'

    def validate_file(self, data):

        max_size = settings.FILE_UPLOAD_MAX_SIZE if hasattr(settings, 'FILE_UPLOAD_MAX_SIZE') else None
        if max_size and data.size > humanfriendly.parse_size(str(max_size)):
            raise serializers.ValidationError(f'file size limit {max_size}')

        return data
