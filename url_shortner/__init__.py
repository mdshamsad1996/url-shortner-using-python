"""
Contained the common setting and obj which is used by most of other module
"""
import flask

app = flask.Flask(__name__)

app.config["DEBUG"] = True

domain_name = 'sh.com/'

from url_shortner import route
