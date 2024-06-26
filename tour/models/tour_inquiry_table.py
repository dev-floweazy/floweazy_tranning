from odoo import api,models, fields, _


class TourInquiryTable(models.Model):
    _name = 'tour.inquiry.table'
    _description = 'tour inquiry table'

    customer_inquiry = fields.Char(default=lambda self:_('New'), readLine='True')
    customer_email = fields.Char()
    customer_phone = fields.Char()


    @api.model
    def create(self, vals):
        vals['customer_inquiry'] = self.env['ir.sequence'].next_by_code('customer.inquiry.sequence')
        return super(TourInquiryTable, self).create(vals)

