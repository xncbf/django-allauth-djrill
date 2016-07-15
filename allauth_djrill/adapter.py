from __future__ import absolute_import, unicode_literals

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.utils import six

from .tasks import send_mandrill_template_mail

import logging

DJRILL_TEMPLATE_MAP = {
    'account/email/email_confirmation': 'email_confirmation',
    'account/email/email_confirmation_welcome': 'email_confirmation_welcome',
    'account/email/email_confirmation_signup': 'email_confirmation_signup',
    'account/email/password_reset_key': 'password_reset_key',
}


class DjrillAccountAdapter(DefaultAccountAdapter):

    def __init__(self, *args, **kwargs):
        template_map = DJRILL_TEMPLATE_MAP
        overrides = getattr(settings, 'ALLAUTH_DJRILL_TEMPLATES', {})
        template_map.update(overrides)
        self._template_map = template_map
        super(DjrillAccountAdapter, self).__init__(*args, **kwargs)

    def send_mail(self, template_prefix, email, context):
        # Allow for overriding with '' or None
        if template_prefix in self._template_map and self._template_map[template_prefix]:
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', "")
            mandrill_template = self._template_map[template_prefix]
            merge_vars = {}
            for key, value in six.iteritems(context):
                if key == 'current_site':
                    # This will always be in the context, but we don't want to pass it along
                    continue
                if key == 'user':
                    value = str(value)
                elif isinstance(value, (int, str)):
                    pass
                else:
                    raise TypeError('Unknown object in allauth email context %s: %s' % (key, value))
                merge_vars[key] = value
            send_mandrill_template_mail.apply_async(kwargs={
                'template_name': mandrill_template,
                'to': email,
                'global_merge_vars': merge_vars,
                'from_email': from_email
            })
        else:
            super(DjrillAccountAdapter, self).send_mail(template_prefix, email, context)
