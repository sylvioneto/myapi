from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    user_name = os.getenv("USER_NAME", "Not Found")
    return "Hello, {}!".format(user_name)
