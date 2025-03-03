from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cs.adminlanguage


class CsAdminlanguageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

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


CS_ADMINLANGUAGE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CS_ADMINLANGUAGE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CsAdminlanguageLayer:AcceptanceTesting",
)
