#!/usr/bin/env python3

import sys
import os

# Add the directory to Python path
sys.path.insert(0, '/web/groups/gustyai/public_html')
os.chdir('/web/groups/gustyai/public_html')

from genaiStudio_app import app
from wsgiref.handlers import CGIHandler

CGIHandler().run(app)