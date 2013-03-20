files="PloneMeeting plone"
languages="de en es fr nl"

for file in $files; do
    for language in $languages; do
        /srv/python/python273/bin/i18ndude sync --pot $file.pot $language/LC_MESSAGES/$file.po
        msgfmt -o $language/LC_MESSAGES/$file.mo $language/LC_MESSAGES/$file.po
    done
done
