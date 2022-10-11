""" Elasticsearch forms
"""
import logging

from django import forms
from django.forms import ModelForm

from core_main_app.commons import exceptions
from core_main_app.components.template import api as template_api
from core_main_app.components.template_version_manager import (
    api as template_version_manager_api,
)

from core_elasticsearch_app.components.elasticsearch_template.models import (
    ElasticsearchTemplate,
)

logger = logging.getLogger(__name__)


class ElasticsearchTemplateForm(ModelForm):
    """ElasticsearchTemplate form"""

    template = forms.ChoiceField(
        label="Template", widget=forms.Select(attrs={"class": "form-control"})
    )

    title_path = forms.CharField(
        label="Path to Title",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Resource/identity/title", "class": "form-control"}
        ),
    )

    description_paths = forms.CharField(
        label="Paths to Description",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Resource/content/description\nResource/content/subject",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        """Meta"""

        model = ElasticsearchTemplate
        fields = ["template", "title_path"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["template"].choices = _get_templates_versions(request=self.request)
        self.fields["description_paths"].initial = "\n".join(
            kwargs["instance"].description_paths if kwargs["instance"] else ""
        )

    def clean_template(self):
        """clean_template

        Returns:

        """
        data = self.cleaned_data["template"]
        return template_api.get_by_id(data, request=self.request)

    def clean_description_paths(self):
        """clean_description_paths

        Returns:

        """
        return self.cleaned_data["description_paths"].split()


# FIXME: duplicate from core_oaipmh_provider_app
def _get_templates_versions(request):
    """Get templates versions.

    Args:
        request:

    Returns:
        List of templates versions.

    """
    templates = []
    try:
        list_ = template_version_manager_api.get_active_global_version_manager(
            request=request
        )
        for elt in list_:
            for version in elt.versions:
                template = template_api.get_by_id(version, request=request)
                version_name = template.display_name
                templates.append((version, version_name))
    except exceptions.DoesNotExist as exception:
        logger.warning("_get_templates_versions threw an exception: %s", str(exception))

    return templates
