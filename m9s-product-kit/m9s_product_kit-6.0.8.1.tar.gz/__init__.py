# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import Pool
from . import inventory
from . import product
from . import sale
from . import purchase
from . import stock
from . import account

__all__ = ['register']


def register():
    Pool.register(
        product.Template,
        product.Product,
        product.Component,
        module='product_kit', type_='model')
    Pool.register(
        product.ProductVariant,
        module='product_kit', type_='model', depends=['product_variant'])
    Pool.register(
        account.Invoice,
        account.InvoiceLine,
        module='product_kit', type_='model', depends=['account_invoice_stock'])
    Pool.register(
        inventory.InventoryLine,
        stock.Move,
        module='product_kit', type_='model', depends=['stock'])
    Pool.register(
        product.ProductSale,
        sale.Sale,
        sale.Line,
        sale.LineComponent,
        sale.LineComponentIgnoredMove,
        sale.LineComponentRecreatedMove,
        stock.MoveSale,
        account.InvoiceLineSale,
        module='product_kit', type_='model', depends=['sale'])
    Pool.register(
        product.ProductSalePriceList,
        module='product_kit', type_='model', depends=['sale_price_list'])
    Pool.register(
        sale.HandleShipmentException,
        module='product_kit', type_='wizard', depends=['sale'])
    Pool.register(
        sale.Amendment,
        sale.AmendmentLine,
        module='product_kit', type_='model', depends=['sale_amendment'])
    Pool.register(
        purchase.Purchase,
        purchase.ProductSupplier,
        purchase.Line,
        purchase.LineComponent,
        purchase.LineComponentIgnoredMove,
        purchase.LineComponentRecreatedMove,
        stock.MovePurchase,
        account.InvoiceLinePurchase,
        module='product_kit', type_='model', depends=['purchase'])
    Pool.register(
        purchase.HandleShipmentException,
        module='product_kit', type_='wizard', depends=['purchase'])
    Pool.register(
        purchase.Amendment,
        purchase.AmendmentLine,
        module='product_kit', type_='model', depends=['purchase_amendment'])
