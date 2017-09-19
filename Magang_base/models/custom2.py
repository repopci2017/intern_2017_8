from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit= 'sale.order'
    
    branch_id = fields.Many2one(string='Branchs', comodel_name='res.partner')
    
class PurchaseOrder(models.Model):
    _inherit= 'purchase.order'
     
    branch_id = fields.Many2one(string='Branchs', comodel_name='res.partner')
    
class AccountInvoice(models.Model):
    _inherit= 'account.invoice'
    
    branch_id = fields.Many2one(string='Branchs', comodel_name='res.partner')