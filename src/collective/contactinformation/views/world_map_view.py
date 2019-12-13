# -*- coding: utf-8 -*-

from collective.contactinformation import _
from Products.Five.browser import BrowserView

# Import für Api
from plone import api

# Import für Länderfunktionen
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

class WorldMapView(BrowserView):
    def all_contacts(self):
        catalog = api.portal.get_tool('portal_catalog')
        results = catalog.searchResults(
            portal_type='Contactinformation'
        )
        return results

    def getCountries(self):
        factory = getUtility(IVocabularyFactory, 'collective.contactinformation.CountryInformation')
        countries = factory(self.context)
        return countries

    def getCountryToken(self, term):
        factory = getUtility(IVocabularyFactory, 'collective.contactinformation.CountryInformation')
        countries = factory(self.context)
        token = countries.getTerm(term)
        return token

    # Gibt Liste von Vokabular aus in Form von token z.B. 'de', title z.B. 'Germany' und value gleich wie token
    def countriesUsed(self):
        allCountries = self.getCountries()
        all_contacts = self.all_contacts()
        countriesUsed = [x.getObject().landerauwahl_einfach for x in all_contacts if x.getObject().landerauwahl_einfach]
        listOfUsedCountries = [x for x in allCountries._terms if x.token in countriesUsed]
        return listOfUsedCountries