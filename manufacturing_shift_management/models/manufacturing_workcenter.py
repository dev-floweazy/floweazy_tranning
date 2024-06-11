from odoo import api, fields, models


class ManufacturingWorkCenter(models.Model):
    _name = "manufacturing.work.center"
    _description = "Manufacturing Work center"

    name = fields.Char(string='work center Name', required=True)
    location = fields.Char()
    capacity_for_machines = fields.Integer(string="Capacity For Machines")
    production_capacity = fields.Integer()
    operation_ids = fields.One2many('manufacturing.operation', 'work_center_id', string="Assigned Operations")
