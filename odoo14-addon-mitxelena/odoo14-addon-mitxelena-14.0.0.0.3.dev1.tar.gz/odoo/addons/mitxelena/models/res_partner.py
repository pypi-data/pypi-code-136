from odoo import models,fields,api
from odoo.tools.translate import _

class ResPartner(models.Model):
    _inherit = "res.partner"

    customer_product_template_ids = fields.One2many(
        'product.template',
        string=_("Related products as customer"),
        compute="_compute_customer_product_template_ids")

    customer_product_template_ids_count = fields.Integer(
        string=_("Related products as customer count"),
        compute="_compute_customer_product_template_ids_count")

    def _compute_customer_product_template_ids(self):
        for record in self:
            product_template_ids = []
            product_customerinfo_ids = self.env['product.customerinfo'].search([('name','=',record.id)])
            if product_customerinfo_ids.exists():
                for product_customerinfo in product_customerinfo_ids:
                    if product_customerinfo.product_tmpl_id:
                        product_template_ids.append((4,product_customerinfo.product_tmpl_id.id))
                record.customer_product_template_ids = product_template_ids
            else:
                record.customer_product_template_ids = False

    def _compute_customer_product_template_ids_count(self):
        for record in self:
            record.customer_product_template_ids_count = len(record.customer_product_template_ids)

    def show_related_customer_products(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('sale.product_template_action')
        if action:
            # TODO: define view_id to pass tree view
            action.update(
                context=dict(self.env.context, group_by=False),
                domain=[('id', 'in', self.customer_product_template_ids.mapped('id'))]
            )
            return action
        return False