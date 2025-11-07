from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name')
def helloPlayer():
    return render_template("poemTemplate.html")

@app.route('/')
def hello_world():
    return """Hello World"""

if __name__=='__main__':
    app.run()