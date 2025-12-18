from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello CI/CD Security"

if __name__ == "__main__":
    app.run()
