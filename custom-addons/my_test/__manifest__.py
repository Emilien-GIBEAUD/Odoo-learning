{
    'name': "my_test",

    'summary': "Module de test Odoo",

    'description': """Création de tables et de CRUD pour apprendre l'utilisation de l'ORM Odoo.""",

    'author': "Mea",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Learning',
    'version': '0.1',
    'license': 'LGPL-3',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

