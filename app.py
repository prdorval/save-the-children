from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "This is a placeholder for your webapp's opening page."

@app.get("/fromTexas")
def bycad():
    return "This is a new page."


if __name__ == "__main__":
    app.run()