from imio.pm.locales.testing import INTEGRATION_TESTING
from zope.component import getUtility
from zope.i18n import translate
from zope.i18n.interfaces import ITranslationDomain

import imio.pm.locales
import os
import unittest


LOCALES = os.path.join(os.path.dirname(imio.pm.locales.__file__), "locales")


class TestLocales(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def test_registerTranslations(self):
        # every .po file of the package is registered (compiled to .mo) in its domain
        pos = []
        for lang in os.listdir(LOCALES):
            lc_messages = os.path.join(LOCALES, lang, "LC_MESSAGES")
            if not os.path.isdir(lc_messages):
                continue
            for name in os.listdir(lc_messages):
                if name.endswith(".po"):
                    domain = name[:-3]
                    pos.append((domain, lang))
                    infos = getUtility(ITranslationDomain, domain).getCatalogsInfo()
                    self.assertIn(
                        os.path.join(lc_messages, domain + ".mo"), infos[lang]
                    )
        # 13 domains in de, en, es, fr and nl
        self.assertEqual(len(pos), 65)
        self.assertEqual(
            sorted(set(lang for domain, lang in pos)), ["de", "en", "es", "fr", "nl"]
        )

        # known msgids translate
        expected = {
            "de": "Anhang hinzufügen",
            "en": "Add an annex",
            "es": "Agregar un anexo",
            "fr": "Ajouter une annexe",
            "nl": "Voeg een bijlage toe",
        }
        for lang, msgstr in expected.items():
            self.assertEqual(
                translate("add_annex", domain="PloneMeeting", target_language=lang),
                msgstr,
            )
        self.assertEqual(
            translate("MeetingItem", domain="plone", target_language="fr"), "Point"
        )
        self.assertEqual(
            translate("MeetingItem", domain="plone", target_language="es"),
            "Tema de reunión",
        )
        self.assertEqual(
            translate(
                "Add recurring item_comments",
                domain="imio.history",
                target_language="fr",
            ),
            "Ce point a été automatiquement ajouté comme point récurrent à la séance.",
        )
