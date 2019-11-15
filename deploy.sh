#!/bin/sh

echo 'Starting...'
echo

echo 'Update linkedIn certificates page'
echo
python update_certificate_md.py

echo 'Create src/downloads/RobinDeGuzmanCv.docx'
echo
sh create_resume.sh

echo 'Deploying to github'
echo
mkdocs gh-deploy

echo 'finished'
echo