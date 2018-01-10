=====================
django-allauth-mandrill
=====================

Since existing repositories are no longer being managed, So it is Hard fork for management.

This package provides a `django-allauth`_ account adapter for sending email utilizing templates stored in `Mandrill`_,
thanks to the `Djrill`_ package.

Installation
============

To install the latest release::

    pip install django-allauth-mandrill

Alternatively, to install the latest development version::

    pip install https://github.com/xncbf/django-allauth-mandrill/tarball/master

Amend your `INSTALLED_APPS` setting::

    INSTALLED_APPS = (
        ...,
        'allauth_djrill',
    )

Ensure that your `EMAIL_BACKEND` is set up to use Djrill::

    EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

Switch your allauth account adapter::

    ACCOUNT_ADAPTER = 'allauth_djrill.adapter.DjrillAccountAdapter'

If you wish to customize the names of the templates which are called in Mandrill's system, you can edit the
`ALLAUTH_DJRILL_TEMPLATES` setting. The defaults are::

    ALLAUTH_DJRILL_TEMPLATES = {
        'account/email/email_confirmation': 'email_confirmation',
        'account/email/email_confirmation_welcome': 'email_confirmation_welcome',
        'account/email/email_confirmation_signup': 'email_confirmation_signup',
        'account/email/password_reset_key': 'password_reset_key',
    }

.. _django-allauth: https://github.com/pennersr/django-allauth
.. _Mandrill: http://mandrill.com/
.. _Djrill: https://github.com/brack3t/Djrill
