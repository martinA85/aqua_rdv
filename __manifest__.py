# -*- coding: utf-8 -*-
{
    'name': "aqua_rdv",

    'summary': """
        Module de prise de rendez-vous pour l'institut Aqua Attitude""",

    'description': """
        Module pour la gestion de la prise de rendez vous pour l'institut de beauté Aqua Attitude
        V1 : prise de rendez vous depuis l'interface Back
    """,

    'author': "Noosys",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','calendar'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/calendar_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}