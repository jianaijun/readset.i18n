import unittest2 as unittest
import transaction

from readset.i18n.normalizer.testing import READSET_I18N_INTEGRATION_TESTING
from readset.i18n.normalizer.testing import READSET_I18N_FUNCTIONAL_TESTING

from plone.testing.z2 import Browser
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD

from zope.component import getUtility
from zope.component import queryUtility

from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.i18n.normalizer.interfaces import IFileNameNormalizer
from plone.i18n.normalizer.interfaces import IURLNormalizer


class TestSetup(unittest.TestCase):

    layer = READSET_I18N_INTEGRATION_TESTING


class TestRendering(unittest.TestCase):

    layer = READSET_I18N_FUNCTIONAL_TESTING
