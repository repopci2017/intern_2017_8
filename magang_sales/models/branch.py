from odoo import api, fields, models, _

class Branch(models.Model):
    _inherit= 'res.partner'
    
    branch_id = fields.Many2one(string='Branch', comodel_name='res.partner')
    
class SaleOrder(models.Model):
    _inherit= 'sale.order'
    
    is_available = fields.Boolean(string='Is Available')
