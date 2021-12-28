from odoo import models, fields


class ResCompanyInheritShopifyOdooInventorySalesSynchronisation(models.Model):
    _inherit = 'res.company'

    shopify_post_url = fields.Char(string="Shopify Stock Change URL")

class ResCompany(models.Model):
    _inherit = 'res.company'

    shopify_product_upload_url = fields.Char(string="Shopify Product Upload URL")