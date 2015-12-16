files="PloneMeeting plone imio.actionspanel datagridfield imio.history collective.eeafaceted.z3ctable eea collective.behavior.talcondition collective.documentgenerator"
languages="de en es fr nl"

for file in $files; do
    for language in $languages; do
        i18ndude sync --pot $file.pot $language/LC_MESSAGES/$file.po
        msgfmt -o $language/LC_MESSAGES/$file.mo $language/LC_MESSAGES/$file.po
    done
done
