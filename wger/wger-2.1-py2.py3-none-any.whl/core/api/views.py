# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

# Standard Library
import logging

# Django
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Third Party
from django_email_verification import send_email
from rest_framework import (
    status,
    viewsets,
)
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response

# wger
from wger import (
    MIN_APP_VERSION,
    get_version,
)
from wger.core.api.permissions import AllowRegisterUser
from wger.core.api.serializers import (
    DaysOfWeekSerializer,
    LanguageSerializer,
    LicenseSerializer,
    RepetitionUnitSerializer,
    UserApiSerializer,
    UserprofileSerializer,
    UserRegistrationSerializer,
    WeightUnitSerializer,
)
from wger.core.forms import UserLoginForm
from wger.core.models import (
    DaysOfWeek,
    Language,
    License,
    RepetitionUnit,
    UserProfile,
    WeightUnit,
)
from wger.utils.api_token import create_token
from wger.utils.permissions import WgerPermission


logger = logging.getLogger(__name__)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for the user profile

    This endpoint works somewhat differently than the others since it always
    returns the data for the currently logged-in user's profile. To update
    the profile, use a POST request with the new data, not a PATCH.
    """
    serializer_class = UserprofileSerializer
    permission_classes = (
        IsAuthenticated,
        WgerPermission,
    )

    def get_queryset(self):
        """
        Only allow access to appropriate objects
        """
        return UserProfile.objects.filter(user=self.request.user)

    def get_owner_objects(self):
        """
        Return objects to check for ownership permission
        """
        return [(User, 'user')]

    def list(self, request, *args, **kwargs):
        """
        Customized list view, that returns only the current user's data
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset.first(), many=False)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(request.user.userprofile, data=data)
        if serializer.is_valid():
            serializer.save()

            # New email, update the user and reset the email verification flag
            if request.user.email != data['email']:
                request.user.email = data['email']
                request.user.save()
                request.user.userprofile.email_verified = False
                request.user.userprofile.save()
                logger.debug('resetting verified flag')

            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, url_name='verify-email', url_path='verify-email')
    def verify_email(self, request):
        """
        Return the username
        """

        profile = request.user.userprofile
        if profile.email_verified:
            return Response({'status': 'verified', 'message': 'This email is already verified'})

        send_email(request.user)
        return Response(
            {
                'status': 'sent',
                'message': f'A verification email was sent to {request.user.email}'
            }
        )


class ApplicationVersionView(viewsets.ViewSet):
    """
    Returns the application's version
    """
    permission_classes = (AllowAny, )

    @staticmethod
    def get(request):
        return Response(get_version())


class PermissionView(viewsets.ViewSet):
    """
    Returns the application's version
    """
    permission_classes = (AllowAny, )

    @staticmethod
    def get(request):
        permission = request.query_params.get('permission')

        if permission is None:
            return Response(
                "Please pass a permission name in the 'permission' parameter",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if request.user.is_anonymous:
            return Response({'result': False})

        return Response({'result': request.user.has_perm(permission)})


class RequiredApplicationVersionView(viewsets.ViewSet):
    """
    Returns the minimum required version of flutter app to access this server
    """
    permission_classes = (AllowAny, )

    @staticmethod
    def get(request):
        return Response(get_version(MIN_APP_VERSION, True))


class UserAPILoginView(viewsets.ViewSet):
    """
    API endpoint for api user objects
    """
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserApiSerializer
    throttle_scope = 'login'

    def get(self, request):
        return Response({'message': "You must send a 'username' and 'password' via POST"})

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data["username"]

        # Try to retrieve the user
        form = UserLoginForm(data=serializer.data)
        if not form.is_valid():
            logger.info(f"Tried logging via API with unknown user: '{username}'")
            return Response(
                {'detail': 'Username or password unknown'},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        token = create_token(form.get_user())
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserAPIRegistrationViewSet(viewsets.ViewSet):
    """
    API endpoint
    """
    permission_classes = (AllowRegisterUser, )
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        """
        Only allow access to appropriate objects
        """
        return UserProfile.objects.filter(user=self.request.user)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.userprofile.added_by = request.user
        user.userprofile.save()
        token = create_token(user)

        # Email the user with the activation link
        send_email(user)

        return Response(
            {
                'message': 'api user successfully registered',
                'token': token.key
            },
            status=status.HTTP_201_CREATED
        )


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for workout objects
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    ordering_fields = '__all__'
    filterset_fields = ('full_name', 'short_name')

    @method_decorator(cache_page(settings.WGER_SETTINGS['EXERCISE_CACHE_TTL']))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DaysOfWeekViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for workout objects
    """
    queryset = DaysOfWeek.objects.all()
    serializer_class = DaysOfWeekSerializer
    ordering_fields = '__all__'
    filterset_fields = ('day_of_week', )


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for workout objects
    """
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    ordering_fields = '__all__'
    filterset_fields = (
        'full_name',
        'short_name',
        'url',
    )


class RepetitionUnitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for repetition units objects
    """
    queryset = RepetitionUnit.objects.all()
    serializer_class = RepetitionUnitSerializer
    ordering_fields = '__all__'
    filterset_fields = ('name', )


class WeightUnitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for weight units objects
    """
    queryset = WeightUnit.objects.all()
    serializer_class = WeightUnitSerializer
    ordering_fields = '__all__'
    filterset_fields = ('name', )
