from rest_framework import serializers
from .models import Object, ObjectClass
from rest_framework import serializers
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin


class PermissionsSubjectsSerializer(serializers.Serializer):
    users = serializers.ListField(required=False)
    groups = serializers.ListField(required=False)


class PermissionsSerializer(serializers.Serializer):
    view_object = PermissionsSubjectsSerializer(required=False)
    change_object = PermissionsSubjectsSerializer(required=False)
    delete_object = PermissionsSubjectsSerializer(required=False)
    clear = serializers.BooleanField(required=False)


class ObjectClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectClass
        fields = "__all__"


class ObjectSerializer(ObjectPermissionsAssignmentMixin, serializers.ModelSerializer):
    data = serializers.JSONField()
    _object_class: ObjectClass

    class Meta:
        model = Object
        fields = "__all__"
        read_only_fields = [
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
            "version",
        ]

    def validate(self, data):
        if not data["object_class"]:
            raise serializers.ValidationError("Object class is required")
        return super().validate(data)

    def to_internal_value(self, data):
        objectClass: ObjectClass
        if type(data["object_class"]) == str:
            objectClass = ObjectClass.objects.get(name=data["object_class"])
        else:
            objectClass = ObjectClass.objects.get(pk=data["object_class"])
        if not objectClass:
            raise serializers.ValidationError("Object class is required")
        else:
            self._object_class = objectClass
            self.context["object_class"] = objectClass
            data["object_class"] = objectClass.pk
        dict = super().to_internal_value(data)
        return dict    

    def get_permissions_map(self, created):
        current_user = self.context["request"].user
        # Default object perms:
        return {
            "view_object": [current_user],
            "change_object": [current_user],
            "delete_object": [current_user],
        }
