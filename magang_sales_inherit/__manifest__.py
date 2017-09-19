# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Discount inherit',
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
    'depends' : ['base','magang_sales'],
    'data': ['views/sale_order_view.xml'
    ],
    'demo': [
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
