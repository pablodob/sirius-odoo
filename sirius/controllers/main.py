# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class Sirius(http.Controller):

    @http.route('/sirius', type='json', csrf=False, auth='user')
    def sirius(self,  **kwargs):
        _logger.info('Sirius controller')
        sirius_views = request.env['sirius.view'].search([])
        _logger.info(sirius_views)
        dict_return = list()
        for view in sirius_views:
            _logger.info(request.env.user.groups_id)
            _logger.info(view.group_id)
            if view.group_id in request.env.user.groups_id:
                _logger.info("in")
                view_dict = {
                    'name': view.name,
                    'type': view.type,
                    'can_create': view.can_create,
                    'can_read': view.can_read,
                    'can_write': view.can_write,
                    'can_unlink': view.can_unlink,
                }
                fields = []
                for field in view.char_fields_ids:
                    fields.append({
                        'store_into': field.field_id.name,
                        'label': field.label,
                        'ttype': field.ttype,
                        'required': field.required,
                        'readonly': field.readonly,
                        'sequence': field.sequence,
                        'data': {
                            'default_value': field.default_value,
                            'hint_value': field.hint_value,
                            'min_length': field.min_length,
                            'max_length': field.max_length
                        }
                    })

                for field in view.int_fields_ids:
                    fields.append({
                        'store_into': field.field_id.name,
                        'label': field.label,
                        'ttype': field.ttype,
                        'required': field.required,
                        'readonly': field.readonly,
                        'sequence': field.sequence,
                        'data': {
                            'default_value': field.default_value,
                            'hint_value': field.hint_value,
                            'minimum': field.minimum,
                            'maximum': field.maximum
                        }
                    })

                for block in view.block_fields_ids:
                    fields.append({
                        'store_into': block.field_id.name,
                        'label': block.label,
                        'ttype': 'block',
                        'type': block.type
                        }
                    )
                view_dict['fields'] = fields
                dict_return.append(view_dict)
        _logger.info(dict_return)
        return dict_return