# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hotel.floor"
    _description = "Hotel Floors"

    name = fields.Char(string='Name', required=True)
    rooms = fields.Integer(string='Rooms')
