from setuptools import find_packages
from setuptools import setup


version = "5.0.dev0"

setup(
    name="imio.pm.locales",
    version=version,
    description="Locales for PloneMeeting",
    long_description=open("README.rst", encoding="utf-8").read()
    + "\n"
    + open("CHANGES.rst", encoding="utf-8").read(),
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="plone i18n locale translation PloneMeeting egov communesplone imio plonegov",
    author="Gauthier Bastien",
    author_email="gauthier@imio.be",
    url="https://github.com/IMIO/imio.pm.locales",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
    ],
    extras_require={"test": ["plone.app.testing"]},
)
