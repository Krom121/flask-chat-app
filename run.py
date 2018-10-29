from flask import Flask, redirect, render_template, request
from datetime import datetime
app = Flask(__name__)

def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

def add_messages(username, message):
    """Add messages to the message text file"""

    write_to_file("data/messages.txt", "({0}) {1} - {2}".format(
            datetime.now().strftime("%H:%M:%S"),
            username.title(), 
            message))

def get_all_messages():
    """Get all the messages and split them by a br"""
    messages = []
    with open("data/messages.txt", "r") as chat_messages:
        messages = chat_messages.readlines()
        return messages

@app.route('/', methods=["GET", "POST"])
def index():
    """MAIN PAGE WITH INSTRUCTIONS"""
    if request.method == "POST":

        # Handle Post request

        write_to_file("data/users.txt", request.form["username"])
        return redirect(request.form["username"])    
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display chat messages"""
    messages = get_all_messages()
    return render_template("chat.html", username=username, chat_messages=messages)

@app.route('/<username>/<message>')
def send_message (username, message):
    """Create a new message and redirect back to the chat page"""

    add_messages(username, message)
    return redirect(username)

app.run(debug=True)