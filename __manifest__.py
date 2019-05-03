# -*- coding: utf-8 -*-

{
    'name': "send_sms",
    'summary': """Send custom message on the mobile number using external services.""",
    'description': """Send SMS on Mobile using service like msg91.""",
    'author': "Elixir Techne Pvt Ltd",
    'website': "http://www.elixirtechne.com",
    'category': 'Service',
    'version': '12.0.1.0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/channel_view.xml',
        'views/sent_sms_view.xml',
        'views/res_config_settings_view.xml',
        'wizard/send_message_views.xml',
    ],
    'license': "LGPL-3",
    'installable': True,
    'application': False,
}
