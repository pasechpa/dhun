# -*- coding: utf-8 -*-
{
    'name': 'Dhun: Payment Receipt Report',
    'description': """Modifies the payment receipt report.""",
    'summary': """Displays relevant information based on payment policy on related invoice.""",
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'version': '1.0',
    'category': 'Custom',
    'license': 'OPL-1',
    'depends': ['account', 'l10n_mx_edi'],
    'data': [
        'report/report_payment.xml'
    ],
    'demo': [
    ]
}
