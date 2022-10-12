from django.core.management.base import BaseCommand

from ...models import Configuration


class Command(BaseCommand):  # lint-amnesty, pylint: disable=missing-class-docstring
    help = "Create or update a Stepwise API configuration."

    def add_arguments(self, parser):
        parser.add_argument(
            "--host",
            dest="host",
            default="https://stepwiseai01.querium.com/webMathematica/api/",
            required=False,
            help="URL to the Stepwise API host. Default: https://stepwiseai01.querium.com/webMathematica/api/",
        )
        parser.add_argument(
            "--environment",
            dest="environment",
            default="Production",
            required=False,
            help="Which Open edX environment to configure. Options: dev, test, prod,  Default: prod",
        )

    def handle(self, *args, **options):

        config = Configuration.objects.get_or_create(type=options.get("environment"))[0]
        config.stepwise_host = options.get("host")
        config.save()
