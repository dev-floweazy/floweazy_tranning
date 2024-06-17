
from odoo import models,fields,api

class SchoolStandard(models.Model):
    _name = "school.standard"
    _description = "School Standard"

    #name = fields.Char(string="name",required=True,help="enter your name please")
    name = fields.Integer(string="Standard")
    professor_name_id = fields.Many2one('school.professor',string="Class Professor")
    class_name_id = fields.Many2one('school.classes', string="Standard")
    students_ids = fields.One2many('school.standard.lines','standard_id',string="Students")




class SchoolStandardLines(models.Model):
    _name = "school.standard.lines"
    _description = "school standard lines"

    standard_id = fields.Many2one('school.standard', string="Standard")
    student_id = fields.Many2one('school.registration', string='Student')




