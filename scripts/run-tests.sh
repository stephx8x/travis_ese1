#!/bin/bash

set -ev

name="oui"


if [ $name == "ouii" ]
then 
    echo "ouiiiiiiiiiii"
else
    echo "NONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
fi


echo "continuuuuuuuuuuuu"


aa=$(ls -l)
echo "$aa"
echo "---------------------------------------------"

tox
mkdir gh-pages
asciidoctor-pdf text1.adoc -o gh-pages/documentation.pdf
asciidoctor text1.adoc -o gh-pages/index.html
