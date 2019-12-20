# -*- coding: utf-8 -*-

from collective.contactinformation import _
from Products.Five.browser import BrowserView

# Import für Api
from plone import api

class ContactsMacro(BrowserView):
    def __call__(self):
        return self.index()

    def getContactReferences(self):
        context = self.context
        # Kontaktinformationen abrufen
        contacts = context.relatedContacts
        # leere Liste für korrekte Verlinkungen
        correct_contacts = []
        if contacts:
            for contact in contacts:
                # Prüfen ob eine der möglichen Verlinkungen kaputt ist
                # wenn nicht kaputt, in Liste schreiben für Ausgabe
                if contact.isBroken():
                    pass
                else:
                    correct_contacts.append(contact)
            return correct_contacts
        else:
            return None