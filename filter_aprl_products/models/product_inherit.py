
from odoo import models, fields


class ProductInherit(models.Model):
    _inherit = 'product.product'

    material_type = fields.Selection([
        ("finished material", "Finished material"),
        ("raw material", "Raw material"),
        ("packaged material", "Packaged material")
    ], string='Material Type')

    packaging_type = fields.Selection([
        ('bulk', 'Bulk'),
        ('consumer packaged', 'Consumer packaged'),
        ('packaged', 'Packaged')
    ], string='Packaging Type')

    head_category_id = fields.Many2one('head_categories',stirng='Head Categories')
    sub_category_id = fields.Many2one('sub_categories',string='Sub Categories')