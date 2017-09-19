from odoo import api, fields, models, _

class ResUsers(models.Model):
    _inherit= 'res.users'
    
    branch_id = fields.Many2one(string='Branchs', comodel_name='res.partner')



        