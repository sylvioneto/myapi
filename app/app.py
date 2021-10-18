from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    user_name = os.getenv("USER_NAME", "Not Found")
    return "Hello, {}!".format(user_name)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')

