import unittest2 as unittest
import doctest

from plone.testing import layered
from plone.testing import zca

from plone.app.testing import PLONE_INTEGRATION_TESTING

def test_suite():
    
    return unittest.TestSuite([
        layered(doctest.DocFileSuite('containment.txt'),    PLONE_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('acquisition.txt'),    PLONE_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('path_traversal.txt'), PLONE_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('catalog.txt'),        PLONE_INTEGRATION_TESTING),
        layered(doctest.DocFileSuite('interfaces.txt'),     zca.UNIT_TESTING),
        layered(doctest.DocFileSuite('utilities.txt'),      zca.UNIT_TESTING),
        layered(doctest.DocFileSuite('adapters.txt'),       zca.UNIT_TESTING),
        layered(doctest.DocFileSuite('events.txt'),         zca.EVENT_TESTING),
        ])
