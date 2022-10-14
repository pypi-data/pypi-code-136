from pathlib import Path
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response

from .utils import get_response


class FileStreamView(views.APIView):

    permission_classes = settings.FILE_ACCESS_PERMISSIONS if hasattr(settings, 'FILE_ACCESS_PERMISSIONS') else []

    def get(self, request, filepath):
        """get the filestream according to the given path
        """
        file = Path(settings.MEDIA_ROOT).joinpath(filepath)

        if not file.exists():
            return Response({'msg': 'file not exists!'}, status=status.HTTP_404_NOT_FOUND)

        return get_response(file, request)
