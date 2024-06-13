from odoo import models,fields,api
from datetime import date,datetime

class SchoolRegistration(models.Model):
    _name = "school.registration"
    _description = "School Registration"

    name = fields.Char(string="name",required=True)
    date_of_birth = fields.Date(string="DOB")
    standard = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('prefer not to say','Prefer not to say')])
    guardian = fields.Char(string="Guardian")
    old_school = fields.Char()


    #my code starts here
    first_name = fields.Char(string="First Name")
    disability = fields.Boolean()
    address = fields.Text()
    registration_fee = fields.Float(digits=(6,2))
    registration_date = fields.Date(default=lambda self: fields.Date.context_today(self))
    #bonafide = fields.Binary() --> not working
    guardian_type = fields.Selection([('mother','Mother'),('father','Father'),('other','Other')])




    
    
    

class SelectionInheritance(models.Model):
    _inherit = "school.registration"

    guardian_type = fields.Selection(selection_add = [('aunt','Aunt'),('uncle','Uncle')])



''' class viewInheritance(model.Model):
    _inherit = "school.registration"

    academic_year = fields.Date(string="Academic Year") '''

