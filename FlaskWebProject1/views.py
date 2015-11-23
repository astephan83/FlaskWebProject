"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/main')
def home():
    """Renders the main page."""
    return render_template(
        'main.html',
        title='Main Page',
        year=datetime.now().year,
    )

@app.route('/settings')
def contact():
    """Renders the settings page."""
    return render_template(
        'settings.html',
        title='Settings',
        year=datetime.now().year,
        message='Your settings page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
