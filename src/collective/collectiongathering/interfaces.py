"""Module where all interfaces, events and exceptions live."""

from plone.app.contenttypes import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveCollectiongatheringLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICollectionGathering(Interface):

    sort_on = schema.TextLine(
        title=_("label_sort_on", default="Sort on"),
        description=_("Sort the collection on this index"),
        required=False,
    )

    sort_reversed = schema.Bool(
        title=_("label_sort_reversed", default="Reversed order"),
        description=_("Sort the results in reversed order"),
        required=False,
    )

    limit = schema.Int(
        title=_("Limit"),
        description=_("Limit Search Results"),
        required=False,
        default=1000,
        min=1,
    )

    item_count = schema.Int(
        title=_("label_item_count", default="Item count"),
        description=_("Number of items that will show up in one batch."),
        required=False,
        default=30,
        min=1,
    )
