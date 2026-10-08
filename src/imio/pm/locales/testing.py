# -*- coding: utf-8 -*-
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import imio.pm.locales


class ImioPmLocalesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=imio.pm.locales)


FIXTURE = ImioPmLocalesLayer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="ImioPmLocalesLayer:IntegrationTesting"
)
