# -*- coding: utf-8 -*-
{
    'name': "InterMan",

    'summary': """
    Management of Technical Department Interventions at NAFTAL Stations Service  in order to rationalize
     the Consumption of Spare Parts and the Efforts of technicians """,

    'description': """
       InterMan aims to improve online intervention management and statistic of naftal company and minimize the effort  
       technicians. """,

    'author': "Hachemi Mohamed Ramzi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/panne.xml',
        'views/station.xml',
        'views/piece.xml',
        'views/equipment.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
