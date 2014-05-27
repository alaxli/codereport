# -*- coding: utf-8 -*-
import os
import sys
import site

site.addsitedir('/data/envcodereport/lib64/python2.6/site-packages')
site.addsitedir('/data/envcodereport/lib/python2.6/site-packages/')

current_dir = os.path.dirname(__file__)
if current_dir not in sys.path: sys.path.append(current_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'codereport.settings'

activate_env = os.path.expanduser('/data/envcodereport/bin/activate_this.py')
execfile(activate_env, dict(__file__ = activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
