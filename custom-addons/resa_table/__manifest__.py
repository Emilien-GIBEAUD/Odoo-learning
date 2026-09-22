{
    'name': "ResaTable",

    'summary': "Application de réservation de tables et/ou pizzas pour restaurant.",

    'description': """Application de réservation de tables et/ou pizzas pour restaurant.""",

    'author': "Mea",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Learning',
    'version': '0.1',
    'license': 'LGPL-3',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Pizza/pizzas.xml',
        'views/base.xml',
        'views/conditions.xml',
        'views/home.xml',
        'views/views.xml',
    ],
    'assets': {
    'resa_table.assets_pizzas': [
        'resa_table/static/src/js/pizza.js',
        'resa_table/static/src/css/pizza.css',
    ],
    'resa_table.base': [
        'resa_table/static/src/js/color-modes.js',
    ],
},
}

