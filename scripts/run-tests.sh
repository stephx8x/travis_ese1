#!/bin/bash
#set -e va arreter le script si il y a une commande qui de fonctionne pas et donc le buid
set -ev


echo "---------------------------------------------"

mkdir public
asciidoctor-pdf text1.adoc -o public/documentation.pdf
asciidoctor text1.adoc -o public/index.html

echo "---------------------------------------------"