#!/usr/bin/env bash
files="PloneMeeting plone imio.actionspanel datagridfield imio.annex imio.history collective.eeafaceted.batchactions collective.eeafaceted.z3ctable eea collective.behavior.talcondition collective.documentgenerator collective.iconifiedcategory collective.contact.core"
languages="de en es fr nl"

for file in $files; do
    for language in $languages; do
        touch $language/LC_MESSAGES/$file.po
        i18ndude sync --pot $file.pot $language/LC_MESSAGES/$file.po
        msgfmt -o $language/LC_MESSAGES/$file.mo $language/LC_MESSAGES/$file.po
    done
done
