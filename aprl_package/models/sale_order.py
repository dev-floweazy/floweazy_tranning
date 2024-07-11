# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    product_batch_id = fields.Many2one('product.batch', string='Batch')

    # @api.onchange('product_id')
    # def onchange_product_id(self):
    #     print("\nself::::::",self, self._context)
    #     if self.product_id:
    #         print("\nproduct id", self.product_id.name)
    #         print("\nproduct id", self.product_id.product_batch_id)
    #         return {'domain': {'batch_id': [('product_id', '=', self.product_id.id)]}}
    #     else:
    #         return {'domain': {'batch_id': []}}
