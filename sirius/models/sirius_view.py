# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SiriusView(models.Model):
    _name = "sirius.view"
    _description = "Sirius view"

    name = fields.Char('View name', required=True)
    model_id = fields.Many2one('ir.model', string='Model', ondelete='cascade', required=True)
    type = fields.Selection(selection=[('form', 'Form'),
                                       ('tree', 'Tree')], string='Type', required=True)
    can_read = fields.Boolean('Can read', default=True)
    can_write = fields.Boolean('Can edit', default=True)
    can_create = fields.Boolean('Can create', default=True)
    can_unlink = fields.Boolean('Can delete', default=False)
    group_id = fields.Many2one('res.groups', string='User group allow', required=True)
    sequence_ids = fields.One2many('sirius.view.sequence', 'view_id', string='Fields sequence')
    char_fields_ids = fields.One2many('sirius.view.field.char', 'view_id', string='Char Fields')
    int_fields_ids = fields.One2many('sirius.view.field.int', 'view_id', string='Int Fields')
    block_fields_ids = fields.One2many('sirius.view.block', 'view_id', string='Block')

    def unlink(self):
        self.sequence_ids.unlink()
        return super().unlink()

    def open_wizard(self):
        return {
            'name': 'Add Field',
            'type': 'ir.actions.act_window',
            'res_model': 'sirius.field.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_sirius_view_id': self.id},
        }