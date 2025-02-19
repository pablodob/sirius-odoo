# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class SiriusViewFieldBlock(models.Model):
    _name = "sirius.view.block"
    _description = "Sirius view block"
    _rec_name = "label"

    type = fields.Selection([('text','Text'),('h1','H1'),('h2','H2'),('h3','H3'),('image','Image')], string='Type')
    label = fields.Char('Field name')
    image = fields.Binary('Image')
    view_id = fields.Many2one('sirius.view', string='View', required=True, ondelete='cascade')
    sequence = fields.Integer('Sequence')

    @api.model_create_multi
    def create(self, vals_list):
        records = super(SiriusViewFieldBlock, self).create(vals_list)
        for rec in records:
            self.env['sirius.view.sequence'].create({
                'sirius_block_id': rec.id,
            })
        return super(SiriusViewFieldBlock, self).create(vals_list)