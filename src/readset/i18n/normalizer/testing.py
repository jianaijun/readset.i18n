from zope.configuration import xmlconfig

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class ReadsetI18n(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import readset.i18n.normalizer
        xmlconfig.file(
            'configure.zcml',
            readset.i18n.normalizer,
            context=configurationContext)

READSET_I18N_FIXTURE = ReadsetI18n()
READSET_I18N_INTEGRATION_TESTING = IntegrationTesting(
    bases=(READSET_I18N_FIXTURE,), name="ReadsetI18n:Integration")
READSET_I18N_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(READSET_I18N_FIXTURE,), name="ReadsetI18n:Functional")
