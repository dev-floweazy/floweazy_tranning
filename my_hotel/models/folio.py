# models/hotel_folio.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class HotelFolio(models.Model):
    _name = 'hotel.folio'
    _description = 'Hotel Folio'
    _order = 'order_date desc'

    name = fields.Char(string='Folio Name', readonly=True, copy=False, default='New')
    order_date = fields.Date(string='Order Date', default=fields.Date.today(), readonly=True)
    guest_name = fields.Many2one('res.partner', string='Guest Name', required=True)
    invoice_address = fields.Many2one('res.partner', string='Invoice Address')
    room_lines = fields.One2many('hotel.folio.room.line', 'folio_id', string='Room Lines')
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('hotel.folio') or 'New'
        return super(HotelFolio, self).create(vals)

    @api.onchange('guest_name')
    def _onchange_guest_name(self):
        if self.guest_name:
            self.invoice_address = self.guest_name.address_get(['invoice'])['invoice']

    @api.depends('room_lines.subtotal')
    def _compute_total(self):
        for folio in self:
            folio.total = sum(line.subtotal for line in folio.room_lines)

class HotelFolioRoomLine(models.Model):
    _name = 'hotel.folio.room.line'
    _description = 'Folio Room Line'

    folio_id = fields.Many2one('hotel.folio', string='Folio')
    check_in_date = fields.Date(string='Check In Date', required=True)
    check_out_date = fields.Date(string='Check Out Date', required=True)
    duration = fields.Float(string='Duration', compute='_compute_duration', store=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    room_price = fields.Float(string='Room Price', readonly=True)
    discount = fields.Float(string='Discount', default=0.0)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('check_in_date', 'check_out_date')
    def _compute_duration(self):
        for line in self:
            if line.check_in_date and line.check_out_date:
                delta = line.check_out_date - line.check_in_date
                line.duration = delta.days

    @api.depends('duration', 'room_price', 'discount')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = (line.duration * line.room_price) * (1 - (line.discount / 100))

    # @api.onchange('room_id')
    # def _onchange_room_id(self):
    #     self.room_price = self.room_id.charge if self.room_id else 0.0
