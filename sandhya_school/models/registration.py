from odoo import models,fields,api

class SchoolRegistration(models.Model):
    _name = "school.registration"
    _description = "School Registration"

    name = fields.Char(string="name",required=True)
    date_of_birth = fields.Date(string="DOB")
    standard = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('prefer not to say','Prefer not to say')])
    guardian = fields.Char(string="Guardian")
    old_school = fields.Char()
