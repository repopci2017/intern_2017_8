from odoo import api, fields, models, _

class Discount(models.Model):
    _name = "discount.discount"
    _description = "Discount"
    
    name = fields.Char(string='Discount')
    percentage = fields.Float(string='Percentage')
    status = fields.Boolean(string='Status')
    
