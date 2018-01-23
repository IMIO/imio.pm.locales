from setuptools import setup, find_packages
import os

version = '4.1b4.dev0'

setup(name='imio.pm.locales',
      version=version,
      description="Locales for PloneMeeting",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='plone i18n locale translation PloneMeeting egov communesplone imio plonegov',
      author='',
      author_email='',
      url='http://svn.communesplone.org/svn/communesplone/imio.pm.locales/',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['imio', 'imio.pm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing', 'unittest2']},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
