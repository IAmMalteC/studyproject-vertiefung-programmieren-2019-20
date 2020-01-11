from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to Flask"

# Just for debuging -- REMOVE before delivering
if __name__ == "__main__":
    app.run(debug=True)
