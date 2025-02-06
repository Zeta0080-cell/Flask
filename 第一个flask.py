from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World!"

@app.route('/hello')
def hello():
    return '<h1>Hello!<h1>'

app.run()