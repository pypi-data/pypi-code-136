from odoo import models,fields,api
from odoo.tools.translate import _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    reference = fields.Char(string=_("Reference"))

    product_customer_code = fields.Char(
        string="Product Customer Code",
    )

    @api.onchange("product_id")
    def product_id_change(self):
        result = super(SaleOrderLine, self).product_id_change()
        for line in self.filtered(
            lambda sol: sol.product_id.product_tmpl_id.customer_ids
            and sol.order_id.pricelist_id.item_ids
        ):
            product = line.product_id
            if product:
                supplierinfo = line.product_id._select_customerinfo(
                    partner=line.order_partner_id
                )
                line.product_customer_code = supplierinfo.product_code
                line.reference = product.default_code
            else:
                line.reference = False
                line.product_customer_code = False
