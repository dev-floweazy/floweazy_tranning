# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    batch_ids = fields.One2many('product.batch', 'product_id', string='Batches')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    batch_ids = fields.One2many('product.batch', 'product_id', string='Batches')