#!/usr/bin/python
activate_this = '/var/www/whatdayisitinnz/whatdayisitinnz/whatdayisitinnz/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from whatdayisitinnz import app as application