from odoo import fields, models, api


class LaborType(models.Model):
    _name = 'labor.type'
    _description = 'Labor Type'

    name = fields.Selection([('skilled','Skilled'),('unskilled','Unskilled')])
    hourly_rate = fields.Float(string="Hourly Rate")
    description = fields.Text()

