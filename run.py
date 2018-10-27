import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """MAIN PAGE WITH INSTRUCTIONS"""

    return "To Send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    return "Hi {0}" + username

@app.route('/<username/<message>')
def send_message (username, message):
    return "{0}: {1}".format(username, message)

app.run(debug=True)

