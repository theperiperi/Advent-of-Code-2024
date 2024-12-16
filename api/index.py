import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# This is for Vercel
def handler(request, context):
    return app(request, context) 