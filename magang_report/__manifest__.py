# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Magang Report',
    'version' : '1.0',
    'summary': 'Sales order report',
    'sequence': 1,
    'description': """

v1.0    
====================

    """,
    'category': 'sale custom',
    'Author': 'Hilmy',
    'depends' : ['base','sale'],
    'data': ['report/sale_order_report.xml',
       'views/sale_order_src.xml' 
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
