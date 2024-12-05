"""Setup tests for this package."""

from collective.collectiongathering.testing import (  # noqa
    COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING,
)
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.collectiongathering is properly installed."""

    layer = COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if collective.collectiongathering is installed with portal_quickinstaller."""
        self.assertTrue(
            self.installer.isProductInstalled("collective.collectiongathering")
        )

    def test_uninstall(self):
        """Test if collective.collectiongathering is cleanly uninstalled."""
        self.installer.uninstallProducts(["collective.collectiongathering"])
        self.assertFalse(
            self.installer.isProductInstalled("collective.collectiongathering")
        )

    def test_browserlayer(self):
        """Test that ICollectiveCollectiongatheringLayer is registered."""
        from collective.collectiongathering.interfaces import (
            ICollectiveCollectiongatheringLayer,
        )
        from plone.browserlayer import utils

        self.assertIn(ICollectiveCollectiongatheringLayer, utils.registered_layers())
