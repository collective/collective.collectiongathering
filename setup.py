"""Installer for the collective.collectiongathering package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open("README.rst").read() + "\n" + "Contributors\n"
    "============\n"
    + "\n"
    + open("CONTRIBUTORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read()
    + "\n"
)


setup(
    name="collective.collectiongathering",
    version="0.1",
    description="A Dexterity content type which can gather multiple collection into one.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords="Python Plone",
    author="Gagaro",
    author_email="yfo@makina-corpus.com",
    url="http://pypi.python.org/pypi/collective.collectiongathering",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Acquisition",
        "plone.app.contenttypes",
        "plone.app.dexterity",
        "plone.base"
        "plone.batching",
        "plone.dexterity",
        "Products.CMFPlone",
        "Products.GenericSetup",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.contenttypes",
            "plone.app.testing",
            "plone.browserlayer",
            "plone.dexterity",
            "plone.testing",
            "zope.component",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
