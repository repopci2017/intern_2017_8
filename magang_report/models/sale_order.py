from odoo import api, fields, models, _
 
class ProductTemplate(models.Model):
    _inherit= 'product.product'
     
    tin_dus=fields.Float(related='product_tmpl_id.tin_dus')
    
class ProductTemplates(models.Model):
    _inherit= 'product.template'
    
    tin_dus = fields.Float('Tin/Dus')
    
