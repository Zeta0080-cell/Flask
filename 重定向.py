# 重定向 302

from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return redirect('https://www.baidu.com')

@app.route('/')
def hello():
    return 'this is hello function'

if __name__ == '__main__':
    app.run()