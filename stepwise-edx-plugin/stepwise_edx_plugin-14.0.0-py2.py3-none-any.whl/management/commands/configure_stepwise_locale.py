from django.core.management.base import BaseCommand

from ...models import Locale


class Command(BaseCommand):  # lint-amnesty, pylint: disable=missing-class-docstring
    help = "Create or update a Stepwise marketing site html element locale"

    def add_arguments(self, parser):
        parser.add_argument(
            "--element_id",
            dest="element_id",
            help="An html element id. Example: stepwise-locale-contact",
        )
        parser.add_argument(
            "--language",
            dest="language",
            help="A language code. Examples: en, en-US, es, es-419, es-MX",
        )
        parser.add_argument(
            "--url",
            dest="url",
            help="URL for for anchor tag for this language. Example: https://mx.stepwisemath.ai/contact/",
        )
        parser.add_argument(
            "--value",
            dest="value",
            help="The text value of this html element. Example: Contacto",
        )

    def handle(self, *args, **options):

        Locale.objects.update_or_create(
            element_id=options["element_id"],
            language=options["language"],
            url=options["url"],
            value=options["value"],
        )
