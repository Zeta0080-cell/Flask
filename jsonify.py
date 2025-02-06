from flask import Flask,make_response,json,jsonify

app=Flask(__name__)
app.config['JSON_AS_ASCII']=False
@app.route('/index')
def index():
    data={
        'name':'张三'
    }
    return jsonify(data)
    #直接将data转换为json并返回给前端
if __name__=='__main__':
    app.run()
