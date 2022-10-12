from django.conf import settings
from django.db import models
from djangoldp_conversation.models import Conversation, Message
from djangoldp.models import Model
from djangoldp_circle.models import Circle
from django.contrib.auth import get_user_model
from djangoldp_resource.permissions import *


class Type (Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Resource type")

    class Meta(Model.Meta):
        anonymous_perms = ['view', 'add']
        rdf_type = 'sib:type'

    def __str__(self):
        return self.name


class Keyword (Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Keywords")

    class Meta(Model.Meta):
        anonymous_perms = ['view', 'add']
        rdf_type = 'sib:keyword'
 
    def __str__(self):
        return self.name


class Resource (Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, verbose_name="Resource Title", null=True, blank=True)
    shortdesc = models.TextField(blank=True, null=True)
    longdesc = models.TextField(blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    type = models.ForeignKey(Type, blank=True, null=True,verbose_name="Resource type", on_delete=models.SET_NULL)
    img = models.URLField(default=settings.BASE_URL + "/media/defaultresource.png", verbose_name="Illustration", null=True, blank=True)
    document = models.URLField(blank=True, null=True, verbose_name="Document")
    link = models.CharField(max_length=2048, blank=True, null=True, verbose_name="Internet link")
    conversations = models.ManyToManyField(Conversation, blank=True, related_name='resources')
    circle = models.ForeignKey(Circle, blank=True, null=True, related_name="resources", on_delete=models.SET_NULL)
    creationDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta(Model.Meta):
        serializer_fields = ["@id", "name", "shortdesc", "longdesc", "type", "img", "document",\
                           "link", "keywords", "conversations", "circle"]
        auto_author = 'user'
        owner_field = 'user'
        container_path = 'resources/'
        rdf_type = 'hd:resource'
        anonymous_perms = ['view']
        owner_perms = ['inherit', 'change', 'control', 'delete']
        authenticated_perms = ['inherit', 'add']
        nested_fields = ['keywords', 'conversations', 'circle', 'type']
        permission_classes = [ResourcePermissions]
        
    def __str__(self):
        return self.name
