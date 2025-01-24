# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SiriusViewFieldChar(models.Model):
    _name = "sirius.view.field.char"
    _description = "Sirius char field"
    _inherit = ['sirius.view.field']

    default_value = fields.Char('Default value', help='Default value for field in create form')
    hint_value = fields.Char('Hint text', help='Hint text for field in create form')
    min_length = fields.Integer('Min length', help='Min length for field')
    max_length = fields.Integer('Max length', help='Max length for field')
