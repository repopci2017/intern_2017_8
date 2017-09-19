from odoo import api, fields, models, _

class SaleOrderLine(models.Model):
    _inherit= 'sale.order.line'
    
    discount_m2o = fields.Many2one('discount.discount', string='Discount')
    discount1 = fields.Many2one('discount.discount', string='Discount')            
   
class SaleOrder(models.Model):
    _inherit= 'sale.order'
    
    price_discount = fields.Float(string='Price Discount', compute='amount_discount')
    total_discount = fields.Float(string='Total', compute='amount_fix')

    def amount_discount(self):
        order =  self.order_line
        total_discount = 0
        print order
        for line in order :
            print total_discount 
            discount = ((line.price_subtotal * line.discount_m2o.percentage)/100.0)
            print discount
            total_discount = total_discount + discount
            print total_discount
        self.price_discount = total_discount
        
    def amount_fix(self):
        total = self.amount_total - self.price_discount
        self.total_discount = total 
            


        
        

    
