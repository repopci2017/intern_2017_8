# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Discount',
    'version' : '1.0',
    'summary': 'Sales discount',
    'sequence': 1,
    'description': """

v1.0    
====================
"create menu discount."

    """,
    'category': 'discount custom',
    'Author': 'Hilmy',
    'depends' : ['base','product','sale','stock'],
    'data': ['views/sales_order_view.xml',
             'views/product_template_view.xml',
             'views/discount_view.xml',
             'views/branch_view.xml',
             'views/menu_branch_view.xml',
             'report/report_discount_custom.xml'
    ],
    'demo': [
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
