# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.contactinformation


class CollectiveContactinformationLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.contactinformation)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.contactinformation:default')


COLLECTIVE_CONTACTINFORMATION_FIXTURE = CollectiveContactinformationLayer()


COLLECTIVE_CONTACTINFORMATION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CONTACTINFORMATION_FIXTURE,),
    name='CollectiveContactinformationLayer:IntegrationTesting',
)


COLLECTIVE_CONTACTINFORMATION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CONTACTINFORMATION_FIXTURE,),
    name='CollectiveContactinformationLayer:FunctionalTesting',
)


COLLECTIVE_CONTACTINFORMATION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CONTACTINFORMATION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveContactinformationLayer:AcceptanceTesting',
)
