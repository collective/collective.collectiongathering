from collective.collectiongathering.interfaces import ICollectionGathering
from collective.collectiongathering.testing import (  # noqa
    COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility
from plone import api
import unittest


class CollectionGatheringIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name="CollectionGathering")
        schema = fti.lookupSchema()
        self.assertEqual(ICollectionGathering, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name="CollectionGathering")
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name="CollectionGathering")
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ICollectionGathering.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory("CollectionGathering", "CollectionGathering")
        self.assertTrue(
            ICollectionGathering.providedBy(self.portal["CollectionGathering"])
        )


class CollectionGathersOtherCollections(unittest.TestCase):
    layer = COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

        self.collection_gather = api.content.create(
            container=self.portal,
            id="collection_gather",
            title="Gather",
            type="CollectionGathering",
            sort_on="created",
            sort_reversed=False,
            limit=20,
            item_count=100,
        )

        self.collection1 = api.content.create(
            container=self.collection_gather,
            id="collection1",
            title="Collection 1",
            type="Collection",
            query=[
                {
                    "i": "portal_type",
                    "o": "plone.app.querystring.operation.selection.any",
                    "v": ["News Item"],
                }
            ],
        )
        self.collection2 = api.content.create(
            container=self.collection_gather,
            id="collection2",
            title="Collection 2",
            type="Collection",
            query=[
                {
                    "i": "portal_type",
                    "o": "plone.app.querystring.operation.selection.any",
                    "v": ["Event"],
                }
            ],
        )

        self.news1 = api.content.create(
            container=self.portal,
            id="news1",
            title="News 1",
            type="News Item",
        )

        self.news2 = api.content.create(
            container=self.portal,
            id="news2",
            title="News 2",
            type="News Item",
        )

        self.event1 = api.content.create(
            container=self.portal,
            id="event1",
            title="Event 1",
            type="Event",
        )

        self.news2 = api.content.create(
            container=self.portal,
            id="event2",
            title="Event 2",
            type="Event",
        )

    def test_gathering(self):

        results = self.collection1.results(batch=False)
        self.assertEqual(len(results), 2)

        results = self.collection2.results(batch=False)
        self.assertEqual(len(results), 2)

        results = self.collection_gather.results(batch=False)
        self.assertEqual(len(results), 4)
