from odoo import api, fields, models, _
from datetime import date


class HotelFolio(models.Model):
    _name = "hotel.folio"
    _description = "Hotel Folio"

    name = fields.Char(index=True, readonly=True, default=lambda self: _('New'))
    order_date = fields.Date(string='Order Date', default=fields.Date.context_today, readonly=True)
    guest_name_id = fields.Many2one('res.partner', string='Guest Name')
    invoice_address_id = fields.Many2one('res.partner', string="Invoice Address")
    room_lines_ids = fields.One2many('hotel.folio.line', 'folio_id', string="Room line ids")
    total = fields.Float()

    @api.onchange('guest_name_id')
    def _onchange_guest_name_id(self):
        if self.guest_name_id:
            self.invoice_address_id = self.guest_name_id

    @api.depends('room_lines_ids.subtotal')
    def _compute_total(self):
        for folio in self:
            folio.total = sum(line.subtotal for line in folio.roomlines_ids)

    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('my_sequence_code')
        return super(HotelFolio, self).create(vals)


'''class HotelFolioLine(models.Model):
    _name = 'hotel.folio.line'
    _description = 'Hotel Folio Line'

    check_in_date = fields.Date(string="Check In")
    check_out_date = fields.Date(string="Check Out")
    duration = fields.Float()
    room_id = fields.Many2one('hotel.room', 'Room')
    room_price = fields.Float()
    discount = fields.Float()
    subtotal = fields.Float()
    folio_id = fields.Many2one('hotel.folio', string='Folio')

    @api.depends('check_in_date', 'check_out_date')
    def _compute_duration(self):
        for line in self:
            if line.check_in_date and line.check_out_date:
                delta = fields.Date.from_string(line.check_out_date) - fields.Date.from_string(line.check_in_date)
                line.duration = delta.days + 1
            else:
                line.duration = 0

    @api.depends('duration', 'room_price', 'discount')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = (line.duration * line.room_price) - line.discount '''
            
            
            
            
class HotelFolioLine(models.Model):
    _name = 'hotel.folio.line'
    _description = 'Hotel Folio Line'

    folio_id = fields.Many2one('hotel.folio', string='Folio', required=True, ondelete='cascade')
    check_in_date = fields.Date(string='Check In Date')
    check_out_date = fields.Date(string='Check Out Date')
    duration = fields.Float(string='Duration', compute='_compute_duration')
    room_id = fields.Many2one('hotel.room', string='Room')
    room_price = fields.Float(string='Room Price', related='room_id.room_charge')
    discount = fields.Float(string='Discount')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.depends('check_in_date', 'check_out_date')
    def _compute_duration(self):
        for line in self:
            if line.check_in_date and line.check_out_date:
                delta = fields.Date.from_string(line.check_out_date) - fields.Date.from_string(line.check_in_date)
                line.duration = delta.days

    @api.depends('duration', 'room_price', 'discount')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = (line.duration * line.room_price) - line.discount
