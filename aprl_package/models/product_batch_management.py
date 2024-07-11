# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductBatch(models.Model):
    _rec_name = 'pack_batch'
    _name = 'product.batch'
    _description = 'Product Batch'

    pack_batch = fields.Char(string='Batch ID')
    manufacturing_date = fields.Date(string='Manufacturing Date')
    expiry_date = fields.Date(string='Expiry Date')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    last_sequence = fields.Integer(string='Last Sequence', default=1)

    def generate_batch_id(self):
        # Get the current date in the format DDMMMYY (e.g., 13JUN24)
        current_date = fields.Date.today().strftime('%d%b%y').upper()

        # Increment the last sequence number
        next_sequence = self.last_sequence + 1

        # Generate the new batch ID
        batch_id = f'PACK-{current_date}-{next_sequence:02}'

        # Update the last sequence number
        self.write({'pack_batch': batch_id, 'last_sequence': next_sequence})

        return batch_id
