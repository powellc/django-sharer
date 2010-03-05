#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# Dynamically calculate the version based on sharer.VERSION
version_tuple = __import__('sharer').VERSION
if len(version_tuple) == 3:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = "django-sharer",
    version = version,
    description = "sharer management for the Django web framework.",
    author = "Colin Powell",
    author_email = "cpowel@penobscotbaypress.com",
    url = "http://src.coastalconnect.me/django-sharer/",
    packages = find_packages(),
    package_data = {
        'sharer': [
            'templates/sharer/*.html',
        ]
    },
    zip_safe = False,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)

