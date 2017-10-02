# -*- coding: utf-8 -*-

{
    'name': 'MPESA Payment',
    'category': 'Accounting',
    'summary': 'MPESA Payment Module',
    'version': '1.0',
    'author': 'Brian Gikonyo',
    'description': """MPESA Payment Module""",
    'depends': ['point_of_sale'],
    'data': [
        'views/mpayment_view.xml',
        'views/point_of_sale_template.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'auto_install': False,
}