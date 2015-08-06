from __future__ import absolute_import, unicode_literals

from django.core.mail import EmailMessage
from django.utils import six
try:
    # Use celery if it is available
    from celery import shared_task
except ImportError:
    # Emulate apply_async, in the case that celery isn't installed
    def shared_task(func):
        def apply_async(self, args=None, kwargs=None, task_id=None, producer=None, link=None, link_error=None,
                        shadow=None, **options):
            if not args:
                args = []
            if not kwargs:
                kwargs = {}
            return func(*args, **kwargs)
        func.apply_async = apply_async
        return func


# https://djrill.readthedocs.org/en/v1.4/usage/sending_mail/#mandrill-specific-options
VALID_DJRILL_OPTIONS = [
    'important', 'track_opens', 'track_clicks', 'auto_text', 'auto_html', 'inline_css', 'url_strip_qs',
    'preserve_recipients', 'view_content_link', 'tracking_domain', 'signing_domain', 'return_path_domain',
    'merge_language', 'tags', 'subaccount', 'google_analytics_domain', 'google_analytics_campaign', 'metadata',
    'recipient_metadata', 'async', 'ip_pool', 'send_at'
]


@shared_task
def send_mandrill_template_mail(template_name, to, global_merge_vars=None, merge_vars=None, content_blocks=None,
                                subject=None, from_email=None, **options):
    if isinstance(to, six.string_types):
        to = [to]
    msg = EmailMessage(subject=subject, from_email=from_email, to=to)
    msg.template_name = template_name
    if content_blocks:
        msg.template_content = content_blocks
    if global_merge_vars:
        msg.global_merge_vars = global_merge_vars
    if merge_vars:
        msg.merge_vars = merge_vars
    for option, value in six.iteritems(options):
        if option not in VALID_DJRILL_OPTIONS:
            raise ValueError('Invalid option for Mandrill template: %s' % option)
        setattr(msg, option, value)
    if not subject:
        msg.use_template_subject = True
    if not from_email:
        msg.use_template_from = True
    msg.send()
