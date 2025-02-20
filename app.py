from flask import Flask, render_template_string
from dash import Dash

def create_flask_app():
    """Creates the Flask app."""
    flask_app = Flask(__name__)

    # Define a home route
    @flask_app.route('/')
    def home():
        return render_template_string("""
           <!DOCTYPE html>
           <html>
           <head>
               <title>Home Page</title>
           </head>
           <body>
               <h1>Workforce Analysis of UK</h1>
               <p>Select a dashboard:</p>
               <ul>
                   <li><a href="/regional_dash/">Regional Analysis</a></li>
                   <li><a href="/industrial_dash/">Industrial Analysis</a></li>
                   <li><a href="/full_part_dash/">Full-time & Part-time jobs Analysis</a></li>
                   <li><a href="/timeseries_dash/">Time Series Analysis</a></li>
               </ul>
           </body>
           </html> 
           """)
    return flask_app

def create_dash_app(flask_app, name, url_base_pathname):
    """Creates a Dash app."""
    dash_app = Dash(
        __name__,
        server=flask_app,
        url_base_pathname=url_base_pathname,
        external_stylesheets=["https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"]
    )
    return dash_app
