from time import strftime
from typing import List
from abc import ABC, abstractclassmethod
import lxml.etree as Etree
import requests
from urllib3.exceptions import InsecureRequestWarning
from xmlApiParse.enums import SpecificCollectionsEnum, AllCollectionsEnum
from xmlApiParse.repository import (
    OrderLineDTO, ParseError, ConnectionErrors, BadRequestError, SystemInfoDTO,
    WaiterListDTO, OrderDTO, RestaurantDTO,
    MenuDTO, MenuItemsDTO, EmployeeDTO, WaiterDTO,
    GetVisitDTO, CategoryDTO, TableDTO, CurrencyDTO
)


class XMLRequest(ABC):

    @abstractclassmethod
    def check_connection(self):
        pass

    @abstractclassmethod
    def send_request(self):
        pass

    @abstractclassmethod
    def get_system_info_request(self):
        pass

    @abstractclassmethod
    def all_collections_request(self):
        pass

    @abstractclassmethod
    def specific_collections_request(self):
        pass

    @abstractclassmethod
    def get_employees(self):
        pass

    @abstractclassmethod
    def get_waiters(self):
        pass

    @abstractclassmethod
    def waiter_list_request(self):
        pass

    @abstractclassmethod
    def get_orders(self):
        pass

    @abstractclassmethod
    def get_restaurants(self):
        pass

    @abstractclassmethod
    def menu_request(self):
        pass

    @abstractclassmethod
    def get_menu_items(self):
        pass

    @abstractclassmethod
    def get_categories(self):
        pass

    @abstractclassmethod
    def get_order_lines(self):
        pass

    # @abstractclassmethod
    # def get_visits(self):
    #     pass

    @abstractclassmethod
    def get_order_line_list(self):
        pass
    
    @abstractclassmethod
    def get_tables(self):
        pass
    
    @abstractclassmethod
    def get_currencies(self):
        pass


