
from odoo import models,fields,api

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    #name = fields.Char(string="name",required=True,help="enter your name please")
    name = fields.Many2one('school.registration', string="Student Name")
    date_of_birth = fields.Date(string="DOB")
    standard = fields.Char(string="Standard")
    guardian_name = fields.Char(string="Guardian_Name")
    #subject_ids = fields.One2many('school.student.lines','subject_id',string="Subjects")




'''class SchoolStudentLines(models.Model):
    _name = "school.student.lines"
    _description = "school student lines"

    student_id = fields.Many2one('school.student', string='Student_Name')
    subject_id = fields.Many2one('school.student', string="Subjects")
    name_id = fields.Many2one('school.professor', string="Professor Name") '''



