from flask import Flask
app=Flask(__name__)

@app.route('/hello',methods=['GET','POST'],endpoint='hello')
def hello():
    return 'Hello World!'

@app.route('/hi',methods=['GET','POST'],endpoint='hi')
def hi():
    return 'hi hi'

if __name__ == '__main__':
    app.run()