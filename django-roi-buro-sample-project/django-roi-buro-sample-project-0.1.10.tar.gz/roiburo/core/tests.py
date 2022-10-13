"""Core tests"""

import logging
import statistics

from django.conf import settings
from django.urls import reverse
from faker import Faker
from faker.providers import internet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from roiburo.tests import CustomTestCase
from .models import SystemState
from .services import get_context_data, TOP_COUNT

logging.config.dictConfig(settings.LOGGING)
logger = logging.getLogger("test")


class CoreTest(CustomTestCase):
    """Core testcase"""
    def test_create_cpu_usage(self):
        """Test create cpu usage"""
        request_data = dict(
            url=reverse("create-system-state", kwargs={"version": "v1"}),
            method="post",
            data={"cpu_usage": "25"},
        )
        resp = self._process_request(**request_data)  # type: ignore
        logger.debug(
            self._get_formatted_response(
                test_description="Create cpu usage", request=request_data, response=resp
            )
        )
        self.assertEqual(resp.status_code, HTTP_201_CREATED)
        self.assertEqual(SystemState.objects.all().count(), 1)
        created = SystemState.objects.filter(cpu_usage=25)
        self.assertEqual(len(created), 1)

    def test_get_statistics(self):
        """Test get stats"""
        request_data = dict(
            url=reverse("get-system-state-details", kwargs={"version": "v1"}),
            method="get",
            data={},
        )
        resp = self._process_request(**request_data)  # type: ignore
        self.assertEqual(resp.status_code, HTTP_200_OK)

    def test_get_context_data(self):
        """Test service get_context_data"""
        fake = Faker()
        fake.add_provider(internet)
        SystemState.objects.all().delete()
        cpu_usages = (100, 25, 50, 75, 30, 90, 80, 35, 20)
        for cpu_usage in cpu_usages:
            SystemState.objects.create(
                cpu_usage=cpu_usage, source_ip=fake.ipv4_private()
            )

        context = get_context_data({})

        self.assertEqual(context["avg"]["total"]["min"], min(cpu_usages))
        self.assertEqual(context["avg"]["total"]["max"], max(cpu_usages))
        self.assertEqual(context["avg"]["total"]["avg"], statistics.fmean(cpu_usages))

        top_usages = cpu_usages[-TOP_COUNT:]
        logger.info(top_usages)

        self.assertEqual(context["avg"]["top"]["min"], min(top_usages))
        self.assertEqual(context["avg"]["top"]["max"], max(top_usages))
        self.assertEqual(context["avg"]["top"]["avg"], statistics.fmean(top_usages))

    def test_get_schema(self):
        """Test get schema"""
        request_data = dict(
            url=settings.BASE_URL + "/api/schema",
            method="get",
            data={},
        )
        resp = self._process_request(**request_data)  # type: ignore
        self.assertEqual(resp.status_code, HTTP_200_OK)
