from odoo import models,fields


class HeadCategories(models.Model):
    name = 'head.categories'
    _description = 'Shows head categories'

    head_category = fields.Char(string="Head Category")

