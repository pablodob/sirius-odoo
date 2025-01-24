# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SiriusViewFieldChar(models.Model):
    _name = "sirius.view.field.int"
    _description = "Sirius integer field"
    _inherit = ['sirius.view.field']

    default_value = fields.Integer('Default value', help='Default value for field in create form')
    hint_value = fields.Integer('Hint value', help='Hint value for field in create form')
    minimum = fields.Integer('Minimum', help='Minimum value for field. If is empty then no limit')
    maximum = fields.Integer('Maximum', help='Max length for field. If is empty then no limit')