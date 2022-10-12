# from django.conf import settings
from django.db import models


class FKTestingModel(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )
    non_filled = models.CharField(
        max_length=32,
    )


# class M2MTestingModel(models.Model):
#     name = models.CharField(
#         max_length=32,
#     )


# class TestingModel(models.Model):
#     fk_test = models.ForeignKey(
#         FKTestingModel,
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE,
#     )
#     m2m_test = models.ManyToManyField(
#         M2MTestingModel,
#         blank=True,
#     )
#     enjoy_jards_macale = models.BooleanField(
#         default=True,
#     )
#     name = models.CharField(
#         max_length=30,
#     )
#     nickname = models.SlugField(
#         max_length=36,
#     )
#     age = models.IntegerField()
#     bio = models.TextField()
#     birthday = models.DateField()
#     birth_time = models.TimeField()
#     appointment = models.DateTimeField()
#     blog = models.URLField()
#     uuid = models.UUIDField(
#         primary_key=False,
#     )
#     name_hash = models.BinaryField(
#         max_length=16,
#     )
#     days_since_last_login = models.BigIntegerField()
#     duration_of_sleep = models.DurationField()
#     email = models.EmailField()
#     value = models.FloatField()

#     try:
#         from django.db.models import JSONField

#         data = JSONField()
#     except ImportError:
#         # Skip JSONField-related fields
#         pass

#     try:
#         from django.contrib.postgres.fields import (
#             ArrayField,
#             HStoreField,
#             JSONField as PostgresJSONField,
#         )
#         from django.contrib.postgres.fields.citext import CICharField, CIEmailField, CITextField
#         from django.contrib.postgres.fields.ranges import (
#             BigIntegerRangeField,
#             DateRangeField,
#             DateTimeRangeField,
#             IntegerRangeField,
#         )

#         if settings.USING_POSTGRES:
#             acquaintances = ArrayField(models.IntegerField())
#             postgres_data = PostgresJSONField()
#             hstore_data = HStoreField()
#             ci_char = CICharField(max_length=30)
#             ci_email = CIEmailField()
#             ci_text = CITextField()
#             int_range = IntegerRangeField()
#             bigint_range = BigIntegerRangeField()
#             date_range = DateRangeField()
#             datetime_range = DateTimeRangeField()
#     except ImportError:
#         # Skip PostgreSQL-related fields
#         pass

#     try:
#         from django.contrib.postgres.fields.ranges import FloatRangeField

#         if settings.USING_POSTGRES:
#             float_range = FloatRangeField()
#     except ImportError:
#         # Django version greater or equal than 3.1
#         pass

#     try:
#         from django.contrib.postgres.fields.ranges import DecimalRangeField

#         if settings.USING_POSTGRES:
#             decimal_range = DecimalRangeField()
#     except ImportError:
#         # Django version lower than 2.2
#         pass
