# This file is part of Tryton. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from decimal import Decimal

from trytond.model import (
    ModelView, ModelSQL, ModelStorage, sequence_ordered, fields)
from trytond.pyson import Eval, If, Bool
from trytond.pool import PoolMeta, Pool
from trytond.transaction import Transaction

from trytond.modules.product import round_price

try:
    from nereid import url_for
except ImportError:
    pass


class Template(metaclass=PoolMeta):
    __name__ = "product.template"

    components = fields.One2Many(
        'product.component', 'parent_template', "Components")

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls.type.selection.append(('kit', "Kit"))

    @classmethod
    def _cost_price_method_domain_per_type(cls):
        types_cost_method = super()._cost_price_method_domain_per_type()
        types_cost_method['kit'] = [('cost_price_method', '=', 'fixed')]
        return types_cost_method

    @fields.depends('type', 'cost_price_method')
    def on_change_type(self):
        super().on_change_type()
        if self.type == 'kit':
            self.cost_price_method = 'fixed'

    @classmethod
    def copy(cls, templates, default=None):
        pool = Pool()
        Component = pool.get('product.component')
        if default is None:
            default = {}
        else:
            default = default.copy()

        copy_components = 'components' not in default
        default.setdefault('components', None)
        new_templates = super().copy(templates, default)
        if copy_components:
            old2new = {}
            to_copy = []
            for template, new_template in zip(templates, new_templates):
                to_copy.extend(
                    c for c in template.components if not c.product)
                old2new[template.id] = new_template.id
            if to_copy:
                Component.copy(to_copy, {
                        'parent_template': (lambda d:
                            old2new[d['parent_template']]),
                        })
        return new_templates


class Product(metaclass=PoolMeta):
    __name__ = "product.product"

    components = fields.One2Many(
        'product.component', 'parent_product', "Components")

    def get_multivalue(self, name, **pattern):
        pool = Pool()
        Uom = pool.get('product.uom')
        value = super().get_multivalue(name, **pattern)
        if name == 'cost_price' and self.type == 'kit':
            value = Decimal(0)
            for component in self.components_used:
                cost_price = component.product.get_multivalue(
                    'cost_price', **pattern)
                cost_price = Uom.compute_price(
                    component.product.default_uom, cost_price, component.unit)
                value += cost_price * Decimal(str(component.quantity))
            value = round_price(value)
        return value

    @property
    def components_used(self):
        return self.components or self.template.components

    @classmethod
    def get_quantity(cls, products, name):
        pool = Pool()
        Uom = pool.get('product.uom')
        Product = pool.get('product.product')

        def get_kit_quantity(kit):
            qties = []
            for component in kit.components_used:
                product = Product(component.product.id)
                product_stock = getattr(product, name)
                # If any component is missing, no need to calculate further
                if product_stock <= 0:
                    return 0
                component_qty = Uom.compute_qty(
                    component.product.default_uom,
                    product_stock,
                    component.unit, round=False)
                if not component.fixed:
                    component_qty /= component.quantity
                qties.append(component_qty)
            return kit.default_uom.floor(min(qties, default=0))

        quantities = super().get_quantity(products, name)
        kits = [p for p in products if p.type == 'kit']
        for kit in kits:
            quantities[kit.id] = get_kit_quantity(kit)
        return quantities

    @classmethod
    def copy(cls, products, default=None):
        pool = Pool()
        Component = pool.get('product.component')
        if default is None:
            default = {}
        else:
            default = default.copy()

        copy_components = 'components' not in default
        if 'template' in default:
            default.setdefault('components', None)
        new_products = super().copy(products, default)
        if 'template' in default and copy_components:
            template2new = {}
            product2new = {}
            to_copy = []
            for product, new_product in zip(products, new_products):
                if product.components:
                    to_copy.extend(product.components)
                    template2new[product.template.id] = new_product.template.id
                    product2new[product.id] = new_product.id
            if to_copy:
                Component.copy(to_copy, {
                        'parent_product': (lambda d:
                            product2new[d['parent_product']]),
                        'parent_template': (lambda d:
                            template2new[d['parent_template']]),
                        })
        return new_products

    def serialize(self, purpose=None):
        '''
        Return a serializable dictionary suitable for use with
        components display
        '''
        result = super().serialize(purpose)

        result['kit'] = self.type == 'kit'
        result['kit_lines'] = [{
                'id': line.product.id,
                'rec_name': line.product.rec_name,
                'url': url_for('product.product.render', uri=line.product.uri),
                } for line in self.components_used]
        return result

    @classmethod
    def products_by_location(cls, location_ids,
            with_childs=False, grouping=('product',), grouping_filter=None):
        """
        For kits compute only for storage location the quantities
        of the components and return the stock as the minimal quantity
        of the least one.
        """
        pool = Pool()
        Location = pool.get('stock.location')

        product_id = Transaction().context.get('product')
        calculate_components = False
        if product_id:
            product, = cls.browse([product_id])
            if product.type == 'kit':
                calculate_components = True
        if not product_id or not calculate_components:
            return super().products_by_location(location_ids,
                with_childs=with_childs, grouping=grouping,
                grouping_filter=grouping_filter)

        # Since this is a virtual number that applies only for the current
        # availability of a kit we consider only the storage location and
        # take that number also for the warehouse
        quantities = {}
        warehouses = Location.search([
                    ('type', '=', 'warehouse'),
                    ], order=[('left', 'DESC')])
        if warehouses:
            warehouse = warehouses[0]
        else:
            return quantities

        storage_id = warehouse.storage_location.id
        kit_stock = 0.0
        for component in product.components:
            component_id = component.product.id
            with Transaction().set_context(product=component_id):
                comp_stock = cls.products_by_location([storage_id],
                    with_childs=with_childs, grouping=grouping,
                    grouping_filter=([component_id],))
                if comp_stock:
                    qty = next(iter(comp_stock.values()))
                    if not kit_stock:
                        kit_stock = qty
                    else:
                        kit_stock = min(kit_stock, qty)

        if kit_stock:
            quantities = {
                (storage_id, product_id): kit_stock,
                (warehouse.id, product_id): kit_stock
                }
        return quantities


