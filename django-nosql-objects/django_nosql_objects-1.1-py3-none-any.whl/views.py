import json
from typing import Any
from urllib import request
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from django.conf import settings
from guardian.shortcuts import get_objects_for_user, assign_perm
from guardian.utils import get_anonymous_user
from django.db import transaction
from rest_framework_guardian import filters
from django.contrib.auth.models import User
from .serializers import ObjectClassSerializer, ObjectSerializer, PermissionsSerializer
from .models import Object, ObjectClass, ObjectUserObjectPermission
from .permissions import ObjectPermissions, ReadOnlyPermission
from .pagination import ObjectViewSetPagination


class ObjectClassViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectClassSerializer
    queryset = ObjectClass.objects.all()
    permission_classes = [DjangoObjectPermissions]


class ObjectViewSet(viewsets.ModelViewSet):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()
    pagination_class = ObjectViewSetPagination
    permission_classes = [ObjectPermissions|ReadOnlyPermission]
    filter_backends = [filters.ObjectPermissionsFilter]

    def get_queryset(self) -> queryset:
        query_set = super().get_queryset()
        # Filter by class
        if 'object_class' in self.request.query_params:
            classParam = self.request.query_params['object_class']
            if not classParam.isnumeric():                                
                objectClass = ObjectClass.objects.filter(name=classParam).first()
                if objectClass:
                    query_set = query_set.filter(object_class=objectClass)
                else:
                    raise Exception("Class "+classParam+" not found")
            else:
                query_set = query_set.filter(object_class__pk=classParam)
        # Filter by query
        if 'query' in self.request.query_params:
            obj = json.loads(self.request.query_params['query'])
            params = {}
            for key in obj:
                params['data__'+key] = obj[key]
            for param_key in params:
                query_set = query_set.filter(**{param_key:params[param_key]})
        return query_set

    def perform_create(self, serializer) -> None:
        """
        Sets the user creating the object
        """
        serializer.validated_data["created_by"] = self.request.user
        serializer.validated_data["updated_by"] = self.request.user
        super().perform_create(serializer)

    @action(detail=True, methods=['POST'])
    def perms(self, request, pk=None) -> Response:    
        """
        Endpoint for modifying the permissions on an object
        """
        object = self.get_queryset().get(pk=pk)
        if not self.request.user.has_perm('change_object', object):
            return Response(status=403)
        perms = PermissionsSerializer(data=request.data)        
        if perms.is_valid():
            data = perms.data
            if 'clear' in data and data['clear']:
                ObjectUserObjectPermission.objects.filter(content_object=object).delete()                    
            for perm in data:
                if perm == 'clear': continue
                if 'users' in data[perm]:
                    for name in data[perm]['users']:
                        if name == 'AnonymousUser':
                            if perm != 'view_object':
                                return Response(status=400, data="can not give permission to anonymous user other that view!")
                            if not object.object_class.allow_anonymous:
                                return Response(status=400, data="can not give anonymous permission in this object class")
                            user = get_anonymous_user()
                        else:
                            user = User.objects.get(username=name)
                        if user:
                            assign_perm(perm, user, object)
                        else:
                            return Response(status=400, data="user "+name+" not found!")
                if 'groups' in data[perm]:
                    for name in data[perm]['groups']:
                        group = Group.objects.get(name=name)
                        if group:
                            assign_perm(perm, group, object)
                        else:
                            return Response(status=400, data="group "+name+" not found!")
                        
        else:
            return Response(status=400, data=perms.error_messages)
        return Response(status=200)

