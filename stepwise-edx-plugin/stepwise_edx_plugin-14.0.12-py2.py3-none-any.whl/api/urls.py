from rest_framework.routers import DefaultRouter
from stepwise_plugin.api.views import ConfigurationViewSet

router = DefaultRouter(trailing_slash=False)
router.register("api/v1/configuration", ConfigurationViewSet)
urlpatterns = router.urls
