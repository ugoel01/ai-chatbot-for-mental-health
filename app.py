# import files
from flask import Flask, render_template, request
from bot_model import generate_answer

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(generate_answer(userText))


if __name__ == "__main__":
    app.run()
