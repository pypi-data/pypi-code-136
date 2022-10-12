import pytest

from bfet import DjangoTestingModel

from ...django_examples.models import FKTestingModel


@pytest.mark.django_db
class TestDjangoTestingModel:
    def test_make_should_create_one_object(self):
        new_obj = DjangoTestingModel.create(FKTestingModel)
        assert isinstance(new_obj, FKTestingModel)

    def test_model_create(self):
        assert FKTestingModel.objects.all().count() == 0
        new_obj = DjangoTestingModel.create(FKTestingModel, name="prueba")
        assert FKTestingModel.objects.all().count() == 1
        assert new_obj.name == "prueba"

    def test_model_get_or_create(self):
        assert FKTestingModel.objects.all().count() == 0
        new_obj = DjangoTestingModel.create(FKTestingModel, name="prueba")
        assert FKTestingModel.objects.all().count() == 1
        assert new_obj.name == "prueba"
        duplicated_obj = DjangoTestingModel.create(FKTestingModel, name="prueba")
        assert new_obj == duplicated_obj