class ProductVariant(metaclass=PoolMeta):
    __name__ = "product.product"

    list_price_method = fields.Selection([
            ('fixed', 'Fixed Price'),
            ('list_price', 'Sum of component list prices'),
            ], 'List Price Method',
        states={
            'invisible': Eval('type') != 'kit',
            },
        depends=['type'], help='Select the method to calculate the '
        'kit list price.\n'
        'Note: the sale price of a component is calculated with evtl. '
        'price lists for the component in effect.')

    @staticmethod
    def default_list_price_method():
        return 'fixed'

    def get_multivalue(self, name, **pattern):
        pool = Pool()
        Uom = pool.get('product.uom')
        value = super().get_multivalue(name, **pattern)
        if (name == 'list_price'
                and self.type == 'kit'
                and self.list_price_method != 'fixed'):
            value = Decimal(0)
            for component in self.components_used:
                list_price = component.product.get_multivalue(
                    'list_price', **pattern)
                list_price = Uom.compute_price(
                    component.product.default_uom, list_price, component.unit)
                value += list_price * Decimal(str(component.quantity))
            value = round_price(value)
        return value


class ProductSale(metaclass=PoolMeta):
    __name__ = "product.product"

    components_in_description = fields.Boolean('Components in description',
        states={
            'invisible': Eval('type') != 'kit',
            }, depends=['type'],
        help='When activated, the components of the kit will be added to '
        'the sale line description.')

    @classmethod
    def __setup__(cls):
        super().__setup__()
        if hasattr(cls, 'list_price_method'):
            selection = ('sale_price', 'Sum of component sale prices')
            if selection not in cls.list_price_method.selection:
                cls.list_price_method.selection.append(selection)

    @staticmethod
    def default_components_in_description():
        return True

    def compute_shipping_date(self, date=None):
        Date = Pool().get('ir.date')

        if self.type == 'kit':
            shipping_date = Date.today()
            for component in self.components:
                shipping_date = min(shipping_date,
                    component.product.compute_shipping_date(date))
        else:
            shipping_date = super(Product, self).compute_shipping_date(
                date=date)
        return shipping_date


