# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SiriusViewFieldSequence(models.Model):
    _name = "sirius.view.sequence"
    _description = "Sirius view sequence"

    view_id = fields.Many2one('sirius.view', compute='_compute_view_id', string='View')
    sirius_block_id = fields.Many2one('sirius.view.block', string='Block')
    sirius_field_char_id = fields.Many2one('sirius.view.field.char', string='Field')
    sirius_field_int_id = fields.Many2one('sirius.view.field.int', string='Field')
    sirius_field_name = fields.Char('Field name', compute='_compute_field_name')
    sequence = fields.Integer('Sequence')
    field_type = fields.Selection([
        ('char', 'Char'),
        ('integer', 'Integer'),
        ('block', 'Block')
    ], string="Field Type", required=True)

    @api.model_create_multi
    def create(self, vals_list):
        fields_sequence = super(SiriusViewFieldSequence, self).create(vals_list)

        for seq in fields_sequence:
            seq.sequence = self.env['sirius.view.sequence'].search(
                [('view_id', '=', seq.view_id.id)],
                order='sequence desc', limit=1).sequence + 1
            if seq.sirius_field_char_id:
                seq.field_type = 'char'
            if seq.sirius_field_int_id:
                seq.field_type = 'integer'
            if seq.sirius_block_id:
                seq.field_type = 'block'

        return

    def write(self, values):
        _logger.info(values)
        if 'sequence' in values:
            if self.sirius_field_char_id:
                self.sirius_field_char_id.sequence = values.get('sequence')
            if self.sirius_field_int_id:
                self.sirius_field_int_id.sequence = values.get('sequence')
            if self.sirius_block_id:
                self.sirius_block_id.sequence = values.get('sequence')
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
            elif record.sirius_block_id:
                record.view_id = record.sirius_block_id.view_id
            else:
                record.view_id = False

    def _compute_field_name(self):
        for record in self:
            if record.sirius_field_char_id:
                record.sirius_field_name = record.sirius_field_char_id.label
            elif record.sirius_field_int_id:
                record.sirius_field_name = record.sirius_field_int_id.label
            elif record.sirius_block_id:
                record.sirius_field_name = record.sirius_block_id.label
            else:
                record.sirius_field_name = False

    
    def action_open_wizard(self):
        if self.sirius_block_id:
            return {
                'name': 'Edit',
                'type': 'ir.actions.act_window',
                'res_model': 'sirius.field.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_sirius_block_id': self.sirius_block_id.id,
                    'default_sirius_view_id': self.view_id.id,
                    'default_field_type': self.field_type,
                    'default_label': self.sirius_block_id.label,
                    'default_image': self.sirius_block_id.image,
                    'default_type': self.sirius_block_id.type,
                }
            }
        elif self.sirius_field_char_id:
            return {
                'name': 'Edit',
                'type': 'ir.actions.act_window',
                'res_model': 'sirius.field.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_sirius_field_char_id': self.sirius_field_char_id.id,
                    'default_sirius_view_id': self.view_id.id,
                    'default_field_type': self.field_type,
                    'default_label': self.sirius_field_char_id.label,
                    'default_required': self.sirius_field_char_id.required,
                    'default_readonly': self.sirius_field_char_id.readonly,
                    'default_ttype': self.sirius_field_char_id.ttype,
                    'default_default_value': self.sirius_field_char_id.default_value,
                    'default_hint_value': self.sirius_field_char_id.hint_value,
                    'default_min_length': self.sirius_field_char_id.min_length,
                    'default_max_length': self.sirius_field_char_id.max_length,
                }
            }
        elif self.sirius_field_int_id:
            return {
                'name': 'Edit',
                'type': 'ir.actions.act_window',
                'res_model': 'sirius.field.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_sirius_field_int_id': self.sirius_field_int_id.id,
                    'default_sirius_view_id': self.view_id.id,
                    'default_field_type': self.field_type,
                    'default_label': self.sirius_field_int_id.label,
                    'default_required': self.sirius_field_int_id.required,
                    'default_readonly': self.sirius_field_int_id.readonly,
                    'default_ttype': self.sirius_field_int_id.ttype,
                    'default_default_value': self.sirius_field_int_id.default_value,
                    'default_hint_value': self.sirius_field_int_id.hint_value,
                    'default_minimum': self.sirius_field_int_id.minimum,
                    'default_maximum': self.sirius_field_int_id.maximum,
                }
            }


