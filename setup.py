# -*- coding: utf-8 -*-
"""Installer for the readset.i18n package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='readset.i18n',
    version='1.0',
    description="This package provides a Normalizer for Chinese character",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Chinese (Traditional)",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords='Python Plone i18n i10n normalizer',
    author='Jian Aijun',
    author_email='jianaijun@gmail.com',
    url='https://pypi.org/project/readset.i18n',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['readset'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.component',
        'zope.publisher',
        'plone.i18n',
        'python-slugify',
    ],
    extras_require={
        'test': [
            'zope.component [zcml]',
            'zope.configuration',
            'zope.browserresource',
            'plone.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
