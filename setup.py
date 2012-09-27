#!/usr/bin/env python
from setuptools import setup, find_packages

import mailchimp

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'mailchimp api wrapper 1.3'

setup(name='python-mailchimp',
      version=mailchimp.__version__,
      description="""MailChimp API v1.3 wrapper for Python.""",
      author=mailchimp.__author__,
      url='https://github.com/eugene-wee/python-mailchimp',
      packages=find_packages(),
      download_url='https://github.com/eugene-wee/python-mailchimp/tarball/master',
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      zip_safe=True,
      install_requires=['distribute'])
