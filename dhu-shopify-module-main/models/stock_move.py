from odoo import models, fields, api, _
import requests
import json
import logging

_logger = logging.getLogger(__name__)
from odoo.tools.float_utils import float_is_zero

class StockMoveLineInheritShopifyOdooInventorySalesSynchronisation(models.Model):
    _inherit = 'stock.move'

    def send_data_to_webserver(self):
        move_lines = self.move_line_ids
        for line in move_lines:
            product = line.product_id
            qty_custom = 0
            for location in product.stock_quant_ids:
                if("Physical Locations/WH/Stock" in location.location_id.display_name):
                    qty_custom += location.quantity - location.reserved_quantity
                    
            data = {'product_id': product.id,
                    'sku': product.default_code,
                    'stock_qty': qty_custom,
                    'price': product.lst_price}
            _logger.info("Loading data to webservice %s" % data)
            headers = {'Content-Type': 'application/json'}
            data_json = json.dumps({'params': data})
            try:
                requests.post(url=self.env.user.company_id.shopify_post_url, data=data_json, headers=headers)
            except Exception as e:
                _logger.error("Failed to send post request to shopify webservice, reason : %s" % e)
