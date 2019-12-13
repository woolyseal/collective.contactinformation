# -*- coding: utf-8 -*-
from collective.contactinformation.behaviors.related_contact import IRelatedContactMarker
from collective.contactinformation.testing import COLLECTIVE_CONTACTINFORMATION_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class RelatedContactIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CONTACTINFORMATION_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_related_contact(self):
        behavior = getUtility(IBehavior, 'collective.contactinformation.related_contact')
        self.assertEqual(
            behavior.marker,
            IRelatedContactMarker,
        )
