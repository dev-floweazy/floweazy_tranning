# -*- coding: utf-8 -*-
{
    'name': 'Test App',
    'version': '16',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/test_app_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}