from flask import Flask, request
import sys
import os

# Add parent directory to path so we can import from main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

# For Vercel serverless deployment
def handler(request):
    return app.wsgi_app(request.environ, lambda x, y: y) 