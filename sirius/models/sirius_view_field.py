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
    field_id = fields.Many2one('ir.model.fields', string='Field',
                              domain="[('model_id', '=', model_id)]")
    view_id = fields.Many2one('sirius.view', string='View')
    required = fields.Boolean('Required', default=False)
    readonly = fields.Boolean('Readonly', default=True)
    sequence = fields.Integer('Sequence')
