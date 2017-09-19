from odoo import api, fields, models, _

class Discount(models.Model):
    _inherit= 'discount.discount'
    date = fields.Date(string='date')