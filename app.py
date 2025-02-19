from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)

# MySQL配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'competition_db'

mysql = MySQL(app)

# 创建数据库和表的SQL语句
create_db_query = """
CREATE DATABASE IF NOT EXISTS competition_db;
"""

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
"""

@app.before_first_request
def create_tables():
    cursor = mysql.connection.cursor()
    cursor.execute(create_db_query)
    cursor.execute(create_table_query)
    mysql.connection.commit()

# 注册路由
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        return jsonify({'message': '用户名已存在'}), 400

    # 使用bcrypt加密密码
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    mysql.connection.commit()

    return jsonify({'message': '注册成功'}), 201

if __name__ == '__main__':
    app.run(debug=True)