from odoo import models, fields


class ClassifiersMain(models.Model):
    _name = 'classifiers.main'
    _description = 'Classification of products'

    head_category = fields.Char(string='head Category')
