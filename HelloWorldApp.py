from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/name')
def helloPlayer():
    return render_template("poemTemplate.html")

@app.route('/')
def hello_world():
    return """Hello World"""

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # default to 5000 locally
    app.run(host='0.0.0.0', port=port)