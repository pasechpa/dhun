from odoo import models, fields, api, _
import requests
import json
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    shopify_product_id = fields.Char()
    shopify_handle = fields.Char()
    
    def get_alternatives_products(self):
        alt_products = []
        for alt_product in self.alternative_product_ids:
            alt_products.append({
                "sku": alt_product.default_code,
                "shopify_id": alt_product.shopify_product_id,
                "shopify_handle":alt_product.shopify_handle
            })
        return alt_products

    def get_products_accesories(self):
        acc_products = []
        for acc_product in self.accessory_product_ids:
            acc_products.append({
                "sku": acc_product.default_code,
                "shopify_id": acc_product.shopify_product_id,
                "shopify_handle":acc_product.shopify_handle
            })
        return acc_products


    def get_product_parent_tags(self):
        res_categ = []
        for categs in self.public_categ_ids:
            current_category = categs;
            while current_category:
                pair_split = {
                    "parent_tag": current_category.parent_id.name,
                    "son_tag": current_category.name
                }
                res_categ.append(pair_split)
                current_category = current_category.parent_id
        return res_categ

    def get_shopify_data_upload(self):
        _logger.info(_("Getting data of the product %s") % self.name)
        variants = self.product_variant_ids
        product_image = ''
        if self.image_1024:
            product_image = self.image_1024.decode('utf-8')
        shopify_data_post = {
            "id":self.id,
            "title": self.name,
            "shopify_product_id": self.shopify_product_id,
            "tags": self.get_product_parent_tags(),
            "category":self.categ_id.display_name,
            "images": "",
            "multiple_sell": self.x_studio_mltiplo_de_10,
            "quotation_only": self.x_studio_solo_cotizar_1,
            "outlet": self.x_studio_outlet,
            "marca": self.x_studio_marca,
            "product_accesories": self.get_products_accesories(),
            "product_alternatives": self.get_alternatives_products(),
            "variants": [
                {
                    "id":variant.id,
                    "sku": variant.default_code,
                    "variant_data": [{variant_attribute.attribute_id.display_name: variant_attribute.name} for
                                     variant_attribute in
                                     variant.product_template_attribute_value_ids],
                    "stock": variant.qty_available - variant.outgoing_qty,
                    "sales_price": variant.list_price,
                    "barcode": variant.barcode,
                    "shopify_variant_id": variant.shopify_variant_id
                } for variant in variants
            ]
        }
        return shopify_data_post

    def upload_product_to_shopify(self):
        for line in self:
            upload_data = line.get_shopify_data_upload()
            if upload_data:
                headers = {'Content-Type': 'application/json'}
                data_json = json.dumps({'params': upload_data})
                try:
                    shopify_product_upload_url = self.env.user.company_id.shopify_product_upload_url
                    requests.post(url=shopify_product_upload_url, data=data_json, headers=headers)
                except Exception as e:
                    _logger.error(
                        "Failed to send post request to shopify for upload the product %s, reason : %s" % (
                            self.name, e))
            else:
                _logger.error(_("The upload data is empty for the product %s") % (self.name))


class ProductProduct(models.Model):
    _inherit = 'product.product'

    shopify_variant_id = fields.Char(string="Shopify variant_id")
