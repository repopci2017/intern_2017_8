from odoo import api, fields, models, _

class MenuBranch(models.Model):
    _inherit= 'res.partner'
    
    branch = fields.Boolean(string='Branch')
    
class SO(models.Model):
    _inherit= 'sale.order'
    
    branch_id = fields.Many2one(string='Branch', comodel_name='res.partner')
    