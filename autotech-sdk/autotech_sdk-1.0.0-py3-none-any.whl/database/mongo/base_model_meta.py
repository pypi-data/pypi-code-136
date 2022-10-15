from .setup_collection import register_collection


class BaseModelMeta(type):
    """
    This is a metaclass for create class model and register indexes of collection
    Read more about metaclass in python here: https://viblo.asia/p/metaclass-in-python-gDVK24JnlLj
    """
    def __new__(mcs, class_name, supers, class_dict):
        """
        Auto add class variable COLLECTION_NAME to class model
        """

        created_class = super().__new__(mcs, class_name, supers, class_dict)
        collection_name = created_class.__name__.lower()
        created_class.COLLECTION_NAME = collection_name

        if collection_name != 'basemongodb':
            register_collection(created_class)
        return created_class
