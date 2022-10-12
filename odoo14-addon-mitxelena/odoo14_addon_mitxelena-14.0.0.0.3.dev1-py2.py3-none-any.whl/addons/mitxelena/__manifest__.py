# -*- coding: utf-8 -*-
{
  'name': "mitxelena",

  'summary': """
    Manufacturing customisation for Talleres mitxelena""",

  'author': "Coopdevs Treball SCCL",
  'website': "https://gitlab.com/coopdevs",

  # Categories can be used to filter modules in modules listing
  # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
  # for the full list
  'category': 'manufacturing',
  'version': '14.0.0.0.2',

  # any module necessary for this one to work correctly
  'depends': [
    'base',
    'sale',
    'product_supplierinfo_for_customer',
    'base_revision',
    'mrp_parallel',
    
  ],

  # always loaded
  'data': [
    'views/res_partner.xml',
    'views/product_template.xml',
    'views/sale_order_line.xml',
    'views/engspecsheet.xml'
  ]
}
