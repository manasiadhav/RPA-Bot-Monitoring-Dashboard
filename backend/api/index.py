from vercel_wsgi import make_wsgi_handler

# Import the Flask app instance from app.py
from app import app as flask_app

# Create the Vercel-compatible handler
handler = make_wsgi_handler(flask_app)


