# models/hotel_room.py
from odoo import models, fields

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Name', required=True)
    floor_id = fields.Many2one('hotel.floor', string='Floor')
    room_manager_id = fields.Many2one('res.users', string='Room Manager')
    room_capacity = fields.Integer(string='Room Capacity')
    room_charge = fields.Float(string='Room Charge')
