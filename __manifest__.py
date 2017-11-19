# -*- coding: utf-8 -*-

{
    'name': 'Paybill/Till module',
    'category': 'Accounting',
    'summary': 'MPESA Paybill/Till Module for POS',
    'version': '1.0',
    'author': 'Brian Gikonyo',
    'description': """MPESA Paybill/Till Module for POS
	Paybill url:<domain>:8069/web/mpesa/paybill
	Till url:<domain>:8069/web/mpesa/till
	""",
    'depends': ['point_of_sale'],
    'data': [
        'views/mpayment_view.xml',
        'views/point_of_sale_template.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
