from django.conf.urls import url
from .views import FutureEventsViewset, PastEventsViewset

urlpatterns = [
    url(r'^events/future/', FutureEventsViewset.urls(model_prefix="event-future")),
    url(r'^events/past/', PastEventsViewset.urls(model_prefix="event-past"))
]

