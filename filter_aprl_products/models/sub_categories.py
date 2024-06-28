from odoo import models,fields


class SubCategories(models.Model):
    name = 'sub.categories'
    _description = 'Shows sub categories'

    sub_category = fields.Char(string="Sub head Category")
