.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.collectiongathering
==============================================================================

A Dexterity content type which can gather multiple collection into one.

To do so create a `CollectionGathering` object in your Plone site, and add inside it the collections you want
to gather in the main one, and configure each one independently.


Translations
------------

This product has been translated into

- English


Installation
------------

Install collective.collectiongathering by adding it to your buildout::

   [buildout]

    ...

    eggs =
        collective.collectiongathering


and then running "bin/buildout"



Contribute
----------

- Issue Tracker: https://github.com/collective/collective.collectiongathering/issues
- Source Code: https://github.com/collective/collective.collectiongathering


License
-------

The project is licensed under the GPLv2.
