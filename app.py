from flask import Flask
app = Flask(__name__)


@app.route('/')
def function():
    return 'This is my first API call!'