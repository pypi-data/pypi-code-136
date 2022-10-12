from django_set_field.debug import hook_class

from rest_framework import serializers

# SetField = hook_class(serializers.MultipleChoiceField)
# SetField = serializers.ListField(child=serializers.CharField())


class StringListField(serializers.ListField):
    child = serializers.CharField()


SetField = StringListField
# SetField = hook_class(StringListField)
# @hook_class
# class SetField(serializers.MultipleChoiceField):
#     def to_representation(self, value):
#         return super().to_representation(value)

#     def to_internal_value(self, data):
#         return super().to_internal_value(data)
