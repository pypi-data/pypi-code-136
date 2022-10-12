from odoo import models,fields,api
from odoo.tools.translate import _

class ProductTemplate(models.Model):
    _name="product.template"

    _inherit = ["product.template","base.revision"]

    state = fields.Selection([
        ('active', 'Active product'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='active')

    current_revision_id = fields.Many2one(
        comodel_name="product.template"
    )
    old_revision_ids = fields.One2many(
        comodel_name="product.template"
    )

    # Relation between product and customer
    customer_ids = fields.One2many(
        comodel_name="product.customerinfo",
        inverse_name="product_tmpl_id",
        string="Customer",
        copy=True
    )

    # Overwrite as sales.order can be multi-company
    _sql_constraints = [
        (
            "revision_unique",
            "unique(unrevisioned_name, revision_number, company_id)",
            "Product Reference and revision must be unique per Company.",
        )
    ]

    use_case = fields.Selection([
        ('prensas', 'Prensas'),
        ('naval', 'Naval'),
        ('eolico', 'Eólico'),
        ('petroquimica', 'Petroquímica'),
        ('siderurgica', 'Siderúrgica'),
        ('hydro', 'Hydro'),
        ('oiletagas', 'Oil & Gas'),
        ('mecanizado', 'Mecanizado'),
        ('energia', 'Energía'),
        ('aeronautica', 'Aeronáutica'),
        ('papel', 'Papel'),
        ('otros', 'Otros')
        ], 
        string='Aplicación',
        required=True
        )


    sizes = fields.Text(
        related="engspecsheet.description",
        string="Sizes"
    )

    # Used on create_revision
    @api.model
    def default_get(self, fields):
        res = super(ProductTemplate, self).default_get(fields)
        # Fields not copied by default
        res['default_code'] = self.default_code
        res['weight'] = self.weight
        res['volume'] = self.volume
        # Duplicating a cancelled record will detach the revision information
        if self.state == 'cancel':
            res['current_revision_id'] = False
        # TODO: duplicate BOM
        return res
    
    
    @api.returns("self", lambda value: value.id)
    def copy(self, default=None):
        default = default or self.default_get([])
        rec = super(ProductTemplate, self).copy(default)
        return rec

    def action_view_revisions(self):
        self.ensure_one()
        action = self.env.ref("sale.product_template_action")
        result = action.read()[0]
        result["domain"] = [("current_revision_id", "=", self.id)]
        result["context"] = {
            "active_test": 0
        }
        return result

    def action_view_active_revision(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_type': 'form',
            'view_mode': 'form',
            'res_id': self.current_revision_id.id,
            'target': 'current',
            'context': self.env.context
        }