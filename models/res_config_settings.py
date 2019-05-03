# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_send_sms = fields.Boolean('Send SMS', implied_group="base.group_user")
    default_channel = fields.Many2one('sms.channel', string="Channel", default_model='message.send_sms')
