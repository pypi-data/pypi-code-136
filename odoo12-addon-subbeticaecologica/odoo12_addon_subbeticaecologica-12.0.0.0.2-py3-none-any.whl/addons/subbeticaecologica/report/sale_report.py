from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    carrier_id = fields.Char('Delivery method', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['carrier_id'] = ", s.carrier_id as carrier_id"
        groupby += ', s.carrier_id'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
