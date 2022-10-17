from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
from django.utils.translation import gettext_lazy as _
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks

class GalleryImageBlock(blocks.StructBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(local_blocks=[
            ('id', ImageChooserBlock(icon='image', label=_('Image'))),
        ], **kwargs)


@register_snippet
class Gallery(ClusterableModel):
    name = models.CharField(max_length=120, help_text=_('Gallery name'))
    stream = StreamField(use_json_field=True, block_types=[
        ('gallery_image', GalleryImageBlock()),
    ])
    panels = [
        FieldPanel('name'),
        FieldPanel('stream'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Galerie')
        verbose_name_plural = _('Galerie')
