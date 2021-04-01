#!/bin/bash

set -e


echo "---------------------------------------------"

tox
mkdir gh-pages
asciidocto-pdf text1.adoc -o gh-pages/documentation.pdf
asciidoctor text1.adoc -o gh-pages/index.html

echo "---------------------------------------------"