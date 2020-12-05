# Versions
python 3.6.9, 3.7.3, 3.8.2
pip 9.0.1, 19.3.1
pandoc 1.19.2.4, 2.7.3
virtualenv 16.7.2
venv ???


# Run server
1. source env/bin/activate or source env/Scripts/activate
2. mkdocs serve


# Deploy to github
1. source env/bin/activate or source env/Scripts/activate
2. python update_certificate_md.py
3. sh create_resume.sh
4. mkdocs gh-deploy
5. deactivate

or 

1. source env/bin/activate or source env/Scripts/activate
2. sh deploy.sh


# Build static html files w/o pushing to Github
1. mkdocs build


# Setup
1. git clone git@github.com:rfdeguzman21/rfdeguzman21.github.io.git
2. git checkout develop `master branch contains html files`
3. python3 -m venv env
4. source env/bin/activate or source env/Scripts/activate
5. pip install requirements.txt
6. when done, deactivate
