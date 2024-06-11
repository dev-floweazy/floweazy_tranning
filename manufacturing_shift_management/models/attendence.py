from odoo import fields, models, api


class ManufacturingAttendance(models.Model):
    _name = 'manufacturing.attendance'
    _description = 'Attendance'

    #employee_id = fields.Many2one('hr.employee', string="Employee")
    #shift_id = fields.Many2one('employee.shift', string="Shift")
    date = fields.Date(string="Date", default=fields.Date.today())
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string="Status", default='present')
