# -*- coding: utf-8 -*-
{
    'name': "dc_report",

    'summary': """
        G.G.Tronics reports""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'web','account','contacts','stock_indent'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/e_way_bill.xml',
        'report/menu.xml',
        'report/header_footer.xml',
        'report/dc_challana.xml',
        'report/tax_invoice.xml',
        # 'report/sale_invoice.xml',
        'report/sale_template.xml'

    ],
}
