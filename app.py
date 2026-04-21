from flask import Flask

app = Flask("myapp")

@app.route("/")
def home():
    return "DevOps Feature Update 🚀"

app.run(host="127.0.0.1", port=5000)
