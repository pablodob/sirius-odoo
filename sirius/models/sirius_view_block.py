# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SiriusViewField(models.AbstractModel):
    _name = "sirius.view.block"
    _description = "Sirius view block"
    _rec_name = "label"

    type = fields.Selection([('text','Text'),('h1','H1'),('h2','H2'),('h3','H3'),('image','Image')], string='Type')
    label = fields.Char('Field name')
    image = fields.Binary('Image')
    view_id = fields.Many2one('sirius.view', string='View')
    required = fields.Boolean('Required', default=False)
    readonly = fields.Boolean('Readonly', default=True)
    sequence = fields.Integer('Sequence')

    def unlink(self):
        self.env['sirius.view.sequence'].search([('sirius_field_id', 'in', self.ids)]).unlink()
        return super().unlink()