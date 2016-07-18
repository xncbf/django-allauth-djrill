from setuptools import find_packages, setup


VERSION = __import__('allauth_djrill').__version__
github_url = 'https://github.com/polejak/django-allauth-djrill'

setup(
    name='django-allauth-djrill',
    version=VERSION,
    url=github_url,
    license='Apache',
    description='Django Allauth account adapter for sending email using Mandrill templates',
    long_description=open('README.rst').read(),
    keywords='django, allauth, mailchimp, mandrill, email',
    author='Joey Wilhelm <jwilhelm@opay.io>',
    author_email='jwilhelm@opay.io',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.3',
        'djrill>=1.4.0',
        'django-allauth>=0.20.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: Apache Software License',
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
