
from odoo import api, fields, models


class HotelFloor(models.Model):
    _name = "hotel.floor"
    _description = "Hotel Floors"

    name = fields.Char(string='Name', required=True)
