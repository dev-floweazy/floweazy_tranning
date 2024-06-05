from odoo import models,fields,api

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string="name",required=True)
    date_of_birth = fields.Date(string="DOB")
    standard = fields.Char(string="Standard")
    guardian_name = fields.Char(string="Guardian_Name")