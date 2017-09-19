# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Product Category Custom',
    'version' : '1.0',
    'summary': 'Sales order',
    'sequence': 1,
    'description': """

v1.0    
====================

    """,
    'category': 'sale custom',
    'Author': 'Hilmy',
    'depends' : ['base','sale','purchase'],
    'data': ['views/product_category_view.xml',
             'security/magang_product_security.xml',
             'security/ir.model.access.csv'

    ],
    'demo': [
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}