class RKXMLRequest(XMLRequest):
    media_type = "text/xml"
    connected = False

    def log(self, log_info):
        print(log_info) if self.logging else None

    def __init__(self, host: str, user_name: str, password: str, logging: bool = False):
        self.host = host
        self.user_name = user_name
        self.password = password
        self.logging = logging
        self.auth = (user_name, password)

    def check_connection(self):
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(self.host, auth=self.auth, verify=False)
            if response.status_code != 200:
                raise ConnectionErrors('Conection error')
            self.connected = True
        except Exception as error:
            raise ConnectionErrors('Conection error') from error
        return self.connected

    def send_request(self, body: str = None):
        if self.check_connection() is True:
            try:
                response = requests.get(
                    self.host, data=body, auth=self.auth, verify=False)
            except Exception as error:
                raise BadRequestError('Bad Request') from error
        return response

    def parse(self, content: str):
        """Parses the incoming bytestream as XML and returns the resulting data."""

        try:
            response = self.send_request(body=content)
            root: list = Etree.fromstring(response.content)
        except (ParseError, ValueError) as error:
            raise ParseError(f"XML parse error - {str(error)}")
        data = self._xml_convert(elements=root)
        return data

    def _xml_convert(self, elements):
        """convert the xml `element` into the corresponding python object"""

        data: dict = {}
        for num, child in enumerate(elements, 1):
            data[f"{num}-{child.tag}"] = {
                "attrib": child.attrib,
                "child":  self._xml_convert(elements=child)}
        return data

    def get_system_info_request(self) -> SystemInfoDTO:
        """request to get restaurant system info"""

        body = f'<RK7Query><RK7CMD CMD="GetSystemInfo2"/></RK7Query>'
        response = self.send_request(body=body)
        try:
            parsed_element = Etree.fromstring(response.content)
            system_info_response = parsed_element.find("./SystemInfo")

            if system_info_response is None:
                return None

            restaurant_response = system_info_response.find('Restaurant')
            restaurant = RestaurantDTO(name=restaurant_response.attrib['name'],
                                        alt_name='',
                                        ident=restaurant_response.attrib['id'])

            restaurant_code_response = system_info_response.attrib['RestCode']
            restaurant_common_shift = system_info_response.find('CommonShift')
            shift_date = restaurant_common_shift.attrib['ShiftDate']
            system_info = SystemInfoDTO(
                restaurant=restaurant,
                restaurant_code=restaurant_code_response,
                shift_date=shift_date)

            return system_info

        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")

    def all_collections_request(self, collection: AllCollectionsEnum):
        """request to get all collections"""

        body = f'<RK7Query><RK7CMD CMD="{collection}"/></RK7Query>'
        response = self.send_request(body=body)
        element_list = []
        try:
            parsed_collection = Etree.fromstring(response.content)
            for item in parsed_collection:
                collection_node = list(item.iter())
                for collections in collection_node:
                    element_list.append(collections.attrib)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return element_list

    def specific_collections_request(self, collection: SpecificCollectionsEnum):
        """request a specific collection"""

        body = f'<RK7Query><RK7CMD CMD="GetRefData" RefName = "{collection}"/></RK7Query>'
        element = []
        response = self.send_request(body=body)
        try:
            parsed_element = Etree.fromstring(response.content)
            for item in parsed_element.findall("./RK7Reference/Items/Item"):
                attr_of_item_node = item.attrib
                element.append(attr_of_item_node)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return element

    def get_employees(self, role_filter: str | None = None) -> List[EmployeeDTO]:
        """request to get all employees, can be filtered by role_filter"""

        body = ('<RK7Query><RK7CMD CMD="GetRefData" RefName="Restaurants" IgnoreEnums="1" '
                'WithChildItems="3" WithMacroProp="1" OnlyActive = "1" '
                'PropMask="RIChildItems.(Ident,Name,genRestIP,genprnStation,genDefDlvCurrency,AltName,'
                'RIChildItems.TRole(ItemIdent,passdata,Name,AltName,gen*,'
                'RIChildItems.(Code, Ident,Name,AltName,gen*)))"/></RK7Query>')
        response = self.send_request(body=body)
        employees_list: List[EmployeeDTO] = []
        try:
            tree = Etree.fromstring(response.content)
            for restaurant_node in tree.findall("./RK7Reference/RIChildItems/TRK7Restaurant"):
                restaurant_name = restaurant_node.attrib['Name']
                restaurant_ident = restaurant_node.attrib['Ident']
                for role_node in restaurant_node.findall("./RIChildItems/TRole"):
                    role = role_node.attrib['Name']
                    if role_filter==role or role_filter is None:
                        for employee in role_node.findall("./RIChildItems/TEmployee"):
                            employee_dto = EmployeeDTO(restaurant_name=restaurant_name,
                                                       restaurant_ident=restaurant_ident,
                                                       name=employee.attrib['Name'],
                                                       role=role,
                                                       altname=employee.attrib['AltName'],
                                                       gen_san_date=employee.attrib['genSanDate'],
                                                       ident=employee.attrib['Ident'],
                                                       code=employee.attrib['Code'],
                                                       gen_tax_payer_id_num=employee.attrib['genTaxPayerIdNum'])
                            employees_list.append(employee_dto)
        except (ParseError, ValueError) as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return employees_list

    def get_waiters(self) -> List[WaiterDTO]:
        waiters_list: List[WaiterDTO] = []
        employees_waiters_list = self.get_employees(role_filter="Официанты")
        for employee in employees_waiters_list:
            waiter_obj = WaiterDTO(
                restaurant_name=employee.restaurant_name,
                restaurant_ident=employee.restaurant_ident,
                name=employee.name,
                ident=employee.ident,
                code=employee.code)
            waiters_list.append(waiter_obj)
        return waiters_list

    def waiter_list_request(self) -> List[WaiterListDTO]: # тут возвращаются все работники, GetWaiterList не фильтрует данные
        """request for a list of waiters"""

        body = '<RK7Query><RK7CMD CMD="GetWaiterList"/></RK7Query>'
        response = self.send_request(body=body)
        elements = []
        try:
            parsed_element = Etree.fromstring(response.content)
            for item in parsed_element:
                for element in item:
                    waiter_id = element.attrib['ID']
                    code = element.attrib['Code']
                    waiter_dto = WaiterListDTO(id=waiter_id, code=code)
                    elements.append(waiter_dto)
        except (ParseError, ValueError) as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return elements

    def get_orders(self, last_version: int | None = None,
                           only_opened: bool = False) -> tuple[List[OrderDTO], int | None]:
        """requests to receive latest orders"""

        last_version_represent = f'lastversion="{last_version}"' if last_version else ''
        only_opened = f'onlyOpened="{only_opened}"' if only_opened else ''

        body = f'<RK7Query><RK7Command2 CMD="GetOrderList"{last_version_represent}{only_opened}/></RK7Query>'
        response = self.send_request(body=body)
        orders_list: List[OrderDTO] = []
        try:
            parsed_element = Etree.fromstring(response.content)
            for item in parsed_element.findall(".//Visit"):
                visit = item.attrib
                if item[0].tag == "Guests":
                    order = item[1][0].attrib
                    order_obj = OrderDTO(visit_id=visit.get('VisitID'),
                                             order_id=order.get('OrderID'),
                                             count_guest=visit.get(
                                                 'GuestsCount'),
                                             order_name=order.get('OrderName'),
                                             url=(order.get('Url')),
                                             version=order.get('Version'),
                                             crc32=int(order.get('crc32')),
                                             guid=order.get('guid'),
                                             table_id=(order.get('TableID')),
                                             table_code=order.get('TableCode'),
                                             order_categ_id=order.get(
                                                 'OrderCategId'),
                                             order_categ_code=order.get(
                                                 'OrderCategCode'),
                                             bill=order.get('Bill'),
                                             waiter_id=order.get('WaiterID'),
                                             order_type_code=order.get(
                                                 'OrderTypeCode'),
                                             order_type_id=order.get(
                                                 'OrderTypeID'),
                                             to_pay_sum=order.get('ToPaySum'),
                                             waiter_code=order.get(
                                                 'WaiterCode'),
                                             order_sum=order.get('OrderSum'),
                                             total_pieces=order.get(
                                                 'TotalPieces'),
                                             finished=order.get('Finished'),
                                             price_list_sum=order.get(
                                                 'PriceListSum'),
                                             dessert=order.get('Dessert'),
                                             created_time=order.get(
                                                 'CreateTime'),
                                             finished_time=order.get('FinishTime'))
                    orders_list.append(order_obj)
            last_version_str = parsed_element.find('CommandResult').attrib.get(
                "lastversion") if parsed_element.find('CommandResult') is not None else None
            last_version = int(last_version_str) if last_version_str else None
        except (ParseError, ValueError) as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return orders_list, last_version

    def get_restaurants(self) -> List[RestaurantDTO]:
        """requests to get restaurants"""

        body = '<RK7Query> <RK7CMD CMD="GetRefData" RefName="Restaurants" ' \
            'IgnoreEnums="1" WithChildItems="3" WithMacroProp="1" ' \
            'OnlyActive = "1" PropMask="RIChildItems.(Ident,Name,genRestIP,genprnStation,' \
            'genDefDlvCurrency,AltName,RIChildItems.TRole(ItemIdent,passdata,Name,AltName,gen*,' \
            'RIChildItems.(Code,Ident,Name,AltName,gen*)))" /></RK7Query>'
        response = self.send_request(body=body)
        restaurants: List[RestaurantDTO] = []
        parsed_element = Etree.fromstring(response.content)
        try:
            for item in parsed_element.findall("./RK7Reference/RIChildItems/TRK7Restaurant"):
                restaurant_obj = RestaurantDTO(name=item.attrib['Name'],
                                                alt_name=item.attrib['AltName'],
                                                ident=item.attrib['Ident'])
                restaurants.append(restaurant_obj)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return restaurants

    def menu_request(self, code: int) -> List[MenuDTO]:
        """getting dishes available for sale"""

        body = f'<RK7Query><RK7CMD CMD="GetOrderMenu" StationCode="{code}" DateTime="{strftime("%Y-%m-%d %H:%M:%S")}" /></RK7Query>'
        response = self.send_request(body=body)
        elements = []
        try:
            parsed_element = Etree.fromstring(response.content)
            for item in parsed_element.findall("./Dishes/Item"):
                attr_of_item_node = (item.attrib)
                ident = attr_of_item_node['Ident']
                price = attr_of_item_node['Price']
                menudto = MenuDTO(ident=ident, price=price)
                elements.append(menudto)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return elements

    def get_menu_items(self, name_filter: str = None) -> List[MenuItemsDTO]:
        """For a complete list of dishes or a specific dish"""

        body = '<RK7Query><RK7CMD CMD="GetRefData" RefName = "MENUITEMS"/></RK7Query>'
        response = self.send_request(body=body)
        menu_items_list: List[MenuItemsDTO] = []
        try:
            parsed_element = Etree.fromstring(response.content)
            for item in parsed_element.findall("./RK7Reference/Items/Item"):
                if item.attrib['Status'] == 'rsActive' and item.attrib['ActiveHierarchy'] == 'true':
                    if item.attrib.get('Name') == name_filter:
                        return item.attrib
                    menu_items_obj = MenuItemsDTO(
                        ident=item.attrib['Ident'], item_ident=item.attrib['ItemIdent'],
                        source_ident=item.attrib['SourceIdent'], guid=item.attrib['GUIDString'],
                        assign_childs_on_server=item.attrib['AssignChildsOnServer'],
                        active_hierarchy=item.attrib['ActiveHierarchy'], code=item.attrib['Code'],
                        name=item.attrib['Name'], alt_name=item.attrib['AltName'],
                        main_parent_ident=item.attrib['MainParentIdent'], status=item.attrib['Status'],
                        sales_terms_start_sale=item.attrib['SalesTerms_StartSale'],
                        sales_terms_stop_sale=item.attrib['SalesTerms_StopSale'],
                        future_tax_dish_type=item.attrib['FutureTaxDishType'],  parent=item.attrib['Parent'],
                        cook_mins=item.attrib['CookMins'], modi_weight=item.attrib['ModiWeight'],
                        min_rest_qnt=item.attrib['MinRestQnt'], categ_path=item.attrib['CategPath'],
                        price_mode=item.attrib['PriceMode'], modi_scheme=item.attrib['ModiScheme'],
                        combo_scheme=item.attrib['ComboScheme'], kurs=item.attrib['Kurs'],
                        qnt_dec_digits=item.attrib['QntDecDigits'], comment=item.attrib['Comment'],
                        instruct=item.attrib['Instruct'], flags=item.attrib['Flags'],
                        tara_weight=item.attrib['TaraWeight'], confirm_qnt=item.attrib['ConfirmQnt'],
                        bar_codes=item.attrib['BarCodes'], open_price=item.attrib['OpenPrice'],
                        change_qnt_once=item.attrib['ChangeQntOnce'],
                        use_rest_control=item.attrib['UseRestControl'],
                        use_confirm_qnt=item.attrib['UseConfirmQnt'],
                        bar_codes_full_info=item.attrib['BarcodesFullInfo'],
                        item_kind=item.attrib['ItemKind'],
                        tariff_round_rule=item.attrib['TariffRoundRule'],
                        combo_discount=item.attrib['ComboDiscount'],
                        money_round_rule=item.attrib['MoneyRoundRule'], round_time=item.attrib['RoundTime'],
                        guests_dish_rating=item.attrib['GuestsDishRating'], rate_type=item.attrib['RateType'],
                        right_lvl=item.attrib['RightLvl'],
                        minimum_tarif_time=item.attrib['MinimumTarifTime'],
                        maximum_tarif_time=item.attrib['MaximumTarifTime'],
                        ignored_tarif_time=item.attrib['IgnoredTarifTime'],
                        min_tarif_amount=item.attrib['MinTarifAmount'],
                        max_tarif_amount=item.attrib['MaxTarifAmount'],
                        availability_schedule=item.attrib['AvailabilitySchedule'],
                        dont_pack=item.attrib['DontPack'], portion_weight=item.attrib['PortionWeight'],
                        portion_name=item.attrib['PortionName'])
                    menu_items_list.append(menu_items_obj)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return menu_items_list

    def get_categories(self) -> List[CategoryDTO]:
        body = '<RK7Query><RK7CMD CMD="GetRefData" RefName = "CATEGLIST" IgnoreEnums="1" WithChildItems="3"' \
            'WithMacroProp="1" OnlyActive = "1"/></RK7Query>'
        categories: List[CategoryDTO] = []
        response = self.send_request(body=body)
        try:
            parsed_element = Etree.fromstring(response.content)
            for category in parsed_element.findall("./RK7Reference/Items/"):
                attr_of_item_node = category.attrib
                category_obj = CategoryDTO(
                    ident=attr_of_item_node.get('Ident'),
                    name=attr_of_item_node.get('Name'),
                    active_hierarchy=attr_of_item_node.get('ActiveHierarchy'),
                    main_parent_ident=attr_of_item_node.get('MainParentIdent')
                )
                categories.append(category_obj)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return categories

    # def get_visits(self):
    #     body = '<RK7Query><RK7CMD CMD="GetOrderList"/></RK7Query>'
    #     response = self.send_request(body=body)
    #     element_list = []
    #     guid = []
    #     try:
    #         parsed_element = Etree.fromstring(response.content)
    #         for item in parsed_element.findall("./Visit"):
    #             if item[0].tag == "Guests":
    #                 order = item[1][0].attrib
    #                 order_dto = GetVisitDTO(
    #                     order_id=order.get('OrderID'), guid=order.get('guid'))
    #                 guid.append(order.get('guid'))
    #                 element_list.append(order_dto)
    #     except (ParseError, ValueError) as error:
    #         raise ParseError(f"XML parse error - {str(error)}")
    #     return guid

    @staticmethod
    def get_detailed_order_query(order_guid: str) -> str:
        return f'<RK7Command CMD="GetOrder"><Order guid="{order_guid}"/></RK7Command>'

    def get_order_lines(self, order_guids:list[str]) -> List[OrderLineDTO]:
        orders_line_list: List[OrderLineDTO] = []
        orders_query = ''.join(RKXMLRequest.get_detailed_order_query(
            order_guid=order_guid) for order_guid in order_guids)
        body = f'<RK7Query>{orders_query}</RK7Query>'
        response = self.send_request(body=body)
        parsed_collection = Etree.fromstring(response.content)
        for order in parsed_collection.findall('./CommandResult/Order'):
            order_item = order.attrib
            for dish in order.findall('./Session/Dish'):
                attr_of_item_node = dish.attrib
                for modi in order.findall('./Session/Dish/Modi'):
                    modi_item = modi.attrib
                    order_obj = OrderLineDTO(
                        order_guid=order_item.get('guid'),
                        line_guid=attr_of_item_node.get('line_guid'),
                        dish_id=attr_of_item_node.get('id'),
                        dish_name=attr_of_item_node.get('name'),
                        quantity=int(attr_of_item_node.get('quantity')) / 1000,
                        modi=modi_item.get('name'))
                    orders_line_list.append(order_obj)
        return orders_line_list

    def get_order_line_list(self, order_guids:list[str]) -> List[OrderLineDTO]:
        orders_line_list: List[OrderLineDTO] = []
        orders_query = ''.join(RKXMLRequest.get_detailed_order_query(
            order_guid=order_guid) for order_guid in order_guids)
        body = f'<RK7Query>{orders_query}</RK7Query>'

        response = self.send_request(body=body)
        parsed_collection = Etree.fromstring(response.content)
        for order in parsed_collection.findall('./CommandResult/Order'):
            order_item = order.attrib
            for dish in order.findall('./Session/Dish'):
                attr_of_item_node = dish.attrib
                modifications = []

                for modi in dish.findall('./Modi'):
                    modi_item = modi.attrib
                    modifications.append(modi_item.get('name'))

                order_obj = OrderLineDTO(
                        order_guid=order_item.get('guid'),
                        line_guid=attr_of_item_node.get('line_guid'),
                        dish_id=attr_of_item_node.get('id'),
                        dish_name=attr_of_item_node.get('name'),
                        quantity=int(attr_of_item_node.get('quantity')) / 1000,
                        modi=', '.join(modifications))

                orders_line_list.append(order_obj)
        return orders_line_list

    def get_tables(self) -> List[TableDTO]:
        body = f'<RK7Query><RK7CMD CMD="GetRefData" RefName = "Tables"/></RK7Query>'
        tables: List[TableDTO] = []
        response = self.send_request(body=body)
        try:
            parsed_element = Etree.fromstring(response.content)
            for table in parsed_element.findall("./RK7Reference/Items/Item"):
                attr_of_item_node = table.attrib
                table_obj = TableDTO(
                    ident=attr_of_item_node.get('Ident'),
                    name = attr_of_item_node.get('Name')
                )
                tables.append(table_obj)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return tables
    
    def get_currencies(self) -> List[CurrencyDTO]:
        body = f'<RK7Query><RK7CMD CMD="GetRefData" RefName = "CURRENCIES"/></RK7Query>'
        currencies: List[CurrencyDTO] = []
        response = self.send_request(body=body)
        try:
            parsed_element = Etree.fromstring(response.content)
            for currency in parsed_element.findall("./RK7Reference/Items/Item"):
                attr_of_item_node = currency.attrib
                currency_obj = CurrencyDTO(
                    ident=attr_of_item_node.get('Ident'),
                    name = attr_of_item_node.get('Name')
                )
                currencies.append(currency_obj)
        except Exception as error:
            raise ParseError(f"XML parse error - {str(error)}")
        return currencies
