from odoo import models, fields


class Classifiers(models.Model):
    _name = 'classifiers'
    _description = 'Classification of products'

    sub_category = fields.Char(string='sub Category')
