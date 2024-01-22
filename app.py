from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()
    setup = joke["setup"]
    punchline = joke["punchline"]
    return render_template("index.html", title="Hello", setup=setup, punchline=punchline)