class ProductSalePriceList(metaclass=PoolMeta):
    __name__ = "product.product"

    def _get_kit_price_list(self):
        '''
        Provide an extensible method to specify distinct pricelists for the
        calculation of kit products when based on sale price of their
        components, e.g. for use with nested pricelists when you do not want to
        apply the complete pricelist chain onto the kit again where it was
        already applied onto the components.
        '''
        return Transaction().context.get('price_list')

    @classmethod
    def get_sale_price(cls, products, quantity=0):
        '''
        Use component sale prices when composing the kit price
        '''
        pool = Pool()
        Uom = pool.get('product.uom')
        PriceList = pool.get('product.price_list')
        Party = pool.get('party.party')
        Tax = pool.get('account.tax')

        context = Transaction().context

        def _get_sale_price(prices, products, quantity=0):
            # This is basically an adapted monkey patch of
            # sale_price_list/sale/get_sale_price, but without doing super()
            if context.get('price_list'):
                price_list = PriceList(Transaction().context['price_list'])
                customer = None
                if context.get('customer'):
                    customer = Party(context['customer'])
                context_uom = None
                if context.get('uom'):
                    context_uom = Uom(Transaction().context['uom'])
                taxes = None
                if context.get('taxes'):
                    taxes = Tax.browse(context.get('taxes'))
                for product in products:
                    uom = context_uom or product.sale_uom
                    if uom.category != product.sale_uom.category:
                        uom = product.sale_uom
                    price = price_list.compute(
                         customer, product, prices[product.id], quantity, uom)
                    if price_list.tax_included and taxes:
                        price = Tax.reverse_compute(price, taxes)
                    prices[product.id] = price
            return prices

        prices = {}

        uom = None
        if context.get('uom'):
            uom = Uom(context.get('uom'))

        non_kits = []
        for product in products:
            if (product.type != 'kit'
                    or (getattr(product, 'list_price_method', None)
                        != 'sale_price')):
                non_kits.append(product)
                continue

            product_price = Decimal('0.0')
            for component in product.components_used:
                with Transaction().set_context(uom=component.unit):
                    product_price += (cls.get_sale_price([component.product],
                            quantity=component.quantity)[component.product.id]
                        * Decimal(str(component.quantity)))
            if uom:
                product_price = Uom.compute_price(
                    product.default_uom, product_price, uom)
            prices[product.id] = product_price
            # The kit itself could be part of a price list, so we need to
            # run here _get_sale_price_list
            kit_price_list = product._get_kit_price_list()
            with Transaction().set_context(price_list=kit_price_list):
                prices = _get_sale_price(prices, [product], quantity=quantity)

        if non_kits:
            prices.update(super(Product, cls).get_sale_price(non_kits,
                    quantity))
        return prices


