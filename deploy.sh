#!/bin/bash

echo 'Starting...'
echo

echo 'Update linkedIn certificates page'
echo
python3 update_certificate_md.py

echo 'Create src/downloads/RobinDeGuzmanCv.docx'
echo
sh create_resume.sh

echo 'Deploying to github'
echo
env/bin/mkdocs gh-deploy

echo 'Finished deploying to github pages.'
echo