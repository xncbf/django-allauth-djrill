from setuptools import setup


setup(
    name='django-allauth-djrill',
    description='Django Allauth account adapter for sending email using Mandrill templates',
    keywords='django, allauth, mailchimp, mandrill, email',
    author='Joey Wilhelm <jwilhelm@opay.io>',
    author_email='jwilhelm@opay.io',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'django>=1.3',
        'djrill>=1.4.0',
        'django-allauth>=0.20.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',

    ]
)
