from odoo import models, fields, api

class SiriusFieldWizard(models.TransientModel):
    _name = "sirius.field.wizard"
    _description = "Wizard para agregar campos"

    sirius_block_id = fields.Many2one('sirius.view.block', string='Block')
    sirius_field_char_id = fields.Many2one('sirius.view.field.char', string='Field')
    sirius_field_int_id = fields.Many2one('sirius.view.field.int', string='Field')

    label = fields.Char(string="Label", required=True)
    sirius_view_id = fields.Many2one('sirius.view', string='View', required=True, ondelete='cascade')
    model_id = fields.Many2one(related='sirius_view_id.model_id', string='Model', store=True)
    field_id = fields.Many2one("ir.model.fields", string="Field", domain="[('ttype', '=', field_type), ('model_id','=',model_id)]")
    field_type = fields.Selection([
        ('char', 'Char'),
        ('integer', 'Integer'),
        ('block', 'Block')
    ], string="Field Type", required=True)
    required = fields.Boolean('Required', default=False)
    edit_required = fields.Boolean('Required editable', default=True)
    readonly = fields.Boolean('Readonly', default=True)
    edit_readonly = fields.Boolean('Readonly editable', default=True)

    default_value = fields.Char(string="Default Value")
    hint_value = fields.Char(string="Hint")
    min_length = fields.Integer(string="Min Length")
    max_length = fields.Integer(string="Max Length")
    minimum = fields.Integer(string="Minimum")
    maximum = fields.Integer(string="Maximum")

    image = fields.Binary('Image')
    type = fields.Selection([('text','Text'),('h1','H1'),('h2','H2'),('h3','H3'),('image','Image')], string='Type')

    @api.onchange('field_id', 'sirius_view_id')
    def _onchange_field_id(self):
        if self.field_id:
            self.edit_required = not self.field_id.required
            self.edit_readonly = not self.field_id.readonly
            self.required = self.field_id.required
            self.readonly = self.field_id.readonly
        else:
            self.edit_required = False
            self.edit_readonly = False

        if not self.sirius_view_id.can_write:
            self.readonly = True
            self.edit_readonly = False
            self.edit_required = False

    def action_save_field(self):
        """Guarda el campo en la vista Sirius dependiendo de su tipo"""
        if self.sirius_field_char_id:
            self.sirius_field_char_id.update({
                'label': self.label,
                'required': self.required,
                'readonly': self.readonly,
                'default_value': self.default_value,
                'hint_value': self.hint_value,
                'min_length': self.min_length,
                'max_length': self.max_length
            })
        elif self.sirius_field_int_id:
            self.sirius_field_int_id.update({
                'label': self.label,
                'required': self.required,
                'readonly': self.readonly,
                'default_value': self.default_value,
                'hint_value': self.hint_value,
                'minimum': self.minimum,
                'maximum': self.maximum
            })
        elif self.sirius_block_id:
            self.sirius_block_id.update({
                'label': self.label,
                'type': self.type,
                'image': self.image,
            })
        elif self.field_type == 'char':
            self.sirius_view_id.char_fields_ids.create({
                'view_id': self.sirius_view_id.id,
                'label': self.label,
                'field_id': self.field_id.id,
                'required': self.required,
                'readonly': self.readonly,
                'default_value': self.default_value,
                'hint_value': self.hint_value,
                'min_length': self.min_length,
                'max_length': self.max_length
            })
        elif self.field_type == 'integer':
            self.sirius_view_id.int_fields_ids.create({
                'view_id': self.sirius_view_id.id,
                'label': self.label,
                'field_id': self.field_id.id,
                'required': self.required,
                'readonly': self.readonly,
                'default_value': self.default_value,
                'hint_value': self.hint_value,
                'minimum': self.minimum,
                'maximum': self.maximum,
            })
        elif self.field_type == 'block':
            self.sirius_view_id.block_fields_ids.create({
                'view_id': self.sirius_view_id.id,
                'type': self.type,
                'label': self.label,
                'image': self.image
            })
        return {'type': 'ir.actions.act_window_close'}
