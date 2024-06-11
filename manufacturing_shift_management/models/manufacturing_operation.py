from odoo import api, fields, models


class ManufacturingOperation(models.Model):
    _name = "manufacturing.operation"
    _description = "Manufacturing Operations"

    name = fields.Char(string='Operation Name', required=True)
    operation_cost = fields.Float()
    estimated_duration = fields.Float(string="Estimated Duration")
    work_center_id = fields.Many2one('manufacturing.workcenter', string="Workcenter")

