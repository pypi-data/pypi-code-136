from typing import Dict, List, Type, Union

from ..create_data import DataCreator


class DjangoTestingModel(DataCreator):
    def __init__(
        self, model, quantity: int, in_bulk: bool, fill_all_fields: bool, force_create: bool
    ) -> None:
        self.model = model
        self.quantity = quantity
        self.in_bulk = in_bulk
        self.fill_all_fields = fill_all_fields
        self.force_create = force_create

    @classmethod
    def create(
        cls,
        model: Type,
        quantity: int = 1,
        in_bulk: bool = False,
        fill_all_fields: bool = True,
        force_create: bool = False,
        **kwargs,
    ) -> Union[Type, List[Type]]:
        """The method to call when we want to create one or more instances
        TODO
        Create and raise an error if in_bulk or quantity > 1 and force_create is set to True
        and instances can't be created without repeating a given field

        Parameters
        ----------
            model : Type
                The model that we want to use to create the instances from

            quantity : int, optional
                The number of instances that we want to create, by default 1

            in_bulk : bool, optional
                Boolean to use the bulk_create built-in of Django, by default False

            fill_all_fields : bool, optional
                Boolean to tell if all the fields must be filled or it's better to leave them blank
                (if possible), by default True

            force_create : bool, optional
                Boolean to indicate, if any field is manually filled, it has to perform
                a get_or_create instead of create, by default False

            kwargs : Dict[str, Any]
                Fields of the model that we want to manually fill

        Returns
        -------
            Union[Type, List[Type]]
                An instance or a list of instances created
        """
        creator = cls(model, quantity, in_bulk, fill_all_fields, force_create)
        if quantity > 1:
            if in_bulk:
                return creator.create_in_bulk(**kwargs)
            else:
                return [creator.create_model(**kwargs) for number in range(quantity)]
        else:
            return creator.create_model(**kwargs)

    def get_model_manager(self) -> Type:
        try:
            manager = self.model._default_manager
        except AttributeError:
            manager = self.model.objects
        finally:
            return manager

    def create_in_bulk(self, **kwargs):
        pre_objects = [
            self.model(**self.inspect_model(**kwargs)) for number in range(self.quantity)
        ]
        return self.get_model_manager().bulk_create(pre_objects)

    def create_model(self, **kwargs) -> Type:
        model_data = self.inspect_model(**kwargs)
        model_manager = self.get_model_manager()
        if self.force_create:
            kwargs.update(model_data)
            return model_manager.create(**kwargs)
        else:
            model, created = model_manager.get_or_create(**kwargs, defaults=model_data)
            return model

    def inspect_model(self, **kwargs) -> Dict:
        fields_info = dict()
        # all_model_fields = model._meta.get_fields()
        for field in self.model._meta.fields:
            field_name = field.name
            if field_name == "id":
                continue
            if field_name in kwargs:
                fields_info[field_name] = kwargs.pop(field_name)
            else:
                if self.fill_all_fields is False:
                    field_allow_null = field.__dict__.get("null")
                    if field_allow_null and field_allow_null is True:
                        fields_info.update({field_name: None})
                        continue

                fields_info.update(self.inspect_field(field, field_name))

        return fields_info

    def inspect_field(self, field: Type, field_name: str) -> Dict:
        field_type = field.get_internal_type()
        field_specs = field.__dict__
        max_length = field_specs.get("max_length")
        extra_params = {}
        if max_length:
            extra_params["max_value"] = max_length
        return {field_name: self.generate_random_data_per_field(field_type, **extra_params)}

    def generate_random_data_per_field(self, field_type: str, **kwargs):
        # BigIntegerField (min_value=10000)
        # PositiveBigIntegerField (min_value=10000)
        data_generator = {
            "DateTimeField": DjangoTestingModel.create_random_datetime,
            "DateField": DjangoTestingModel.create_random_date,
            "TimeField": DjangoTestingModel.create_random_hour,
            # "DurationField": DjangoTestingModel.create(),
            # "AutoField": DjangoTestingModel.create(),
            # "BigAutoField": DjangoTestingModel.create(),
            # "SmallAutoField": DjangoTestingModel.create(),
            # "BinaryField": DjangoTestingModel.create(),
            # "CommaSeparatedIntegerField": DjangoTestingModel.create(),
            "DecimalField": DjangoTestingModel.create_random_float,
            "FloatField": DjangoTestingModel.create_random_float,
            "BigIntegerField": DjangoTestingModel.create_random_integer,
            "PositiveBigIntegerField": DjangoTestingModel.create_random_positive_integer,
            "PositiveIntegerField": DjangoTestingModel.create_random_positive_integer,
            "PositiveSmallIntegerField": DjangoTestingModel.create_random_positive_integer,
            "IntegerField": DjangoTestingModel.create_random_integer,
            "SmallIntegerField": DjangoTestingModel.create_random_integer,
            "CharField": DjangoTestingModel.create_random_string,
            "TextField": DjangoTestingModel.create_random_text,
            "SlugField": DjangoTestingModel.create_random_slug,
            "URLField": DjangoTestingModel.create_random_url,
            "UUIDField": DjangoTestingModel.create_random_uuid,
            "EmailField": DjangoTestingModel.create_random_email,
            # "Empty": DjangoTestingModel.create(),
            # "Field": DjangoTestingModel.create(),
            # "NOT_PROVIDED": DjangoTestingModel.create(),
            # "FilePathField": DjangoTestingModel.create(),
            "FileField": self.return_none_by_now,
            "ImageField": self.return_none_by_now,
            "JSONField": DjangoTestingModel.create_random_json,
            # "GenericIPAddressField": DjangoTestingModel.create(),
            # "IPAddressField": DjangoTestingModel.create(),
            "BooleanField": DjangoTestingModel.create_random_bool,
            "NullBooleanField": DjangoTestingModel.create_random_bool,
            "ForeignKey": self.return_none_by_now,
            "OneToOneField": self.return_none_by_now,
            "ManyToManyField": self.return_none_by_now,
        }
        return data_generator[field_type](**kwargs)  # type: ignore

    def return_none_by_now(self, **kwargs):
        return None
