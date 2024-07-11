# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PackDivide(models.Model):
    _name = 'pack.divide'
    _description = 'pack divide'

    batch_id = fields.Many2one('mrp.production', string="Batch")

    components = fields.Selection([('available','Available'),('Unavailable','Unavailable')])
    packaging_size = fields.Selection([
        ('2', '2kg'),
        ('5', '5kg'),
        ('10', '10kg')
    ], string="Packaging Size", required=True)
    package_id = fields.Many2one('main.package',string="Package")
    pack_count = fields.Integer(string="Pack Count", compute='_compute_packs', store=True)
    product_batch = fields.Integer(string = "Product Batch")
    product_batch_tracking = fields.Integer(String = "Unique Id")
    product_id = fields.Many2one('product.template',string="Product")
    packaging_quantity = fields.Float(string="product Quantity")
    no_of_packs = fields.Integer(string="No of packs")
    pack_unique_id = fields.Integer(string="Unique Id")
    package_lines = fields.One2many('pack.divide.line', 'pack_divide_id', string="Package Lines")

@api.depends('qty_available', 'packaging_size')
def _compute_packs(self):
    for record in self:
        if record.packaging_size:
            packaging_size = int(record.packaging_size)
            record.pack_count = int(record.qty_available / packaging_size)


class PackDivideLine(models.Model):
    _name = 'pack.divide.line'
    _description = 'Pack Divide Line'

    pack_divide_id = fields.Many2one('pack.divide', string="Pack Divide")
    product_id = fields.Many2one('product.template', string="Product")
    packaging_quantity = fields.Float(string="Packaging Quantity")
    pack_count = fields.Integer(string="Pack Count")
    pack_unique_id = fields.Integer(string="Unique Id")
