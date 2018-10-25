from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there!</h1>"

app.run

debug = True