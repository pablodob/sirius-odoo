# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class SiriusView(models.Model):
    _name = "sirius.view"
    _description = "Sirius view"

    name = fields.Char('View name')
    model_id = fields.Many2one('ir.model', string='Model')
    type = fields.Selection(selection=[('form', 'Form'),
                                            ('tree', 'Tree')], string='Type')
    can_read = fields.Boolean('Can read', default=True)
    can_write = fields.Boolean('Can edit', default=True)
    can_create = fields.Boolean('Can create', default=True)
    can_unlink = fields.Boolean('Can delete', default=False)
    group_id = fields.Many2one('res.groups', string='User group allow')
    char_fields_ids = fields.One2many('sirius.view.field.char', 'view_id', string='Fields')
    int_fields_ids = fields.One2many('sirius.view.field.int', 'view_id', string='Fields')