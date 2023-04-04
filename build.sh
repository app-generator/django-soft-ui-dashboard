#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

# recompile scss
npm install gulp-cli
npm i 
gulp 

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
