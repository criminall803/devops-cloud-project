from flask import Flask

app = Flask("myapp")

@app.route("/")
def home():
    return "DevOps App Running 🚀"

app.run(host="127.0.0.1", port=5000)