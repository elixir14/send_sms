# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields


class SmsChannel(models.Model):
    _name = 'sms.channel'
    _description = "Channel"

    name = fields.Char(reqiured=True, help="Channel Name")
    sms_url = fields.Char(required=True, help="URL of the service provider")
    sms_auth_key = fields.Char(required=True, help="auth key from your account on service provider")
    sms_sender = fields.Char(required=True)
    route = fields.Integer(required=True)


class SentSms(models.Model):
    _name = 'sent.sms'
    _description = 'Sent SMS'

    partner = fields.Many2one('res.partner')
    channel = fields.Many2one('sms.channel')
    mobile = fields.Char()
    time = fields.Datetime(default=datetime.datetime.now())
    message = fields.Char()
    status = fields.Char()
