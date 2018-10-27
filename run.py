from flask import Flask, redirect
from datetime import datetime
app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the message list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {}: {}".format(now, username, message))

def get_all_messages():
    """Get all the messages and split them by a br"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """MAIN PAGE WITH INSTRUCTIONS"""

    return "To Send a message use /USERNAME/MESSAGE"

@app.route('/<username>')
def user(username):
    """Display chat messages"""

    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message (username, message):
    """Create a new message and redirect back to the chat page"""

    add_messages(username, message)
    return redirect(username)

app.run(debug=True)

