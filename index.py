#!/usr/bin/env python3

import sys
import os

# Add the directory to Python path
sys.path.insert(0, '/web/groups/gustyai/public_html')
os.chdir('/web/groups/gustyai/public_html')

# Import your Flask app
from genai_studio_app import app

# Run as CGI
if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
