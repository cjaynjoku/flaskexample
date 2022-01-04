from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return "hello there good sir"

if __name__ == "__main__":
    app.run(Debug=True)