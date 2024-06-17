from odoo import models,fields,api

class SchoolParent(models.Model):
    _name = "school.parent"
    _description = "School Parent"

    name = fields.Char(string="name",required=True)
    age = fields.Integer()
    child_name = fields.Many2one('school.registration', name='Child Name')
    relation_with_child = fields.Selection([('mother','Mother'),('father','Father'),('other','Other')])
    phone_no = fields.Char()
    address = fields.Char()