class ComponentMixin(sequence_ordered(), ModelStorage):

    parent_type = fields.Function(fields.Selection(
            'get_product_types', "Parent Type"), 'on_change_with_parent_type')
    product = fields.Many2One(
        'product.product', "Product", required=True,
        domain=[
            ('components', '=', None),
            ('template.components', '=', None),
            If(Eval('parent_type') == 'kit',
                ('type', '=', 'goods'),
                ()),
            ],
        depends=['parent_type'])
    product_unit_category = fields.Function(
        fields.Many2One('product.uom.category', "Product Unit Category"),
        'on_change_with_product_unit_category')
    quantity = fields.Float(
        "Quantity", required=True,
        digits=(16, Eval('unit_digits', 2)),
        depends=['unit_digits'])
    unit = fields.Many2One('product.uom', "Unit", required=True,
        domain=[
            If(Bool(Eval('product_unit_category')),
                ('category', '=', Eval('product_unit_category')),
                ('category', '!=', -1)),
            ],
        depends=['product', 'product_unit_category'])
    unit_digits = fields.Function(fields.Integer('Unit Digits'),
        'on_change_with_unit_digits')
    fixed = fields.Boolean("Fixed",
        help="Check to make the quantity of the component independent "
        "of the kit quantity.")

    @classmethod
    def get_product_types(cls):
        pool = Pool()
        Product = pool.get('product.product')
        return Product.fields_get(['type'])['type']['selection']

    def on_change_with_parent_type(self, name):
        raise NotImplementedError

    @property
    def parent_uom(self):
        raise NotImplementedError

    @fields.depends('product', 'unit', 'quantity',
        methods=['on_change_with_product_unit_category'])
    def on_change_product(self):
        if self.product:
            self.product_unit_category = (
                self.on_change_with_product_unit_category())
            if (not self.unit
                    or self.unit.category != self.product_unit_category):
                self.unit = self.product.default_uom

    @fields.depends('product')
    def on_change_with_product_unit_category(self, name=None):
        if self.product:
            return self.product.default_uom.category.id

    @fields.depends('unit')
    def on_change_with_unit_digits(self, name=None):
        if self.unit:
            return self.unit.digits

    def get_line(self, Line, quantity, unit, **values):
        pool = Pool()
        Uom = pool.get('product.uom')
        line = Line(product=self.product, **values)
        line.unit = self.unit
        if self.fixed:
            line.quantity = self.quantity
        else:
            quantity = Uom.compute_qty(
                unit, quantity, self.parent_uom, round=False)
            line.quantity = self.unit.round(quantity * self.quantity)
        return line

    def get_rec_name(self, name):
        pool = Pool()
        Lang = pool.get('ir.lang')
        lang = Lang.get()
        return (lang.format(
                '%.*f', (self.unit.digits, self.quantity))
            + '%s %s' % (
                self.unit.symbol, self.product.rec_name))

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('product.rec_name',) + tuple(clause[1:]),
            ]


class Component(ComponentMixin, ModelSQL, ModelView):
    "Product Component"
    __name__ = "product.component"

    parent_template = fields.Many2One(
        'product.template', "Parent Product",
        required=True, ondelete='CASCADE', select=True,
        domain=[
            If(Bool(Eval('parent_product')),
                ('products', '=', Eval('parent_product')),
                ()),
            ],
        depends=['parent_product'])
    parent_product = fields.Many2One(
        'product.product', "Parent Variant", ondelete='CASCADE', select=True,
        domain=[
            If(Bool(Eval('parent_template')),
                ('template', '=', Eval('parent_template')),
                ()),
            ],
        depends=['parent_template'])

    @classmethod
    def __setup__(cls):
        super().__setup__()
        cls.__access__.update(['parent_template', 'parent_product'])

    @fields.depends(
        'parent_product', '_parent_parent_product.template')
    def on_change_parent_product(self):
        if self.parent_product:
            self.parent_template = self.parent_product.template

    @fields.depends(
        'parent_template', '_parent_parent_template.type',
        'parent_product', '_parent_parent_product.type')
    def on_change_with_parent_type(self, name=None):
        if self.parent_product:
            return self.parent_product.type
        elif self.parent_template:
            return self.parent_template.type

    @property
    def parent_uom(self):
        if self.parent_product:
            return self.parent_product.default_uom
        elif self.parent_template:
            return self.parent_template.default_uom

    def get_rec_name(self, name):
        return super().get_rec_name(name) + (
            ' @ %s' % (
                self.parent_product.rec_name if self.parent_product
                else self.parent_template.rec_name))

    @classmethod
    def search_rec_name(cls, name, clause):
        return super().search_rec_name(name, clause) + [
            ('parent_product.rec_name',) + tuple(clause[1:]),
            ('parent_template.rec_name',) + tuple(clause[1:]),
            ]
