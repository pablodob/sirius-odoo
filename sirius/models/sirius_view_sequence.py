# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SiriusViewField(models.Model):
    _name = "sirius.view.sequence"
    _description = "Sirius view sequence"

    view_id = fields.Many2one('sirius.view', compute='_compute_view_id', string='View')
    sirius_block_id = fields.Many2one('sirius.view.block', string='Block')
    sirius_field_char_id = fields.Many2one('sirius.view.field.char', string='Field')
    sirius_field_int_id = fields.Many2one('sirius.view.field.int', string='Field')
    sirius_field_name = fields.Char('Field name', compute='_compute_field_name')
    sequence = fields.Integer('Sequence')

    @api.model_create_multi
    def create(self, vals_list):
        fields_sequence = super(SiriusViewField, self).create(vals_list)

        for seq in fields_sequence:
            seq.sequence = self.env['sirius.view.sequence'].search(
                [('view_id', '=', seq.view_id.id)],
                order='sequence desc', limit=1).sequence + 1
        return

    def write(self, values):
        if 'sequence' in values:
            if self.sirius_field_char_id:
                self.sirius_field_char_id.sequence = values.get('sequence')
            if self.sirius_field_int_id:
                self.sirius_field_int_id.sequence = values.get('sequence')
        return super().write(values)

    def unlink(self):
        if self.sirius_field_char_id:
            self.sirius_field_char_id.unlink()
        if self.sirius_field_int_id:
            self.sirius_field_int_id.unlink()
        if self.sirius_block_id:
            self.sirius_block_id.unlink()
        return super().unlink

    def _compute_view_id(self):
        for record in self:
            if record.sirius_field_char_id:
                record.view_id = record.sirius_field_char_id.view_id
            elif record.sirius_field_int_id:
                record.view_id = record.sirius_field_int_id.view_id
            else:
                record.view_id = False

    def _compute_field_name(self):
        for record in self:
            if record.sirius_field_char_id:
                record.sirius_field_name = record.sirius_field_char_id.label
            elif record.sirius_field_int_id:
                record.sirius_field_name = record.sirius_field_int_id.label
            else:
                record.sirius_field_name = False


