from setuptools import setup, find_packages
# import os

version = '1.0.b2'

setup(name='readset.i18n',
      version=version,
      description="This package provides a Normalizer for Chinese character",
      long_description=open("README.rst").read() + "\n" +
      open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Natural Language :: Chinese (Simplified)",
          "Natural Language :: Chinese (Traditional)",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Text Processing",
      ],
      keywords='Zope Plone i18n i10n Pinyin',
      author='Jian Aijun',
      author_email='jianaijun@gmail.com',
      url='http://pypi.python.org/pypi/readset.i18n',
      license='GPL version 2',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['readset'],
      include_package_data=True,
      zip_safe=False,
      test_suite="readset.i18n",
      install_requires=[
          'setuptools',
          'zope.interface',
          'zope.component',
          'zope.publisher',
          'plone.i18n',
      ],
      extras_require={
          'test': [
              'zope.component [zcml]',
              'zope.configuration',
              'zope.browserresource',
              'plone.testing',
              'zope.testing',
          ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
