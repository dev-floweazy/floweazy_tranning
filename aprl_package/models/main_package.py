from odoo import models, fields, api


class MainPackage(models.Model):
    _name = 'main.package'
    _description = 'package creation'

    #size, weight, max_weight, barcode, company, carrier, carrier code

    name = fields.Char(string="Name")
    size = fields.Float(string="Size")
    weight = fields.Float(string="Weight")
    max_weight = fields.Float(string="Max Weight")
    barcode = fields.Char(string="Barcode")
    company = fields.Char(string="Company")
    carrier = fields.Char(string="Carrier")
    carrier_code = fields.Char(string="carrier Code")
