from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.collectiongathering


class CollectiveCollectiongatheringLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.collectiongathering)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.collectiongathering:default")


COLLECTIVE_COLLECTIONGATHERING_FIXTURE = CollectiveCollectiongatheringLayer()


COLLECTIVE_COLLECTIONGATHERING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_COLLECTIONGATHERING_FIXTURE,),
    name="CollectiveCollectiongatheringLayer:IntegrationTesting",
)


COLLECTIVE_COLLECTIONGATHERING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_COLLECTIONGATHERING_FIXTURE,),
    name="CollectiveCollectiongatheringLayer:FunctionalTesting",
)


COLLECTIVE_COLLECTIONGATHERING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_COLLECTIONGATHERING_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CollectiveCollectiongatheringLayer:AcceptanceTesting",
)
