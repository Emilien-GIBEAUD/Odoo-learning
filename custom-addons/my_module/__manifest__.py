# -*- coding: utf-8 -*-
{
    'name': "my_module",

    'summary': """
        Module de test pour apprendre Odoo""",

    'description': """
        Module de test pour apprendre Odoo
    """,

    'author': "Mea",
    'website': "https://emilien-gibeaud.tech/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Learning',
    'version': '0.1',
    'license': 'LGPL-3',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}