# -*- coding: utf-8 -*-
##############################################################################
#
#    Digital Ranjan
#    Copyright (C) 2024 (http://www.digitalranjan.in)
#
##############################################################################

{
    'name': 'ARPL Package Management',
    'version': '1.0',
    'summary': 'ARPL Management by Digital Ranjan',
    'sequence': -1000,
    'description': """A arpl management software which helps you to build tour bookings and everything online""",
    'category': 'Productivity',
    'website': 'http://www.digitalranjan.in',
    'Licence': 'LGPL-3',
    'depends': ['mrp', 'product', 'stock', 'purchase', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pack_divide.xml',
        'views/main_package.xml',
        "views/product_batch_management_view.xml",
        "views/product_extension_view.xml",
        "views/sale_order_view.xml",
        "views/menu.xml",
    ],
    'demo': [],
    'qweb': [],
    'installation': True,
    'application': True,
    'auto_install': False,
}
