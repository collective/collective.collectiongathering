from collective.collectiongathering.interfaces import ICollectionGathering
from collective.collectiongathering.testing import (  # noqa
    COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest2 as unittest


class CollectionGatheringIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer = api.portal.get_tool("portal_quickinstaller")

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
