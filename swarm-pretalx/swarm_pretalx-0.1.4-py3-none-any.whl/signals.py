
import logging

from django.conf import settings
from django.dispatch import receiver
from pretalx.agenda.tasks import export_schedule_html
from pretalx.schedule.signals import schedule_release
from .tasks import post_to_swarm

logger = logging.getLogger("Swarm-plugin-logger")

def get_export_zip_path(event):
    export_path = settings.HTMLEXPORT_ROOT / event.slug
    return export_path.with_suffix(".zip")


@receiver(schedule_release, dispatch_uid="swarm signal")
def on_schedule_release(sender, schedule, user, **kwargs):

    zip_path = str(get_export_zip_path(sender))

    try:
        export_schedule_html.apply_async(kwargs={"event_id": sender.id}, link=post_to_swarm.si(zip_path))
    except Exception as e:
        logger.info(e)    


