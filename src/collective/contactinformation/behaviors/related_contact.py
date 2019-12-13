# -*- coding: utf-8 -*-

from collective.contactinformation import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider

class IRelatedContactMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IRelatedContact(model.Schema):
    relatedContacts = RelationList(
        title=_(u'Zugewiesene Kontakte'),
        default=[],
        required=False,
        description=_(u'Bitte weisen Sie hier einen oder mehrere Kontakte zu, welche zu dem jeweiligen Inhalt gehoeren.'),
        value_type=RelationChoice(
            title=_(u'Kontakte'),
            source=CatalogSource(portal_type=['Contactinformation'])
        ),
    )

@implementer(IRelatedContact)
@adapter(IRelatedContactMarker)
class RelatedContact(object):
    def __init__(self, context):
        self.context = context

    @property
    def relatedContacts(self):
        if hasattr(self.context, 'relatedContacts'):
            return self.context.relatedContacts
        return None

    @relatedContacts.setter
    def relatedContacts(self, value):
        self.context.relatedContacts = value
