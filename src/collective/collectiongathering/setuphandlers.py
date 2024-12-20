from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.collectiongathering:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return ["collective.collectiongathering.upgrades"]


def post_install(context):
    """Post install script"""
    # Do something during the installation of this package


def post_uninstall(context):
    """Post uninstall script"""
    # Do something during the installation of this package
