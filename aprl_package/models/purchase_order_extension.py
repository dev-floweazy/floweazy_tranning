# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_line_batch_ids = fields.One2many('purchase.order.line.batch', 'order_id', string='Batch List')


class PurchaseOrderLineBatch(models.Model):
    _name = 'purchase.order.line.batch'

    order_id = fields.Many2one('purchase.order', string='Order')
    product_id = fields.Many2one('product.product', string='Product')
    batch_id = fields.Many2one('product.batch', string='Batch')
    quantity = fields.Float(string='Quantity')
