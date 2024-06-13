# -*- coding: utf-8 -*-
{
    'name': 'Hotel',
    'version': '1.0',
    'summary': 'FlowEazy Software Management',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/floor.xml',
        'views/folio.xml',
        'data/folio_sequence.xml',
        'views/rooms.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
