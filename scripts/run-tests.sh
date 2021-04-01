#!/bin/bash
#set -e va arreter le script si il y a une commande qui de fonctionne pas et donc le buid
set -e


echo "---------------------------------------------"

tox
mkdir gh-pages
asciidoctor-pdf text1.adoc -o gh-pages/documentation.pdf
asciidoctor text1.adoc -o gh-pages/index.html

echo "---------------------------------------------"