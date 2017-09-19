from odoo import api, fields, models, _

class ProductCategory(models.Model):
    _inherit= 'product.category'
    
    branch = fields.Many2one(string='Branch', comodel_name='res.partner')


