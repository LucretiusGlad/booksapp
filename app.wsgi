#!/usr/bin/python
import sys, os
cur_dir = os.path.dirname(os.path.abspath(__name__))
sys.path.insert(0,"cur_dir")

from app import app as application
application.secret_key = 'Add your secret key'
