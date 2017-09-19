# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale_Order_Custom',
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
    'data': ['views/custom_view.xml',
            'views/custom_a_view.xml',
            'security/magang_base_security.xml',
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
