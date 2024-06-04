from odoo import models,fields,api

class Schoolprofessor(models.Model):
    _name = "school.professor"
    _description = "School Professor"

    name = fields.Char(string="name" ,required=True)
    date_of_birth = fields.Date(string = "DOB")
    qualification = fields.Char(string="Qualification")
    salary = fields.Integer(string = "salary")