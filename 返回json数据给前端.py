from flask import Flask,make_response,json,jsonify

app=Flask(__name__)

@app.route('/index')
def index():
    data={
        'name':'张三'
    }
    response = make_response(json.dumps(data,ensure_ascii=False))
    response.mitetype='application/json'
    #转换为json数据
    return response
    #返回给前端
if __name__=='__main__':
    app.run()
