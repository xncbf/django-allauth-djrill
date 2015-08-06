=====================
django-allauth-djrill
=====================

`Django Allauth`_ account adapter for sending email through `Mandrill`_, using `Djrill`_

Installation
============

    pip install -e https://github.com/obsidiancard/django-allauth-djrill.git

Amend your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'allauth_djrill',
    )

Ensure that your `EMAIL_BACKEND` is set up to use Djrill:

    EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

Switch your allauth account adapter:

    ACCOUNT_ADAPTER = 'allauth_djrill.adapter.DjrillAccountAdapter'

.. _Django Allauth: https://github.com/pennersr/django-allauth
.. _Mandrill: http://mandrill.com/
.. _Djrill: https://github.com/brack3t/Djrill
