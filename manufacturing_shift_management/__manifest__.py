# -*- coding: utf-8 -*-
{
    'name': 'Manufacturing',
    'version': '1.0',
    'summary': 'FlowEazy Software Management',
    'sequence': -100,
    'description': """Manufacturing Software""",
    'category': 'Manufacturing',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': ['hr'],
    'data': [
        'views/attendence.xml',
        'views/employee.xml',
        'views/labor_type.xml', 
        'views/manufacturing_operation.xml',
        'views/manufacturing_workcenter.xml',

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
