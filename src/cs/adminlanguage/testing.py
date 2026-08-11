from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import cs.adminlanguage


class CsAdminlanguageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=cs.adminlanguage)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "cs.adminlanguage:default")


CS_ADMINLANGUAGE_FIXTURE = CsAdminlanguageLayer()


CS_ADMINLANGUAGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CS_ADMINLANGUAGE_FIXTURE,),
    name="CsAdminlanguageLayer:IntegrationTesting",
)


CS_ADMINLANGUAGE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CS_ADMINLANGUAGE_FIXTURE,),
    name="CsAdminlanguageLayer:FunctionalTesting",
)
