# -*- coding: utf-8 -*-
{
    'name': "Sirius",

    'summary': """Sirius Odoo setting tools""",

    'description': """Sirius Odoo setting tools""",

    'author': "Grupo Faster",
    'website': "https://faster.es/",

    'version': '0.1',

    'depends': [

    ],
    'data': [
        'security/sirius_security.xml',
        'security/ir.model.access.csv',
        'views/sirius_view_views.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}
