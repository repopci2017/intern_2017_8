# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Purchase Custom',
    'version' : '1.0',
    'summary': 'Purchase Order',
    'sequence': 1,
    'description': """

v1.0    
====================
"create a new field Down Payment."

    """,
    'category': 'purchase custom',
    'Author': 'Hilmy',
    'depends' : ['base','purchase'],
    'data': ['views/purchase_view.xml',
             'report/report_custom_view.xml'
     ],
    'demo': [
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
