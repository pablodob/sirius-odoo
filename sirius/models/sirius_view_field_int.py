# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SiriusViewFieldInt(models.Model):
    _name = "sirius.view.field.int"
    _description = "Sirius integer field"
    _inherit = ['sirius.view.field']

    default_value = fields.Integer('Default value', help='Default value for field in create form')
    hint_value = fields.Integer('Hint value', help='Hint value for field in create form')
    minimum = fields.Integer('Minimum', help='Minimum value for field. If is empty then no limit')
    maximum = fields.Integer('Maximum', help='Max length for field. If is empty then no limit')

    @api.model_create_multi
    def create(self, vals_list):
        records = super(SiriusViewFieldInt, self).create(vals_list)
        for rec in records:
            self.env['sirius.view.sequence'].create({
                'sirius_field_int_id': rec.id,
            })
        return records