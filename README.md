# Versions
python 3.7.3
pip 19.3.1
pandoc 2.7.3
virtualenv 16.7.2


# Run server
1. mkdocs serve


# Deploy to github
1. source env/Scripts/activate
2. python update_certificate_md.py
3. sh create_resume.sh
4. mkdocs gh-deploy

or run command `sh deploy.sh`


# Build static html files w/o pushing to Github
1. mkdocs build


# Setup
1. git clone git@github.com:rfdeguzman21/rfdeguzman21.github.io.git
2. git checkout develop `master branch contains html files`
3. virtual env
4. source env/Scripts/activate
5. pip install requirements.txt
