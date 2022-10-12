# coding: utf-8

from m3_gar_client.backends.base import BackendBase as AbstractBackend

from .utils import (
    find_address_objects,
    find_house,
    get_address_object,
    get_house,
    get_stead
)


class BackendBase(AbstractBackend):

    """Базовый бекенд для проксей к m3-rest-gar."""

    def find_address_objects(
        self,
        filter_string,
        levels=None,
        typenames=None,
        parent_id=None,
        timeout=None,
    ):
        """Возвращает адресные объекты, соответствующие параметрам поиска.

        :param unicode filter_string: Строка поиска.
        :param levels: Уровни адресных объектов, среди которых нужно осуществлять поиск.
        :param typenames: Наименования типов адресных объектов, среди которых нужно осуществлять поиск.
        :param parent_id: ID родительского объекта.
        :param float timeout: Timeout запросов к серверу ГАР в секундах.

        :rtype: generator
        """
        return find_address_objects(filter_string, levels, typenames, parent_id, timeout)

    def get_address_object(self, obj_id, timeout=None):
        """Возвращает адресный объект ГАР по его ID.

        :param obj_id: ID адресного объекта ГАР.
        :param float timeout: Timeout запросов к серверу ГАР в секундах.

        :rtype: m3_gar_client.data.AddressObject
        """
        return get_address_object(obj_id, timeout)

    def find_house(self, house_number, parent_id, building_number, structure_number, timeout=None):
        """Возвращает информацию о здании по его номеру.

        :param unicode house_number: Номер дома.
        :param parent_id: ID родительского объекта.
        :param unicode building_number: Номер корпуса.
        :param unicode structure_number: Номер строения.
        :param float timeout: Timeout запросов к серверу ГАР в секундах.

        :rtype: m3_gar_client.data.House or NoneType
        """
        return find_house(house_number, parent_id, building_number, structure_number, timeout)

    def get_house(self, house_id, timeout=None):  # pylint: disable=signature-differs
        """Возвращает информацию о здании по его ID в ГАР.

        :param house_id: ID здания.
        :param float timeout: Timeout запросов к серверу ГАР в секундах.

        :rtype: m3_gar_client.data.House
        """
        return get_house(house_id, timeout)

    def get_stead(self, stead_id, timeout=None):
        """Возвращает информацию о земельном участке по его ID в ГАР."""
        return get_stead(stead_id, timeout)
