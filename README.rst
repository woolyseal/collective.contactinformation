.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=============================
collective.contactinformation
=============================

AddOn for Plone 5 with Python 2.7. to add contactinformation for distribution partners or contacts.

Features
--------

- Adds new contenttype "Contactinformation"
- Adds new behavior for setting relations between context and contacts
- Adds Macro to display connected contacts of content
- Adds View to show all contacts with countries on a world map


Examples
--------

Parts of this AddOn can be seen at:

- www.erichsen.de
- www.tbzpaderborn.de

Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has not been translated yet


Installation
------------

Install mr.developer first by adding following lines and proceed with a buildout:

    [buildout]

    extensions =
        mr.developer

Install collective.contactinformation by adding it to your buildout now:

    [buildout]

    auto-checkout = 
        collective.contactinformation

    ...

    eggs =
        collective.contactinformation

    ...

    [sources]

    collective.contactinformation = git git://github.com/wkbkhard/collective.contactinformation.git

and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/wkbkhard/collective.contactinformation/issues
- Source Code: https://github.com/wkbkhard/collective.contactinformation


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
