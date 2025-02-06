from flask import Flask
app=Flask(__name__)
@app.route('/user/<int:id>')
def index(id):
    if id==1:
        return 'python'
    if id==2:
        return 'django'
    if id==3:
        return 'flask'
    return 'hello world'

if __name__=='__main__':
    app.run()
