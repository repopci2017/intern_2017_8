# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Magang_wizard',
    'version' : '1.0',
    'summary': 'Sale report Custom',
    'sequence': 1,
    'description': """

v1.0    
====================
"create a New report."

    """,
    'category': 'sales',
    'Author': 'Hilmy',
    'depends' : ['base','sale'],
    'data': ['wizard/laporan_penjualan_harian_view.xml'
     ],
    'demo': [
    ],
    'qweb': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}