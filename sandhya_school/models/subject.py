from odoo import models,fields,api

class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "School Subject"

    name = fields.Char(string="name",required=True)
    code = fields.Integer()
    type = fields.Selection([('theory','Theory'),('practical','Practical'),('both','Both'),('other','Other')])
    subject_type = fields.Selection([('compulsory','Compulsory'),('elective','elective')])
    grade_weightage = fields.Float()

