{
    'name': 'shopify-odoo-dhu',
    'version': '2.1',
    'summary': 'Synchronise sales and qty of product on odoo and shopify, also uploaod you producs to shopify',
    'description': 'This module will synchronise the sale order creation of odoo and shopify as well as the qtys ajustments and '
                   'will add the feature of uploading the product and all '
                   'its variants using action server, if the upload is successful, it will'
                   'return the shopify id of the product',
    'category': 'Inventory, Logistic, Storage, sale',
    'author': '',
    'website': '',
    'license': '',
    'depends': ['base', 'sale', 'sale_management', 'stock', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product.xml',
        'views/res_partner.xml',
        'views/res_company.xml',
        'views/sale.xml'],
    'installable': True,
    'auto_install': False
}
