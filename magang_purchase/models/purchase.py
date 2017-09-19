from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order']

    total_payment = fields.Float(string='Total', compute='amount_fix')
    down_payment = fields.Float('Down Payment')

    def amount_fix(self):
        total = self.amount_total - self.down_payment
        self.total_payment = total
        
        
