# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SiriusViewField(models.AbstractModel):
    _name = "sirius.view.field"
    _description = "Sirius view field"
    _rec_name = "label"

    label = fields.Char('Field name')
    model_id = fields.Many2one(related='view_id.model_id', string='Model')
    field_id = fields.Many2one('ir.model.fields', string='Field', required=True,  ondelete='set null')
    ttype = fields.Selection(related='field_id.ttype', string='Type')
    view_id = fields.Many2one('sirius.view', string='View', required=True)
    required = fields.Boolean('Required', default=False)
    readonly = fields.Boolean('Readonly', default=True)
    sequence = fields.Integer('Sequence')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            self.env['sirius.view.sequence'].create({
                'sirius_field_id': vals['id'],
            })
        return super(SiriusViewField, self).create(vals_list)

    def unlink(self):
        self.env['sirius.view.sequence'].search([('sirius_field_id', 'in', self.ids)]).unlink()
        return super().unlink()