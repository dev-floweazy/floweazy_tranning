from odoo import fields, models, api


class ManufacturingEmployee(models.Model):
    _inherit = 'hr.employee'


    shift_ids = fields.Many2many('employee.shift', string="Shifts")
    wage = fields.Float(string="Wage")

    
    



