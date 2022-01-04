from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return "sup bro"

if __name__ == "__main__":
    app.run(Debug=True)